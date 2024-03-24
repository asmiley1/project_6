from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Calculator")

ttk.Entry(root, state='disabled').pack()

ttk.Entry(root).pack()

buttons = ['1','2','3','4','5','6','7','8','9','0','+','-','/','*','=']

for btn in buttons:
    ttk.Button(root, text=btn).pack(side = LEFT)

root.mainloop()