from copyreg import pickle
from textwrap import fill
from tkinter import *
import tkinter
from tkinter.ttk import Combobox, Notebook
import os
import pickle
import dill
import os.path
import main

from pandas import value_counts

manschaftList = []
manschaftList_Sort = []
tabs_List = []
serialize_list = []  

class Intro:
    def __init__(self, root, width, height, title="MyWindow", resizable=(False,False), icon=None) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.i = 4
        self.manschaftList = manschaftList
        self.manschaftList_Sort = manschaftList_Sort
        self.tabs_List = tabs_List
        self.serialize_list = serialize_list                  # fur serialized Objected

        self.manschaftList = Listbox(self.root)
        self.tabs_control = Notebook(self.root)
        self.message_entry = Entry(self.root)

        if icon:
            self.root.iconbitmap(icon)

        self.label = Label(self.root, text="I'am Label")
        self.x = True

    def run(self):       

        self.add_test_manschaften()     
        Label(self.root, width=20).grid(row=0, column=1)
        Label(self.root, width=20).grid(row=1, column=2)
        Label(self.root, width=20).grid(row=2, column=3)

        Button(self.root, width=10, text="START", command=self.KlassMain).grid(row=3, column=1)

        self.manschaftList.grid(row=0, column=2)
        self.message_entry.grid(row=2, column=2)    # Field
        
        ls = self.manschaftList.get(0, self.manschaftList.size())
        for i in ls: self.manschaftList_Sort.append(i)

        Label(self.root, width=20).grid(row=3, column=2)
        Button(self.root, width=10, text="Add", command=self.add_manschaft).grid(row=4, column=2)
        Label(self.root, width=20).grid(row=5, column=2)
        Button(self.root, width=10, text="DEL", command=self.delete).grid(row=6, column=2)  

        # self.root.mainloop()

    def add_test_manschaften(self):
        self.manschaftList.insert(END, "FC Bayern München")  
        self.manschaftList.insert(END, "Borussia Dortmund")
        self.manschaftList.insert(END, "Bayer 04 Leverkusen")
        self.manschaftList.insert(END, "RB Leipzig")
        self.manschaftList.insert(END, "SC Freiburg")
        self.manschaftList.insert(END, "FC Union Berlin")
        self.manschaftList.insert(END, "TSG Hoffenheim")
        self.manschaftList.insert(END, "Eintracht Frankfurt")
        self.manschaftList.insert(END, "FSV Mainz 05")   

    def add_manschaft(self):
        print(self.message_entry.get())
        if self.message_entry.get() != "":
            self.manschaftList.insert(END, self.message_entry.get())
            self.manschaftList_Sort.append(self.message_entry.get())

    def delete(self):
        self.manschaftList.delete(ANCHOR)

    def save_manschaften(self):
        with open('manschaften.txt', 'w', encoding="utf-8") as file:            
            for i in self.manschaftList_Sort:
                file.write(str(i))
                file.write('\n')
        file.close

    def KlassMain(self):
        self.save_manschaften()
        self.root.destroy()

        root = tkinter.Tk()
        window = main.Window(root, 500, 500, "App")
        window.run()

# ======================================================