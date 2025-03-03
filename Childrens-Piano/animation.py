# Author: Matthew O'Keefe
# Created: 01/27/2025
# Description: Animation methods and the gif file paths used.

# Needed for the animations
from PIL import Image, ImageTk

# Keep track of the current animation category. Starts with animal category.
current_category = "animal"

# Global variable to store the ID of the current animation task
current_animation_task = None

# Method to switch categories between animal and pokemon
def switch_category():
    global current_category
    current_category = "pokemon" if current_category == "animal" else "animal"  # Toggle category

# Method to display the animation for the last pressed note
def trigger_animation(note, canvas):
    global current_category, current_animation_task

    # Cancel the current animation if it's running
    if current_animation_task is not None:
        canvas.after_cancel(current_animation_task)
        current_animation_task = None 

    # Animal and pokemon gif paths
    animal_animations = {
        "C4": ["gifs/animals/cat.gif"],
        "Cs4": ["gifs/animals/cat.gif"],
        "D4": ["gifs/animals/dog.gif"],
        "Ds4": ["gifs/animals/dog.gif"],
        "E4": ["gifs/animals/elephant.gif"],
        "F4": ["gifs/animals/frog.gif"],
        "Fs4": ["gifs/animals/frog.gif"],
        "G4": ["gifs/animals/gorilla.gif"],
        "Gs4": ["gifs/animals/gorilla.gif"],
        "A4": ["gifs/animals/alpaca.gif"],
        "As4": ["gifs/animals/alpaca.gif"],
        "B4": ["gifs/animals/bat.gif"],
        "C5": ["gifs/animals/cat.gif"],
        "Cs5": ["gifs/animals/cat.gif"],
        "D5": ["gifs/animals/dog.gif"],
        "Ds5": ["gifs/animals/dog.gif"],
        "E5": ["gifs/animals/elephant.gif"],
        "F5": ["gifs/animals/frog.gif"],
        "Fs5": ["gifs/animals/frog.gif"],
        "G5": ["gifs/animals/gorilla.gif"],
        "Gs5": ["gifs/animals/gorilla.gif"],
        "A5": ["gifs/animals/alpaca.gif"],
        "As5": ["gifs/animals/alpaca.gif"],
        "B5": ["gifs/animals/bat.gif"]
    }

    pokemon_animations = {
        "C4": ["gifs/pokemon/charmander.gif"],
        "Cs4": ["gifs/pokemon/charmander.gif"],
        "D4": ["gifs/pokemon/ditto.gif"],
        "Ds4": ["gifs/pokemon/ditto.gif"],
        "E4": ["gifs/pokemon/eevee.gif"],
        "F4": ["gifs/pokemon/flareon.gif"],
        "Fs4": ["gifs/pokemon/flareon.gif"],
        "G4": ["gifs/pokemon/gengar.gif"],
        "Gs4": ["gifs/pokemon/gengar.gif"],
        "A4": ["gifs/pokemon/aggron.gif"],
        "As4": ["gifs/pokemon/aggron.gif"],
        "B4": ["gifs/pokemon/bulbasaur.gif"],
        "C5": ["gifs/pokemon/charmander.gif"],
        "Cs5": ["gifs/pokemon/charmander.gif"],
        "D5": ["gifs/pokemon/ditto.gif"],
        "Ds5": ["gifs/pokemon/ditto.gif"],
        "E5": ["gifs/pokemon/eevee.gif"],
        "F5": ["gifs/pokemon/flareon.gif"],
        "Fs5": ["gifs/pokemon/flareon.gif"],
        "G5": ["gifs/pokemon/gengar.gif"],
        "Gs5": ["gifs/pokemon/gengar.gif"],
        "A5": ["gifs/pokemon/aggron.gif"],
        "As5": ["gifs/pokemon/aggron.gif"],
        "B5": ["gifs/pokemon/bulbasaur.gif"],
    }

    # Depending on the selected category, choose the animations
    animations = animal_animations if current_category == "animal" else pokemon_animations

    # Open the gif using PIL and extract the frames
    gif = Image.open(animations[note][0])

    frames = []
    try:
        while True:
            # Append a PhotoImage object for each frame in the GIF
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(gif.tell() + 1)  
    except EOFError:
        pass 

    # Store frames in list
    def update_frame(frame_index):
        global current_animation_task

        # Clear the canvas before displaying the next frame
        canvas.delete("all")
        canvas.create_image(275, 190, image=frames[frame_index])
        if frame_index + 1 < len(frames):
            current_animation_task = canvas.after(25, update_frame, (frame_index + 1))  # Continue to the next frame
        else:
            current_animation_task = None  # Reset the task ID when done

    update_frame(0)  # Start from the first frame