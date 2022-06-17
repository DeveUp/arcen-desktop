import tkinter as tk
from tkinter import font,Label


root = tk.Tk()
for font in font.families():
    print(font)
    if(font!=Integer):
        lb = Label(root, text="Se registra intento de inicio de session RRRRRRRRRRR",bg="red",font=font)
        lb.place(relx=0.0, rely=0.0,relwidth=0.8, relheight=0.05)

mainloop()