from tkinter import filedialog
import random
from docx import Document

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
    return file_path

def generate_poem(linecount_var, selectfile_var):
    lines = []
    if selectfile_var.endswith('.docx'):
        doc = Document(selectfile_var)
        lines = [para.text for para in doc.paragraphs if para.text.strip() != '']
    else:
        with open(selectfile_var, 'r') as file:
            lines = file.readlines()
    
    selected_lines = random.sample(lines, min(len(lines), linecount_var))
    poem = "\n".join(line.strip() for line in selected_lines)
    return poem

def save_file(poem):
    output_file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if output_file_name:
        with open(output_file_name, 'w') as file:
            file.write(poem)
        print(f"Poem saved to {output_file_name}")