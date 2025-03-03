import re
import datetime
import pytz
from datetime import datetime
from location_coordinates import get_location_info
from pymongo import MongoClient
from config.keys import mongoURI


def parse_event(event_text):
    # Extract each field using regex
    name_match = re.search(r'EventName: (.*?)(?:\n|$)', event_text)
    desc_match = re.search(r'EventDescription: (.*?)(?:\n|$)', event_text)
    time_match = re.search(r'EventTime: (.*?)(?:\n|$)', event_text)
    location_match = re.search(r'EventLocation: (.*?)(?:\n|$)', event_text)
    
    # Extract the values
    event_name = name_match.group(1) if name_match else ""
    event_description = desc_match.group(1) if desc_match else ""
    event_time_full = time_match.group(1) if time_match else ""
    event_location = location_match.group(1) if location_match else ""
    
    # Split the time_full into date and time parts
    date_time_parts = event_time_full.split(" ", 3)
    
    if len(date_time_parts) >= 4:
        event_date = f"{date_time_parts[0]} {date_time_parts[1]} {date_time_parts[2]}"
        event_time = date_time_parts[3]
    else:
        event_date = ""
        event_time = event_time_full
    
    # Parse the date and start time to create ISO 8601 timestamp
    cleaned_date = event_date.replace(".", "")
    current_year = datetime.now().year  # Get current year
    
    # Combine date and time for parsing
    start_time = event_time.split(" - ")[0]
    date_time_str = f"{cleaned_date} {start_time} {current_year}"
    
    try:
        # Create datetime object in EST timezone
        est = pytz.timezone('US/Eastern')
        event_datetime = datetime.strptime(date_time_str, "%A, %b %d %I:%M %p %Y")
        event_datetime_est = est.localize(event_datetime)
        
        # Convert to UTC
        event_datetime_utc = event_datetime_est.astimezone(pytz.UTC)
        
        # Format to ISO 8601
        event_timestamp = event_datetime_utc.strftime("%Y-%m-%dT%H:%M:%S")
    except Exception as e:
        # If date parsing fails, provide an empty timestamp
        event_timestamp = ""
        print(f"Error parsing date/time: {e}")
    
    # Get location coordinates and image URL
    x_coord, y_coord, image_url = get_location_info(event_location)
    
    # Construct the modified event
    modified_event = {
        "eventName": event_name,
        "eventBio": event_description,
        "eventTime": event_time,
        "eventDate": event_date,
        "eventDateTime": event_timestamp,
        "eventLocation": event_location
    }
    
    # Add coordinates if available
    if x_coord is not None and y_coord is not None:
        modified_event["xCoord"] = x_coord
        modified_event["yCoord"] = y_coord
    
    # Add image URL if available
    if image_url is not None:
        modified_event["eventImageUrl"] = image_url
    
    return modified_event

def format_event(event_dict):
    """Format event dictionary back to text format"""
    output = ""
    for key, value in event_dict.items():
        output += f"{key}: {value}\n"
    return output.strip()

def parse_events_to_mongodb(events_text):
    """
    Parse multiple events and prepare them for MongoDB insertion
    Returns a list of event dictionaries
    """
    # Split the text into individual events (assuming events are separated by blank lines)
    event_blocks = re.split(r'\n\s*\n', events_text)
    
    # Parse each event
    parsed_events = [parse_event(event) for event in event_blocks if event.strip()]
    
    return parsed_events

def upload_events_to_mongodb(events):
    """
    Upload parsed events to MongoDB
    """
    try:
        # MongoDB connection
        uri = mongoURI
        client = MongoClient(uri)
        database = client["loginGameDatabase"]
        collection = database["events"]
        
        # Insert events into MongoDB
        result = collection.insert_many(events)
        print(f"Inserted event IDs: {result.inserted_ids}")
        
        # Ping the database to confirm connection
        client.admin.command("ping")
        print("Connected successfully")
        
        # Close the client connection
        client.close()
    
    except Exception as e:
        print(f"Error uploading events to MongoDB: {e}")

def main():
    # Read the contents of formatted_events.txt
    with open('formatted_events.txt', 'r') as file:
        events_content = file.read()
    
    # Split the content into individual events
    events = events_content.split('\n\n\n')
    
    # Parse and reformat each event
    reformatted_events = []
    for event in events:
        parsed_event = parse_event(event)
        reformatted_event = format_event(parsed_event)
        reformatted_events.append(reformatted_event)
    
    # Write the reformatted events to reformatted_events.txt
    with open('reformatted_events.txt', 'w') as file:
        file.write('\n\n\n'.join(reformatted_events))
    
    print("Reformatted events have been written to reformatted_events.txt")
    
    # Parse events for MongoDB
    parsed_events = parse_events_to_mongodb(events_content)
    
    # Upload parsed events to MongoDB
    upload_events_to_mongodb(parsed_events)

if __name__ == "__main__":
    main()