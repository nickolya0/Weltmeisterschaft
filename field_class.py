from tkinter import *
from tkinter.ttk import Combobox


class Field_creator:
    def __init__(self, root) -> None:
        self.root = root
        
        self.tab = Frame(self.tabs_control)
        self.tabs_control.add(self.tab, text="Tab")
        self.tabs_control.pack(fill=BOTH, expand=1)
        Label(self.tab, text="Manschaft").grid(row=0, column=0, padx=20)
        Label(self.tab, text="Tore").grid(row=0, column=1)
        Label(self.tab, text="Tore").grid(row=0, column=2)
        Label(self.tab, text="Manschaft").grid(row=0, column=3)


        x = Combobox(self.tab, values=[str(i) for i in self.manschaftList_Sort], state="readonly")
        x.current(0)
        x.grid(row=1, column=0, padx=20, pady=5)
        Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=1, column=1)
        Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=1, column=2)
        y = Combobox(self.tab, value=[str(i) for i in self.manschaftList_Sort], state="readonly")
        y.current(1)
        y.grid(row=1, column=3, padx=20)
