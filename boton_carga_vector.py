# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 21:15:35 2025

@author: mariano
"""
import tkinter as tk

def button_clicked():
    print("apretado!")
    
    
root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Cantidad de personas", 
                   e1 = Entry(root),
                   e1.grid(row=0, column=1),
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="Green",
                   font=("Arial", 14),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()

#%%
from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END)
mainloop()


#%%

import tkinter

app = tkinter.Tk()

# Create a set for all clicked buttons (set prevents duplication)
clicked = set()
# Create a tuple of words (your 180 verb goes here)
words = 'hello', 'world', 'foo', 'bar', 'baz', 'egg', 'spam', 'ham'

# This function will run when pressing the space bar
def on_spacebar_press( event ):
    print( 'Clicked words:', *clicked )

# Button creator function
def create_buttons( words ):
    # Create a button for each word
    for word in words:
        # This function will run when a button is clicked
        def on_button_click(word=word):
            clicked.add( word )
        # Add button
        button = tkinter.Button( app,
                                 text=word,
                                 command=on_button_click )
        # If you have 180 buttons, you should consider using the grid()
        # layout instead of pack() but for simplicity I used this one for demo
        button.pack()

# Binding function tp space bar event
app.bind('<space>', on_spacebar_press)

# This call creates the buttons
create_buttons( words )

# Now we enter to event loop -> the program is running
app.mainloop()





#%%

import tkinter as tk

root = tk.Tk()
root.title("Boton de prueba")

# Create a button with active background and foreground colors
button = tk.Button(root, text="Ok", activebackground="blue", activeforeground="white")
button.pack()

# Create a label with background and foreground colors
label = tk.Label(root, text="Cantidad de personas", bg="lightgray", fg="black")
label.pack()

# Create an Entry widget with selection colors
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
entry.pack()

root.mainloop()

button.bind(handler=print("lsito"))
