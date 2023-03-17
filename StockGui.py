from doctest import master
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from turtle import onclick
import pandas as pd
import random






root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Random Stock Picker")





def onclick():

    StockPick = pd.read_csv('StockExample.csv')[['Symbol']]
    Row = len(StockPick)
    StockPickingIndex = random.randint(0,Row)
    StockSymbol = StockPick[StockPickingIndex::Row]

    newWindow = Toplevel(master)
    newWindow.title("The STOCK IS ....")
    newWindow.geometry("350x200")
    newWindow.resizable(False,False)
    Label(newWindow, text = StockSymbol, font=('Helvetica', 30, BOLD) ).pack()
    

   


button = tk.Button(root, text='Random Stock', font=('Arial', 18) , activebackground='green', command=onclick)

button.pack(padx=50, pady=100)


root.mainloop()