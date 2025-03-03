import time                 # Used for timestamps in MongoDB
import os                   # Accessing file paths
from tkinter import *       # GUI components
from tkinter import ttk     # Themed widgets
from functions import open_file, generate_poem, save_file   # Import functions from functions.py
from mongo import client    # Import the MongoDB client from mongo.py
#from PIL import Image, ImageTk

# Set up MongoDB database and collection
db = client['poetry_db']
collection = db['poems']

# Create the main window
root = Tk() 
root.title("Poetry Generator")
root.geometry("1165x920+0+0")

# Load the background image
#background_image = PhotoImage(file="PoetryBird.png")

#background = Label( root, image = background_image) 
#background.pack(fill="both", expand=True)
#background.grid(row=1, column=0, columnspan=1, ipady=30, ipadx=10)

title = Label(root, text="Poetry Generator", font=("Arial", 30))
title.grid(row=0, column=0, columnspan=3, pady=10)

intro_text = (
    "To use this application, select a word document of a poem you would like to rearrange.\n"
    "Then, select the number of lines you would like to generate and click 'Generate New Poem'.\n"
    "You can save the generated poem as a local .txt file or save it to MongoDB.\n"
    "Feel free to make edits to the generated poem before saving.\n"
)

intro = Label(root, text=intro_text, font=("Arial", 14))
intro.grid(row=1, column=0, columnspan=3, pady=10)

linecount_var = IntVar(value=1)
linecount = Spinbox(root, textvariable=linecount_var, font=("Arial", 20), bg="lightgray", from_=1, to=16, width=3)
linecount.grid(row=2, column=0, columnspan=3, pady=10)

selectfile_var = StringVar(root, value="NULL")

def select_file():
    file_path = open_file()
    selectfile_var.set(file_path)

selectfile = ttk.Button(root, text='Select File', width=25, command=select_file)
selectfile.grid(row=3, column=0, columnspan=3, pady=10)

poem_display = Text(root, height=20, width=2, font=("Arial", 14))
poem_display.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")

def create_poem():
    num_lines = linecount_var.get()
    file_path = selectfile_var.get()
    poem = generate_poem(num_lines, file_path)
    poem_display.delete(1.0, END)
    poem_display.insert(END, poem)

createpoem = ttk.Button(root, text='Generate New Poem', width=25, command=create_poem)
createpoem.grid(row=5, column=0, columnspan=3, pady=10)

def save_poem():
    poem = poem_display.get(1.0, END)
    save_file(poem)

savepoem = ttk.Button(root, text='Save Poem', width=25, command=save_poem)
savepoem.grid(row=7, column=0, columnspan=1, pady=10)

def save_poem_to_mongodb():
    poem = poem_display.get(1.0, END)
    file_path = selectfile_var.get()
    file_title = os.path.basename(file_path)  # Extract the filename from the file path
    poem_data = {
        "poem": poem,
        "title": file_title,  # Add the filename as the title
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    collection.insert_one(poem_data)
    print("Poem saved to MongoDB")

savemongodb = ttk.Button(root, text='Save to MongoDB', width=25, command=save_poem_to_mongodb)
savemongodb.grid(row=7, column=2, columnspan=1, pady=10)

close = ttk.Button(root, text='Close App', width=25, command=root.destroy)
close.grid(row=8, column=0, columnspan=3, pady=10)

# Configure grid weights to ensure proper resizing
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


mainloop()