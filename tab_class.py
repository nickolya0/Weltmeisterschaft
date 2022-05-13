from tkinter import Frame
from tkinter.ttk import Combobox, Notebook
from tkinter import *



class Tab_creator:
    def __init__(self, root, list, tabs_control, tab_index) -> None:
        self.root = root
        self.manschaftList_Sort = list
        self.tabs_control = tabs_control
        self.tab = Frame(self.tabs_control)
        self.tab_index = tab_index

        self.tab_erstellen()
        
    def tab_erstellen(self):
        print('tab_erstellen')
        self.tab = Frame(self.tabs_control)
        # self.tabs_control.select(self.tab)
        self.tabs_control.add(self.tab, text="Spl.{0}".format(self.tab_index))
        # self.tabs_control.add(self.tab, text="Spl")
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

   


    # def __str__(self) -> str:  # Для наглядности print'а
    #     return "I am {}\nMy param1 is {}\nParam2 is {}\nargs is ".format(
    #         self.__class__,
    #         self.root,
    #         self.list
    #         # self.args
    #     )

    # def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
    #     state = {}
    #     state["root"] = self.root
    #     state["list"] = self.list
    #     # state["args"] = self.args
    #     return state

    # def __setstate__(self, state: dict):  # Как мы будем восстанавливать класс из байтов
    #     self.root = state["root"]
    #     self.list = state["list"]
    #     # self.args = state["args"]