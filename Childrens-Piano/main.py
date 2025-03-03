# Author: Matthew O'Keefe
# Created: 01/27/2025
# Description: A simple piano app using Tkinter and Pygame libraries.
#              There are two rows of keys compromising the fourth and fifth octaves.
#              Each note triggers an animation from one of two sets, animal or pokemon.
#  
# pygame sound and GUI functionality adapted from:
# https://codewithcurious.com/projects/creating-gui-piano-using-python/
#


from tkinter import *
import pygame
from animation import trigger_animation, switch_category  # Import the animation trigger function

# initializing the pygame
pygame.init()

# Main Tkinter window
root = Tk()
root.title("Piano App")
root.geometry("1165x920+0+0")
root.configure(background="gray")

# Frames for layout
abc = Frame(root, bg="orange", bd=20, relief=RIDGE) #
abc.grid()
abc1 = Frame(abc, bg="lightgray", bd=20, relief=RIDGE) # Animation Canvas
abc1.grid()
abc2 = Frame(abc, bg="beige", relief=RIDGE)   
abc2.grid(row = 1, column = 0, columnspan = 12)

# StringVar for display
str = StringVar()

# Setup pygame sound channel
channel = pygame.mixer.Channel(0)

# Setup Canvas for animation at the top
animation_canvas = Canvas(abc1, width=550, height=380, bg="black")
animation_canvas.grid(row=0, column=0, columnspan=12, padx=5, pady=20)

def play_note(note_file):
    channel.stop()  # Stop any currently playing sound
    sound = pygame.mixer.Sound(note_file)
    channel.play(sound)

def play_note_and_trigger_animation(note, sound_file):
    str.set(note)
    play_note(sound_file)
    trigger_animation(note, animation_canvas)  # Call the animation function from the animation.py script

# Paths for each note sound file
note_files = {
    "C4": "NewSounds/C4.wav",
    "Cs4": "NewSounds/C#4.wav",
    "D4": "NewSounds/D4.wav",
    "Ds4": "NewSounds/D#4.wav",
    "E4": "NewSounds/E4.wav",
    "F4": "NewSounds/F4.wav",
    "Fs4": "NewSounds/F#4.wav",
    "G4": "NewSounds/G4.wav",
    "Gs4": "NewSounds/G#4.wav",
    "A4": "NewSounds/A4.wav",
    "As4": "NewSounds/A#4.wav",
    "B4": "NewSounds/B4.wav",
    "C5": "NewSounds/C5.wav",
    "Cs5": "NewSounds/C#5.wav",
    "D5": "NewSounds/D5.wav",
    "Ds5": "NewSounds/D#5.wav",
    "E5": "NewSounds/E5.wav",
    "F5": "NewSounds/F5.wav",
    "Fs5": "NewSounds/F#5.wav",
    "G5": "NewSounds/G5.wav",
    "Gs5": "NewSounds/G#5.wav",
    "A5": "NewSounds/A5.wav",
    "As5": "NewSounds/A#5.wav",
    "B5": "NewSounds/B5.wav",
}

# Create button for each piano key
def create_key_button(note, row, column):
    button = Button(abc2, text=note, width=4, height=6, font=("arial", 18, "bold"),
                    command=lambda: play_note_and_trigger_animation(note, note_files[note]))
    button.grid(row=row, column=column, padx=5, pady=5)

# Create piano key buttons for each note
notes = ["C4", "Cs4", "D4", "Ds4", "E4", "F4", "Fs4", "G4", "Gs4", "A4", "As4", "B4", "C5", "Cs5", "D5", "Ds5", "E5", "F5", "Fs5", "G5", "Gs5", "A5", "As5", "B5"]
for idx, note in enumerate(notes):
    create_key_button(note, idx // 12 + 1, idx % 12)  # Adjust row number for the second row

# Button that switches between animal and pokemon animation sets
btnSwitchAnimation = Button(abc2, bd=4, width=14, height=3, text="Change Animations", bg="gold", fg="black", 
                            font=("arial", 12, "bold"), command=switch_category)
btnSwitchAnimation.grid(row=1, column=13, padx=5, pady=5)  

# Main loop
root.mainloop()