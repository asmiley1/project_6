from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Sign Up")

ttk.Label(root, text= 'Name').grid(row=0, column=0)
ttk.Entry(root).grid(row=0, column=1)

ttk.Label(root, text= 'Email').grid(row=1, column=0)
ttk.Entry(root).grid(row=1, column=1)

ttk.Label(root, text= 'Password').grid(row=2, column=0)
ttk.Entry(root).grid(row=2, column=1)

ttk.Button(root, text="Sign Up Now").grid(row=3, column=1)

root.mainloop()
