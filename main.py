from copyreg import pickle
from textwrap import fill
from tkinter import *
import tkinter
from tkinter.ttk import Combobox, Notebook
import os
import pickle
import dill
import os.path
import IntroWindow
import tab_class
import field_class

from pandas import value_counts

manschaftList = []
manschaftList_Sort = []
tabs_List = []
serialize_list = []  
list_obj = []
obj_tab_dict = {}
obj_field_dict = {}
list_field_to_dict = []


class Window:
    def __init__(self, root, width, height, title="MyWindow", resizable=(False,False), icon=None) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.i = 4
        self.field_index = 2
        self.tab_index = 1

        self.manschaftList = manschaftList
        self.manschaftList_Sort = manschaftList_Sort
        self.load_manschaften()
        self.tabs_List = tabs_List
        self.serialize_list = serialize_list 

        self.manschaftList = Listbox(self.root)
        self.tabs_control = Notebook(self.root)
        self.message_entry = Entry(self.root)
        self.list_obj = list_obj
        self.obj_tab_dict = obj_tab_dict
        self.obj_field_dict = obj_field_dict
        self.list_field_to_dict = list_field_to_dict

        if icon:
            self.root.iconbitmap(icon)

        self.label = Label(self.root, text="I'am Label")
        self.x = True
    
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
            
    def run(self):
        self.draw_widgets()
    
    def draw_widgets(self):
        self.draw_menu()
        Button(self.root, width=6, text="+ TAG", command=self.tab_obj_creator).pack()
        Button(self.root, width=6, text="+", command=self.field_obj_creator).pack()
        Button(self.root, width=6, text="Rechnen", command=self.tab_data_berechnen).pack()
        
    
    def tab_obj_creator(self):
        self.list_field_to_dict = []
        obj_tab = tab_class.Tab_creator(root, window.manschaftList_Sort, self.tabs_control, self.tab_index, self.field_index)
        
        self.tabs_control.select(obj_tab.tab)       #   SELECT aktualisiert Tab
        self.list_obj.append(obj_tab)

        self.field_obj_creator()

        self.obj_tab_dict[self.tab_index] = obj_tab     # versuchen Obj Tab in Dict schpeichern
        print('len.Obj', len(self.obj_tab_dict))
        print('len.Obj', self.obj_tab_dict)
        self.tab_index += 1
        self.field_index +=2

    def field_obj_creator(self):
        print('!!!!!!!!!!!!!!!!!!!!!!!! CURRENT', self.tabs_control.index(CURRENT))

        tab = self.list_obj[self.tabs_control.index(CURRENT)].tab
        field_obj = field_class.Field_creator(root, window.manschaftList_Sort, self.tabs_control, self.tab_index, tab, self.field_index)
        self.field_index +=2
        self.list_field_to_dict.append(field_obj)
        self.obj_field_dict[self.tabs_control.index(CURRENT)] = self.list_field_to_dict        # versuchen Obj Field in Dict schpeichern

        print('len.Field', len(self.obj_field_dict[self.tabs_control.index(CURRENT)]))
        print('len.Field', self.obj_field_dict)


    def tab_data_berechnen(self):
        # print('len.obj', len(self.obj_tab_dict))
        # print('len.field', len(self.obj_field_dict))
        # for key in self.obj_tab_dict:
        #     print('Tab-key', key)

        for key_i in self.obj_field_dict:
            print('field-key', key_i ) # list Obj_Fields
            print('field-key', self.obj_field_dict[key_i]) # list Obj_Fields
            for i in self.obj_field_dict[key_i]:
                print(i.x.get(), i.spin_l.get(), i.spin_r.get(), i.y.get())

    def save_manschaften(self):
        with open('manschaften.txt', 'w', encoding="utf-8") as file:            
            for i in self.manschaftList_Sort:
                file.write(str(i))
                file.write('\n')
        file.close

    def save_app(self):
        self.save_tabs()
        self.save_fields()

    def save_tabs(self):
        with open('x_tabs.txt', 'w', encoding="utf-8") as file:     
            file.write(str(len(self.obj_tab_dict)))
        file.close

    def save_fields(self):
        with open('x_fields.txt', 'w', encoding="utf-8") as file:            
            for key_i in self.obj_field_dict:
                for i in self.obj_field_dict[key_i]:
                    str1 = str(i.x.get()) + ' ' + str(i.spin_l.get()) + ' ' + str(i.spin_r.get()) + ' ' + str(i.y.get())
                    file.write(str1)
                    file.write('\n')
        file.close

        

    def load_obj(self):
        pass

    def load_manschaften(self):
        if os.path.isfile('manschaften.txt') is True:
            with open('manschaften.txt', 'r', encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
                    self.manschaftList_Sort.append(line.strip())

        file.close  

    def create_cup(self):                   # ???????????????????????????
        self.save_manschaften()
        self.restart()

    def restart(self):                      # ???????????????????????????
        self.root.destroy()
        window = Window(500, 500, "App")
        window.x = False        
        window.run()

    def delete(self):
        self.manschaftList.delete(ANCHOR)

    def add_manschaft(self):
        print(self.message_entry.get())
        if self.message_entry.get() != "":
            self.manschaftList.insert(END, self.message_entry.get())
            self.manschaftList_Sort.append(self.message_entry.get())

    def draw_menu(self):
        menu_bar = Menu(self.root)

        # menu_bar.add_command(label="File")
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Öffnen", command=self.load_obj)
        file_menu.add_command(label="Speichern", command=self.save_app)
        file_menu.add_command(label="Speichern as..")
        file_menu.add_separator() 
        file_menu.add_command(label="Exit", command=self.root.destroy) 

        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.configure(menu=menu_bar)

    def get_number(self):
        value = self.numbers.get()
        index = self.numbers.current()
        print(value, index)

if __name__ == "__main__":

    if os.path.isfile('manschaften.txt') is True:

        root = tkinter.Tk()
        window = Window(root, 500, 500, "App")
        window.run()
        root.mainloop()

    else:    
        root = tkinter.Tk()
        intro = IntroWindow.Intro(root, 500, 500, "App")
        intro.run()
        root.mainloop()

        