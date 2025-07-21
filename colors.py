# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 22:24:41 2025

@author: JdeDios4
"""

import tkinter as tk

def rgb_to_hex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

#Define RGB value (0-255)

r = 235
g = 250
b = 250

#convert to hex
color_hex = rgb_to_hex(r,g,b)

#create GUI window
root = tk.Tk()
root.title(f'RGB color: {r},{g},{b}')

canvas = tk.Canvas(root, width=300, height=100)
canvas.pack()

#Draw rectangle with RGB color
canvas.create_rectangle(0,0,300,100,fill=color_hex)

root.mainloop()