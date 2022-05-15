from tkinter import Frame
from tkinter.ttk import Combobox, Notebook
from tkinter import *
import field_class



class Tab_creator:
    def __init__(self, root, list, tabs_control, tab_index, index) -> None:
        self.root = root
        self.manschaftList_Sort = list
        self.tabs_control = tabs_control
        self.tab = Frame(self.tabs_control)
        self.tab_index = tab_index
        self.index = index

        # print('Frame')

        self.tabs_control.add(self.tab, text="Tag {0}".format(self.tab_index))
        self.tabs_control.pack(fill=BOTH, expand=1)

        self.spin_l = StringVar()
        self.spin_r = StringVar()
        self.x = ''
        self.y = ''

        # self.field_obj = field_class.Field_creator(root, self.manschaftList_Sort, self.tabs_control, self.tab_index, self.tab, self.index)


