from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Login")

ttk.Label(root, text= 'Username').place(x=20, y=10)
ttk.Entry(root).place(x=100, y=10)

ttk.Label(root, text= 'Passcode').place(x=20, y=50)
ttk.Entry(root).place(x=100, y=50)

ttk.Button(root, text="Login").place(x=100, y=110)

root.mainloop()
