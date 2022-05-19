import os
from textwrap import indent
from tkinter import ttk
from tkinter import *

import numpy as np


class Tabelle:
    def __init__(self, root, manschaftList_Sort, load_fields_index) -> None:
        self.root = root
        self.manschaftList_Sort = manschaftList_Sort
        self.load_fields_index = load_fields_index
        self.arr = []
        self.scoreList = []
        if len(self.load_fields_index) == 0:
            self.load_fields()
        self.index_to_np()

        self.punkteBerechnenEigene()

        print('---------------------------')
        print(load_fields_index)
        print(manschaftList_Sort)
        print('---------------------------')
        
        tv = ttk.Treeview(self.root)
        tv['columns']=('Rank', 'Name', 'Badge')
        tv.column('#0', width=0, stretch=NO)
        tv.column('Rank', anchor=CENTER, width=80)
        tv.column('Name', anchor=CENTER, width=80)
        tv.column('Badge', anchor=CENTER, width=80)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('Rank', text='Id', anchor=CENTER)
        tv.heading('Name', text='rank', anchor=CENTER)
        tv.heading('Badge', text='Badge', anchor=CENTER)

        tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
        tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
        tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
        tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
        tv.pack()

        # nummer = 0
        # for i in list:
        #     tv.insert(parent='', index=0, iid=0, text='', values=(nummer, ))
        # nummer += 1
        # tv.pack()

    def index_to_np(self):
        index = []
        for zeile in self.load_fields_index:
            index.append(zeile.split(' '))
        self.arr = np.array(index)
        print("!!!!!!!", self.arr)

    def load_fields(self):
        if os.path.isfile('x_fields.index') is True:
            with open('x_fields.index', 'r') as file:
                for line in file:
                    print(line.strip())
                    # split_line = line.strip().split()
                    # self.index_combobox.append(split_line)
                    self.load_fields_index.append(line.strip())
            file.close 

    def spielBerechnen_toList(self):
        self.manschaftList_Sort
        self.load_fields_index

    def manschaftBerechnen(self):
        pass

    def punkteBerechnenEigene(self):    # Eigene Spiel
        rows, columns = self.arr.shape
        print("Rows = ",rows)
        print("Columns = ", columns)
        x = 0
        str1 = ''
        while x < rows:
            score = 0
            for item in self.arr:
                if int(item[1]) == x:
                    if int(item[2])>int(item[3]):
                        score += 3
                    elif int(item[2])==int(item[3]):
                        score += 1
                    else:
                        score += 0                
            for item in self.arr:
                if int(item[4]) == x:
                    if int(item[3])>int(item[2]):
                        score += 3
                        print('score-+3-', score)
                    elif int(item[3])==int(item[2]):
                        if int(item[4])!=int(item[1]):
                            score += 1
                    else:
                        score += 0
            str1 = str(x) + ' ' + str(score)
            self.scoreList.append(str1)

                
            x += 1
        print('TOTAL------', self.scoreList)
            

    def punkteBerechnenGast(self):      # Gast Spiel
        for item in self.load_fields_index:
            pass

    def spieleBerechnen(self):
        pass

    def sBerechnen(self):
        pass

    def uBerechnen(self):
        pass

    def nBerechnen(self):
        pass

    def toreBerechnen(self):
        pass


    # def tab_data_berechnen(self):
    #     for key_i in self.obj_field_dict:
    #         print('field-key', key_i ) # list Obj_Fields
    #         print('field-key', self.obj_field_dict[key_i]) # list Obj_Fields
    #         for i in self.obj_field_dict[key_i]:
    #             print(i.x.get(), i.spin_l.get(), i.spin_r.get(), i.y.get())

        # columns = ("имя", "IP-адрес")
        # treeview = ttk.Treeview (self.root, width = 18, show = "заголовки", columns = columns) # таблица
        
        # treeview.column ('name', width = 100, anchor=CENTER) # обозначает столбец, не отображаемый
        # treeview.column ('IP', width = 300, anchor=CENTER)
        
        # treeview.heading ("Name", text = "Name") # показать заголовок таблицы
        # treeview.heading ('IP', текст = 'IP')
        
        # treeview.pack(side=LEFT, fill=BOTH)
        
        # name = ['Computer1', 'Server', 'Notebook']
        # ipcode = ['10.13.71.223','10.25.61.186','10.25.11.163']
        # for i in range(min (len (name), len (ipcode))): # запись данных
        #     treeview.insert('', i, values=(name[i], ipcode[i]))
