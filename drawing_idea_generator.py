import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd

character_list = ['Batman', 'your favourite superhero', 'a capybara', 'Kermit the frog', 'a witch',
                  'Yoda']
action_list = ['as a hogwarts student', 'in a halloween costume', 'chilling at the pool', 'at a music concert',
               'skating', 'in a christmas sweater', 'if they were in a Western']

material_list = ['digital art', 'watercolour', 'acrylic paint', 'gouache', 'graphite', 'alcohol markers',
                 'oil pastel', 'coloured pencils', 'spray paint', 'fine liner', 'paper cutout']

style_list = ['realistic', 'manga', 'impressionistic', 'expressionistic', 'Disney', 'semi-realistic', 'cartoon']


landscape_list = ['forest', 'beach', 'meadow', 'mountains', 'tundra']


# create gui window
root = tk.Tk()

# give window a title
root.title('Drawing Idea Generator')

# change background colour
root.configure(background='powderblue')

# configure the size
screen_height = 650
screen_width = 800
root.minsize(width=screen_width, height=screen_height)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a frame for each page
home_frame = tk.Frame(root, height=600, background='powderblue')
favourites_frame = tk.Frame(root, background='cadetblue', height=600)
landscape_frame = tk.Frame(root, background='powderblue', height=600)

page_frames = [home_frame, favourites_frame, landscape_frame]

# Configure layout for each page
for i in page_frames:
    i.grid_columnconfigure(0, weight=1)
    i.grid_columnconfigure(1, weight=1)
    i.grid_columnconfigure(2, weight=1)
    i.grid_columnconfigure(3, weight=1)
    i.grid_columnconfigure(4, weight=1)

    i.grid_rowconfigure(0, weight=1)
    i.grid_rowconfigure(1, weight=1)
    i.grid_rowconfigure(2, weight=2)
    i.grid_rowconfigure(3, weight=1)


# Set background image
def set_background(frame, image_file_path):

    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0)

# Set background image for each page
set_background(home_frame, 'character_background.png')
set_background(landscape_frame, 'landscape_background.png')

# Creating a title label for homepage
title_label = tk.Label(home_frame,
                       text='wanna draw a character?',
                       background='lightpink',
                       foreground='cadetblue',
                       font=('Comic Sans MS', 24, 'bold')
                       )
title_label.grid(row=0, column=1, columnspan=3)

# Creating a title label for landscape page
landscape_title_label = tk.Label(landscape_frame,
                       text='wanna draw a landscape?',
                       background='lightpink',
                       foreground='seagreen',
                       font=('Comic Sans MS', 24, 'bold')
                       )
landscape_title_label.grid(row=0, column=1, columnspan=3)

# Create a label for generated prompt
prompt_box = tk.Label(home_frame, background='white',
                      text='',
                      font=('arial', 22),
                      foreground='teal',
                      wraplength=400)

# Create a label for generated landscape
landscape_box = tk.Label(landscape_frame, background='white',
                      text='',
                      font=('arial', 22),
                      foreground='teal',
                      wraplength=400)

# Create a frame for the additionally generated options
prompt_additions_frame = tk.LabelFrame(home_frame, background='white')
landscape_additions_frame = tk.LabelFrame(landscape_frame, background='white')

# Create a label for generated material
material_box = tk.Label(prompt_additions_frame, background='white',
                        text='',
                        font=('arial', 22),
                        foreground='teal')
landscape_material_box = tk.Label(landscape_additions_frame, background='white',
                        text='',
                        font=('arial', 22),
                        foreground='teal')

# Create a label for generated style
style_box = tk.Label(prompt_additions_frame, background='white',
                     text='',
                     font=('arial', 22),
                     foreground='teal')
landscape_style_box = tk.Label(landscape_additions_frame, background='white',
                     text='',
                     font=('arial', 22),
                     foreground='teal')

# Creating a frame for the colour palette
colour_frame = tk.LabelFrame(prompt_additions_frame, text='with these colours', background='white')
landscape_colour_frame = tk.LabelFrame(landscape_additions_frame, text='with these colours', background='white')

# Creating a label for each colour
colour1 = tk.Label(colour_frame, background='white', width=9, height=4)
colour2 = tk.Label(colour_frame, background='white', width=9, height=4)
colour3 = tk.Label(colour_frame, background='white', width=9, height=4)
colour4 = tk.Label(colour_frame, background='white', width=9, height=4)
colour5 = tk.Label(colour_frame, background='white', width=9, height=4)

landscape_colour1 = tk.Label(landscape_colour_frame, background='white', width=9, height=4)
landscape_colour2 = tk.Label(landscape_colour_frame, background='white', width=9, height=4)
landscape_colour3 = tk.Label(landscape_colour_frame, background='white', width=9, height=4)
landscape_colour4 = tk.Label(landscape_colour_frame, background='white', width=9, height=4)
landscape_colour5 = tk.Label(landscape_colour_frame, background='white', width=9, height=4)

# Create a frame to place additional options
choices_frame = tk.LabelFrame(home_frame, background='white')
choices_frame.grid(row=1, column=1, columnspan=3)

landscape_choices_frame = tk.LabelFrame(landscape_frame, background='white')
landscape_choices_frame.grid(row=1, column=1, columnspan=3)

# New frame for colour palette options
choice2_frame = tk.LabelFrame(choices_frame, background='white')
var3 = tk.StringVar(choice2_frame, "1")  # Create a variable for strings, and initialize the variable
tk.Radiobutton(choice2_frame, text="1", variable=var3, value="1").grid(row=1, column=0)
tk.Radiobutton(choice2_frame, text="3", variable=var3, value="3").grid(row=1, column=1)
tk.Radiobutton(choice2_frame, text="5", variable=var3, value="5").grid(row=1, column=2)

landscape_choice2_frame = tk.LabelFrame(landscape_choices_frame, background='white')
var5 = tk.StringVar(landscape_choice2_frame, "1")  # Create a variable for strings, and initialize the variable
tk.Radiobutton(landscape_choice2_frame, text="1", variable=var5, value="1").grid(row=1, column=0)
tk.Radiobutton(landscape_choice2_frame, text="3", variable=var5, value="3").grid(row=1, column=1)
tk.Radiobutton(landscape_choice2_frame, text="5", variable=var5, value="5").grid(row=1, column=2)

# Create variables to lock each generated part
lock_prompt = tk.IntVar()
lock_material = tk.IntVar()
lock_style = tk.IntVar()
lock_colours = tk.IntVar()

# Create buttons to lock each generated part
prompt_lock = tk.Checkbutton(home_frame, text='🔒', variable=lock_prompt)
material_lock = tk.Checkbutton(prompt_additions_frame, text='🔒', variable=lock_material)
style_lock = tk.Checkbutton(prompt_additions_frame, text='🔒', variable=lock_style)
colours_lock = tk.Checkbutton(prompt_additions_frame, text='🔒', variable=lock_colours)

landscape_lock = tk.Checkbutton(landscape_frame, text='🔒', variable=lock_prompt)
landscape_material_lock = tk.Checkbutton(landscape_additions_frame, text='🔒', variable=lock_material)
landscape_style_lock = tk.Checkbutton(landscape_additions_frame, text='🔒', variable=lock_style)
landscape_colours_lock = tk.Checkbutton(landscape_additions_frame, text='🔒', variable=lock_colours)

# Add a title to the favourites page
favourites_title_label = tk.Label(favourites_frame, text='favourites', font=('Comic Sans MS', 24, 'bold'),
                                                    background='papayawhip', foreground='cadetblue')
favourites_title_label.grid(row=0, column=1)


# random RGB colour
def random_rgb():
    r = random.randrange(257)
    g = random.randrange(257)
    b = random.randrange(257)
    # convert RGB to Hex colours
    return f'#{r:02x}{g:02x}{b:02x}'


drawing_prompt = ''
style = ''
material = ''
colour_palette = ''


# Generate a character prompt
def generate_prompt():
    global drawing_prompt, style, material, colour_palette

    favourite_button.grid(row=4, column=4)

    # Check if option is locked
    if not lock_prompt.get():
        drawing_prompt = f'{random.choice(character_list) + " " + random.choice(action_list)}'
    prompt_box.grid(row=2, column=1, columnspan=3)
    prompt_box.configure(text=drawing_prompt)
    prompt_additions_frame.grid(row=3, column=1, columnspan=3)
    prompt_lock.grid(row=2,column=4)
    if var1.get():  # If the button is checked, generate random material
        material_box.grid(row=1, column=2, columnspan=3, padx=10)
        if not lock_material.get():  # Check if locked
            material = random.choice(material_list)
        material_box.configure(text=f'using \n{material}')
        material_lock.grid(row=0, column=2, sticky='n')
    else:
        material_box.grid_remove()
        material_lock.grid_remove()
    if var4.get():  # If the button is checked, generate random style
        if not lock_style.get():  # Check if locked
            style = random.choice(style_list)
        style_box.configure(text=f'in a(n) \n{style} style')
        style_box.grid(row=1, column=1, columnspan=1, padx=10)
        style_lock.grid(row=0, column=1, sticky='n')
    else:
        style_box.grid_remove()
        style_lock.grid_remove()
    if var2.get():  # If the button is checked,generate random colour palette
        colour_frame.grid(row=1, column=0, columnspan=1, padx=5)
        choice2_frame.grid(row=1, column=3, columnspan=1, sticky='s')
        colours_lock.grid(row=0, column=0, sticky='n')
        if var3.get() == '1':  # If set to 1, generate one colour
            bg1 = random_rgb()
            colour_palette = [bg1, 'white', 'white', 'white', 'white']
            if not lock_colours.get():
                colour1.configure(background=bg1)
                colour1.grid(row=1, column=0, padx=2, pady=2)
                colour2.grid_remove()
                colour3.grid_remove()
                colour4.grid_remove()
                colour5.grid_remove()
        if var3.get() == '3':  # If set to 3, generate three colours
            bg1 = random_rgb()
            bg2 = random_rgb()
            bg3 = random_rgb()
            colour_palette = [bg1, bg2, bg3, 'white', 'white']
            if not lock_colours.get():
                colour1.grid(row=1, column=0, padx=2, pady=2)
                colour1.configure(background=bg1)
                colour2.grid(row=1, column=1, padx=2, pady=2)
                colour2.configure(background=bg2)
                colour3.grid(row=1, column=2, padx=2, pady=2)
                colour3.configure(background=bg3)
                colour4.grid_remove()
                colour5.grid_remove()
        if var3.get() == '5':  # If set to 5, generate five colours
            bg1 = random_rgb()
            bg2 = random_rgb()
            bg3 = random_rgb()
            bg4 = random_rgb()
            bg5 = random_rgb()
            colour_palette = [bg1, bg2, bg3, bg4, bg5]
            if not lock_colours.get(): # Check if locked
                colour1.grid(row=1, column=0, padx=2, pady=2)
                colour1.configure(background=bg1)
                colour2.grid(row=1, column=1, padx=2, pady=2)
                colour2.configure(background=bg2)
                colour3.grid(row=1, column=2, padx=2, pady=2)
                colour3.configure(background=bg3)
                colour4.grid(row=2, column=0, padx=2, pady=2)
                colour4.configure(background=bg4)
                colour5.grid(row=2, column=1, padx=2, pady=2)
                colour5.configure(background=bg5)
    else:
        colour_frame.grid_remove()
        choice2_frame.grid_remove()

    return drawing_prompt, material, style, colour_palette


# Generate a landscape prompt
def generate_landscape():
    global drawing_prompt, style, material, colour_palette
    landscape_favourite_button.grid(row=4, column=4)

    if not lock_prompt.get():  # Check if locked
        drawing_prompt = random.choice(landscape_list)
    landscape_box.grid(row=2, column=1, columnspan=3)
    landscape_box.configure(text=drawing_prompt)
    landscape_additions_frame.grid(row=3, column=1, columnspan=3)
    landscape_lock.grid(row=2, column=4)
    if var1.get():  # If the button is checked, generate random material
        landscape_material_box.grid(row=1, column=2, columnspan=3, padx=10)
        if not lock_material.get():  # Check if locked
            material = random.choice(material_list)
        landscape_material_box.configure(text=f'using \n{material}')
        landscape_material_lock.grid(row=0, column=2, sticky='n')
    else:
        landscape_material_box.grid_remove()
        landscape_material_lock.grid_remove()
    if var4.get():  # If the button is pressed, generate random style
        if not lock_style.get():  # Check if locked
            style = random.choice(style_list)
        landscape_style_box.configure(text=f'in a(n) \n{style} style')
        landscape_style_box.grid(row=1, column=1, columnspan=1, padx=10)
        landscape_style_lock.grid(row=0, column=1, sticky='n')
    else:
        landscape_style_box.grid_remove()
        landscape_style_lock.grid_remove()
    if var2.get():  # If the button is checked,generate random colour palette
        landscape_colour_frame.grid(row=1, column=0, columnspan=1, padx=5)
        landscape_choice2_frame.grid(row=1, column=3, columnspan=1, sticky='s')
        landscape_colours_lock.grid(row=0, column=0, sticky='n')
        if var5.get() == '1':  # If set to 1, generate one colour
            bg1 = random_rgb()
            colour_palette = [bg1, 'white', 'white', 'white', 'white']
            if not lock_colours.get():  # Check if locked
                landscape_colour1.configure(background=bg1)
                landscape_colour1.grid(row=1, column=0, padx=2, pady=2)
                landscape_colour2.grid_remove()
                landscape_colour3.grid_remove()
                landscape_colour4.grid_remove()
                landscape_colour5.grid_remove()
        if var5.get() == '3':  # If set to 3, generate three colours
            bg1 = random_rgb()
            bg2 = random_rgb()
            bg3 = random_rgb()
            colour_palette = [bg1, bg2, bg3, 'white', 'white']
            if not lock_colours.get():
                landscape_colour1.grid(row=1, column=0, padx=2, pady=2)
                landscape_colour1.configure(background=bg1)
                landscape_colour2.grid(row=1, column=1, padx=2, pady=2)
                landscape_colour2.configure(background=bg2)
                landscape_colour3.grid(row=1, column=2, padx=2, pady=2)
                landscape_colour3.configure(background=bg3)
                landscape_colour4.grid_remove()
                landscape_colour5.grid_remove()
        if var5.get() == '5':  # If set to 5, generate five colours
            bg1 = random_rgb()
            bg2 = random_rgb()
            bg3 = random_rgb()
            bg4 = random_rgb()
            bg5 = random_rgb()
            colour_palette = [bg1, bg2, bg3, bg4, bg5]
            if not lock_colours.get():
                landscape_colour1.grid(row=1, column=0, padx=2, pady=2)
                landscape_colour1.configure(background=bg1)
                landscape_colour2.grid(row=1, column=1, padx=2, pady=2)
                landscape_colour2.configure(background=bg2)
                landscape_colour3.grid(row=1, column=2, padx=2, pady=2)
                landscape_colour3.configure(background=bg3)
                landscape_colour4.grid(row=2, column=0, padx=2, pady=2)
                landscape_colour4.configure(background=bg4)
                landscape_colour5.grid(row=2, column=1, padx=2, pady=2)
                landscape_colour5.configure(background=bg5)

    else:
        landscape_colour_frame.grid_remove()
        landscape_choice2_frame.grid_remove()

    return drawing_prompt, material, style, colour_palette


# Save the generated idea
def save_idea():
    global drawing_prompt, material, style, colour_palette

    # Prepare the data to save
    idea_data = {
        "drawing_prompt": [drawing_prompt],
        "material": [material],
        "style": [style],
        'colour_palette': [colour_palette]
    }
    # Convert to DataFrame and save to CSV
    idea_df = pd.DataFrame(idea_data)
    idea_df.to_csv('data/saved_ideas.csv', index=False, header=False, mode='a')

    tk.messagebox.showinfo("Saved", "idea has been added to favourites. yay :D")


idea_number = 0


# Display each saved idea
def show_saved_ideas():

    global saved_ideas, idea_number

    # Retrieve the data from the file
    saved_ideas = pd.read_csv('data/saved_ideas.csv')

    # Ensure that idea_number is within range of saved ideas
    if idea_number < 0:
        idea_number = 0
    elif idea_number >= len(saved_ideas):
        idea_number = len(saved_ideas) - 1
    idea_drawing_prompt = saved_ideas['drawing_prompt'].iloc[idea_number]
    idea_material = saved_ideas['material'].iloc[idea_number]
    idea_style = saved_ideas['style'].iloc[idea_number]
    colour_str = str(saved_ideas['colour_palette'].iloc[idea_number])[1:-1]
    idea_frame = tk.LabelFrame(favourites_frame, text="Idea")
    idea_frame.grid(row=1, column=1, sticky='nsew')

    # Turn information from the file into a readable list of colours
    idea_colours = [color.strip().strip("'") for color in colour_str.split(',')]

    idea_prompt_label = tk.Label(idea_frame, text=idea_drawing_prompt)
    idea_prompt_label.grid(row=1, column=0, padx=8)
    idea_material_label = tk.Label(idea_frame, text=idea_material, background='lightpink')
    if not pd.isnull(idea_material):  # Only show label if material was saved
        idea_material_label.grid(row=1, column=1, padx=8)
    idea_style_label = tk.Label(idea_frame, text=idea_style, background='powderblue')
    if not pd.isnull(idea_style):  # Only show label if style was saved
        idea_style_label.grid(row=1, column=2, padx=8)
    idea_colour_frame = tk.LabelFrame(idea_frame)
    idea_colour_frame.grid(row=2, column=1)
    idea_colour1 = tk.Label(idea_colour_frame, width=9, height=4)
    idea_colour1.configure(background=idea_colours[0])
    idea_colour2 = tk.Label(idea_colour_frame, width=9, height=4)
    idea_colour2.configure(background=idea_colours[1])
    idea_colour3 = tk.Label(idea_colour_frame, width=9, height=4)
    idea_colour3.configure(background=idea_colours[2])
    idea_colour4 = tk.Label(idea_colour_frame, width=9, height=4)
    idea_colour4.configure(background=idea_colours[3])
    idea_colour5 = tk.Label(idea_colour_frame, width=9, height=4)
    idea_colour5.configure(background=idea_colours[4])
    idea_colour1.grid(row=1, column=0, padx=2, pady=2)
    idea_colour2.grid(row=1, column=1, padx=2, pady=2)
    idea_colour3.grid(row=1, column=2, padx=2, pady=2)
    idea_colour4.grid(row=2, column=0, padx=2, pady=2)
    idea_colour5.grid(row=2, column=1, padx=2, pady=2)

    return saved_ideas


def previous_idea():
    global idea_number
    idea_number = idea_number - 1
    show_saved_ideas()
    next_idea_button.grid(row=2, column=4)


# Button to switch to the previous idea
previous_idea_button = tk.Button(favourites_frame, text='🠔', command=previous_idea)
previous_idea_button.grid(row=2, column=0)

if idea_number == 0:
    previous_idea_button.grid_remove()


def next_idea():
    global idea_number, saved_ideas
    idea_number = idea_number + 1
    previous_idea_button.grid(row=2, column=0)
    show_saved_ideas()


# Button to switch to the next idea
next_idea_button = tk.Button(favourites_frame, text='➞', command=next_idea)
next_idea_button.grid(row=2, column=3)


# Create a generate button
image1 = tk.PhotoImage(file='generate_gif.gif')
generate_button_image = image1.subsample(2, 2)
generate_button = tk.Button(home_frame,
                            text='Generate',
                            borderwidth=0,
                            image=generate_button_image,
                            command=generate_prompt)

generate_button.grid(row=4, column=1, columnspan=3, pady=20)

generate_landscape_button = tk.Button(landscape_frame, image=generate_button_image,
                            borderwidth=0, command=generate_landscape)
generate_landscape_button.grid(row=4, column=1, columnspan=3, pady=20)

image2 = tk.PhotoImage(file='stern1.png')
favourite_button = tk.Button(home_frame, image=image2, borderwidth=0,
                                background='powderblue', command=save_idea)
landscape_favourite_button = tk.Button(landscape_frame, image=image2, borderwidth=0,
                                background='palegreen', command=save_idea)

image3 = tk.PhotoImage(file='view_favourites.png')

var1 = tk.IntVar()  # variable class
var2 = tk.IntVar()
var4 = tk.IntVar()

# Button to choose whether to generate material
choice1 = tk.Checkbutton(choices_frame, text='random material', variable=var1)
choice1.grid(row=0, column=2, columnspan=1, padx=3)

landscape_choice1 = tk.Checkbutton(landscape_choices_frame, text='random material', variable=var1)
landscape_choice1.grid(row=0, column=2, columnspan=1, padx=3)

# Button to choose whether to generate colour palette
choice2 = tk.Checkbutton(choices_frame, text='colour palette', variable=var2)
choice2.grid(row=0, column=3, columnspan=1, padx=3)

landscape_choice2 = tk.Checkbutton(landscape_choices_frame, text='colour palette', variable=var2)
landscape_choice2.grid(row=0, column=3, columnspan=1, padx=3)

# Button to choose whether to generate style
choice3 = tk.Checkbutton(choices_frame, text='random style', variable=var4)
choice3.grid(row=0, column=1, columnspan=1, padx=3)

landscape_choice3 = tk.Checkbutton(landscape_choices_frame, text='random style', variable=var4)
landscape_choice3.grid(row=0, column=1, columnspan=1, padx=3)


# Create a homepage
def create_homepage():
    # remove all other widgets
    for i in root.winfo_children():
        i.grid_remove()
    view_favourites_button = tk.Button(home_frame, text='view favourites', image=image3, command=create_favourites_page)
    view_favourites_button.grid(row=0, column=4, sticky='s')
    home_frame.grid(row=0, column=0, sticky='nsew')


# Button to switch from landscape to character generation
image5 = tk.PhotoImage(file='character_button.png')
character_button = tk.Button(landscape_frame, text='generate character instead', image=image5, command=create_homepage)
character_button.grid(row=4, column=0)


# Create a favourites page
def create_favourites_page():
    for i in root.winfo_children():
        i.grid_remove()

    favourites_frame.grid(row=0, column=0, sticky='nsew')
    home_button = tk.Button(favourites_frame, text='⌂', font=('arial', 44), command=create_homepage,
                            background='papayawhip', foreground='purple')
    home_button.grid(row=3, column=1)
    show_saved_ideas()


# Create a landscape page
def create_landscape_page():
    for i in root.winfo_children():
        i.grid_remove()
    view_favourites_button = tk.Button(landscape_frame, text='view favourites', image=image3, command=create_favourites_page)
    view_favourites_button.grid(row=0, column=4, sticky='s')
    landscape_frame.grid(row=0, column=0, sticky='nsew')
    character_button.grid(row=4, column=0)


# Button to switch from character to landscape generation
image4 = tk.PhotoImage(file='landscape_button.png')
landscape_button = tk.Button(home_frame, text='generate landscape instead', image=image4, borderwidth=0,
                             command=create_landscape_page)
landscape_button.grid(row=4, column=0)

# Show homepage when opening the app
create_homepage()


root.mainloop()
