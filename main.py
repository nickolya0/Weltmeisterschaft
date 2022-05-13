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

from pandas import value_counts

manschaftList = []
manschaftList_Sort = []
tabs_List = []
serialize_list = []  
list_obj = []


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
        # self.manschaftList_Sort = manschaftList_Sort
        self.manschaftList_Sort = manschaftList_Sort
        self.load_manschaften()
        self.tabs_List = tabs_List
        self.serialize_list = serialize_list 

        self.manschaftList = Listbox(self.root)
        self.tabs_control = Notebook(self.root)
        self.message_entry = Entry(self.root)
        self.list_obj = list_obj

        # self.obj_tab = tab_class.Tab_creator(self, root)

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
        self.load_manschaften()
        # self.tab_creat()
        Button(self.root, width=6, text="+ TAG", command=self.tab_obj_creator).pack()
        Button(self.root, width=6, text="+", command=self.field_obj_creator).pack()
#======================

        # print('von List Obj - ', self.list_obj[0].tab_erstellen())
        # print('von List Obj - ', self.list_obj[0].tab_erstellen())

 
#======================
    
    def tab_obj_creator(self):

        obj_tab = tab_class.Tab_creator(root, window.manschaftList_Sort, self.tabs_control, self.tab_index)
        self.tabs_control.select(obj_tab.tab)       #   SELECT aktualisiert Tab
        # obj_tab.tab(0)['fdgdf']
        self.list_obj.append(obj_tab)
        print(self.tabs_control.index(END))


        self.tab_index += 1

    def field_obj_creator(self):

        tab = self.list_obj[self.tabs_control.index(CURRENT)].tab
        x = Combobox(tab, values=[str(i) for i in self.manschaftList_Sort], state="readonly")
        x.current(0)
        x.grid(row=self.field_index+1, column=0, padx=20, pady=5)
        Spinbox(tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=self.field_index+1, column=1)
        Spinbox(tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=self.field_index+1, column=2)
        y = Combobox(tab, value=[str(i) for i in self.manschaftList_Sort], state="readonly")
        y.current(1)
        y.grid(row=self.field_index+1, column=3, padx=20)
        self.field_index += 2

    # def field_obj_creator2(self):
    #     # print(self.list_obj[0].tab)
    #     self.tab = self.list_obj[0].tab
    #     a = self.tab = Frame(self.tabs_control)
    #     b = self.tabs_control.add(self.tab, text="Tab")
    #     c = self.tabs_control.pack(fill=BOTH, expand=1)
    #     Label(self.tab, text="Manschaft").grid(row=0, column=0, padx=20)
    #     Label(self.tab, text="Tore").grid(row=0, column=1)
    #     Label(self.tab, text="Tore").grid(row=0, column=2)
    #     Label(self.tab, text="Manschaft").grid(row=0, column=3)


    #     x = Combobox(self.tab, values=[str(i) for i in self.manschaftList_Sort], state="readonly")
    #     x.current(0)
    #     x.grid(row=1, column=0, padx=20, pady=5)
    #     Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=1, column=1)
    #     Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=1, column=2)
    #     y = Combobox(self.tab, value=[str(i) for i in self.manschaftList_Sort], state="readonly")
    #     y.current(1)
    #     y.grid(row=1, column=3, padx=20)

    #     # Button(self.tab, width=6, text="+ TAG", command=self.tab_creat).grid(row=0, column=4)
    #     # Button(self.tab, width=6, text="+", command=self.add_f).grid(row=1, column=4)

    def load_manschaften(self):
        if os.path.isfile('manschaften.txt') is True:
            with open('manschaften.txt', 'r', encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
                    self.manschaftList_Sort.append(line.strip())
                # self.manschaftList_Sort.append(file.readline())

        file.close

    

    def add_f(self):
        q = Combobox(self.tab, value=[str(i) for i in self.manschaftList_Sort], state="readonly")
        q.current(0)
        q.grid(row=self.i+1, column=0, padx=20, pady=5)
        Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=self.i+1, column=1)
        Spinbox(self.tab, values=([i for i in range(100)]), width=4, wrap=True).grid(row=self.i+1, column=2)
        w = Combobox(self.tab, value=[str(i) for i in self.manschaftList_Sort], state="readonly")
        w.current(1)
        w.grid(row=self.i+1, column=3, padx=20)

        self.i += 1

    def create_cup(self):
        self.save_manschaften()
        self.restart()
        # self.tab_creat()

    def restart(self):
        self.root.destroy()
        window = Window(500, 500, "App")
        window.x = False        
        window.run()

    def save_manschaften(self):
        with open('manschaften.txt', 'w', encoding="utf-8") as file:            
            for i in self.manschaftList_Sort:
                file.write(str(i))
                file.write('\n')
        file.close

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
        # file_menu.add_command(label="Speichern", command=self.serialize_test)
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
        
        
#=============================
        # print(obj_tab, end="\n========\n")  # Выведет информацию о классе
        # serialized = pickle.dumps(obj_tab)  # Сериализуем 
        # print(serialized, end="\n========\n")  # Выведет какие-то байты
        # b = pickle.loads(serialized)  # Восстанавливаем экземпляр класса из байтов
        # print(b)  # Смотрим, что восстановилось
#=============================

        window.run()
        root.mainloop()

    else:    
        root = tkinter.Tk()
        intro = IntroWindow.Intro(root, 500, 500, "App")
        intro.run()
        root.mainloop()

        