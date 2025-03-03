import re
import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email import message_from_bytes
from email.message import EmailMessage
import html2text

# Define the scopes needed to access Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def get_gmail_service():
    """Set up and return Gmail service with appropriate credentials."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("config/token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("config/credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)

def extract_email_content(part):
    """Extract content from email part, handling different content types."""
    content = ""
    if part.get_content_type() == "text/plain":
        content = part.get_payload(decode=True).decode('utf-8', errors='replace')
    elif part.get_content_type() == "text/html":
        html_content = part.get_payload(decode=True).decode('utf-8', errors='replace')
        # Convert HTML to plain text
        h = html2text.HTML2Text()
        h.ignore_links = False
        content = h.handle(html_content)
    return content

def get_email_content(message):
    """Process email message and extract its content."""
    content = ""
    
    if message.is_multipart():
        # Handle multipart messages
        for part in message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is not None:
                continue  # Skip attachments
            content += extract_email_content(part)
    else:
        # Handle single part messages
        content = extract_email_content(message)
    
    # Replace � with -
    content = content.replace('�', '-')
    
    return content

def clean_filename(subject):
    """Create a safe filename from email subject."""
    # Remove invalid filename characters
    safe_subject = re.sub(r'[<>:"/\\|?*]', '', subject)
    # Limit length and remove trailing spaces
    safe_subject = safe_subject.strip()[:50]
    return safe_subject or "no_subject"

def fetch_emails(service, sender_email):
    """Fetch emails from specified sender and save contents to files."""
    # Create output directory if it doesn't exist
    output_dir = "email_contents"
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Get list of messages from sender
        results = service.users().messages().list(
            userId="me",
            q=f"from:{sender_email}",
            maxResults=50  # Adjust as needed
        ).execute()
        
        messages = results.get("messages", [])

        if not messages:
            print("No emails found.")
            return

        print(f"Found {len(messages)} emails from {sender_email}")

        for idx, msg in enumerate(messages, 1):
            try:
                # Get full message data
                msg_data = service.users().messages().get(
                    userId="me",
                    id=msg["id"],
                    format="raw"
                ).execute()
                
                # Decode the raw message
                msg_bytes = base64.urlsafe_b64decode(msg_data["raw"])
                email_msg = message_from_bytes(msg_bytes)
                
                # Get subject for filename
                subject = email_msg.get("subject", f"email_{idx}")
                safe_filename = clean_filename(subject)
                
                # Extract content
                content = get_email_content(email_msg)
                
                # Save to file
                filepath = os.path.join(output_dir, f"{safe_filename}_{idx}.txt")
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(f"Subject: {subject}\n")
                    file.write(f"From: {email_msg['from']}\n")
                    file.write(f"Date: {email_msg['date']}\n")
                    file.write("\n" + "="*50 + "\n\n")
                    file.write(content)
                
                print(f"Saved email {idx} to {filepath}")
                
            except Exception as e:
                print(f"Error processing email {idx}: {str(e)}")
                continue

    except Exception as e:
        print(f"Error fetching emails: {str(e)}")

def main():
    """Main function to run the email fetcher."""
    try:
        sender = input("Enter the sender's email address: ")
        gmail_service = get_gmail_service()
        fetch_emails(gmail_service, sender)
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()