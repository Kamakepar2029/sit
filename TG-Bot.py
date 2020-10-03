from flask import Flask, render_template
from tkinter import *
root = Tk()
root.title('Site Start')


def Starty(event):
    print('Site started...')

def Stopy(event):
    print("Site stopped...")

btns = Button(root,
             text="Start site",
             width=30,height=5,
             bg="white", fg="black")
btns.bind("<Button-1>",Starty)
btns.pack()

btn = Button(root,
             text="Stop site",
             width=30,height=5,
             bg="white", fg="black")
btn.bind("<Button-2>",Stopy)
btn.pack()
root.mainloop()
