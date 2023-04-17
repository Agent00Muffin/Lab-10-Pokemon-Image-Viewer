import poke_api
from tkinter import *
from tkinter import ttk
import os
import ctypes
import image_lib


# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')
# Make image cache folder if it does not exist
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create the main window
root = Tk()
root.title("Pokemon Image Viewer")
root.minsize(550, 550)
# Set the window icon
icon_path = os.path.join(script_dir, 'Ultra_Ball.ico')
root.iconbitmap(icon_path)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# Create Frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Add Image to the frame
img_poke = PhotoImage(file=os.path.join(script_dir, 'poke_logo.png'))
lbl_poke_image = ttk.Label(frame, image=img_poke)
lbl_poke_image.grid(row=0, column=0)

# Add pokemon names pull-down list to the frame
pokemon_name_list = poke_api.get_pokemon_names()
cbox_poke_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_poke_names.set("Select a Pokémon")
cbox_poke_names.grid(padx=10, pady=10, row=1, column=0)

def handle_pokemon_sel(event):
    # Get the name of the selected pokemon
    pokemon_name = cbox_poke_names.get()
    # Download and save the art for the selected pokemon
    global image_path
    image_path = poke_api.download_pokemon_artwork(pokemon_name, image_cache_dir)
    # Display the pokemon art
    if image_path is not None:
        img_poke['file'] = image_path
    # Enable button
    btn_set_desktop.state(['!disabled'])

cbox_poke_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)

def set_background():
    return image_lib.set_desktop_background_image(image_path)

# Add desktop image button
btn_set_desktop = ttk.Button(frame, text='Set as Desktop Image', state=DISABLED, command=set_background)
btn_set_desktop.grid(padx=10, pady=10, row=2, column=0)


root.mainloop()