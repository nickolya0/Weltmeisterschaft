from tkinter import *
from tkinter.ttk import Combobox


class Field_creator:
    def __init__(self, root, list, tabs_control, tab_index, tab, index) -> None:
        self.root = root
        self.manschaftList_Sort = list
        self.tabs_control = tabs_control
        self.tab_index = tab_index
        self.tab = tab
        self.field_index = index
        self.spin_l = StringVar()
        self.spin_r = StringVar()
        self.x = ''
        self.y = ''

        # self.tabs_control.add(self.tab, text="Tag {0}".format(self.tab_index))
        # self.tabs_control.pack(fill=BOTH, expand=1)

        # print('Field Loi')

        Label(self.tab, text="Manschaft").grid(row=0, column=0, padx=20)
        Label(self.tab, text="Tore").grid(row=0, column=1)
        Label(self.tab, text="Tore").grid(row=0, column=2)
        Label(self.tab, text="Manschaft").grid(row=0, column=3)

        self.field_bauen()

    def field_bauen(self):
        print('test', self.field_index)
        self.x = Combobox(self.tab, values=[str(i) for i in self.manschaftList_Sort], state="readonly")
        self.x.current(0)
        self.x.grid(row=self.field_index+1, column=0, padx=20, pady=5)
        Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True, textvariable = self.spin_l).grid(row=self.field_index+1, column=1)
        Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True, textvariable = self.spin_r).grid(row=self.field_index+1, column=2)
        self.y = Combobox(self.tab, value=[str(i) for i in self.manschaftList_Sort], state="readonly")
        self.y.current(1)
        self.y.grid(row=self.field_index+1, column=3, padx=20)



