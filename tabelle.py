import os
from textwrap import indent
from tkinter import ttk
from tkinter import *
import tkinter

import numpy as np


class Tabelle:
    def __init__(self, root, manschaftList_Sort, load_fields_index) -> None:
        self.root = root
        self.manschaftList_Sort = manschaftList_Sort
        self.load_fields_index = load_fields_index
        self.arr = []
        self.scoreList = []
        self.spieleList = []
        self.toreList = []
        self.toreListNegativ = []
        self.toreZusamenVerbinden = []

        if len(self.load_fields_index) == 0:
            self.load_fields()
        self.index_to_np()

        self.punkteBerechnenEigene()
        self.toreZusamenFunk()

        print('---------------------------')
        print(load_fields_index)
        print(manschaftList_Sort)
        print('---------------------------')

        self.initializeTabelle(self.root)
        
        # tv = ttk.Treeview(self.root)
        # tv['columns']=('Rank', 'Name', 'Badge')
        # tv.column('#0', width=0, stretch=NO)
        # tv.column('Rank', anchor=CENTER, width=80)
        # tv.column('Name', anchor=CENTER, width=80)
        # tv.column('Badge', anchor=CENTER, width=80)

        # tv.heading('#0', text='', anchor=CENTER)
        # tv.heading('Rank', text='Id', anchor=CENTER)
        # tv.heading('Name', text='rank', anchor=CENTER)
        # tv.heading('Badge', text='Badge', anchor=CENTER)

        # tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
        # tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
        # tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
        # tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
        # tv.pack()

    def initializeTabelle(self, root):
        

        tv = ttk.Treeview(self.root)
        tv['columns']=('Manschaft', 'Score', 'Tore')
        tv.column('#0', width=0, stretch=NO)
        tv.column('Manschaft', anchor=CENTER, width=80)
        tv.column('Score', anchor=CENTER, width=80)
        tv.column('Tore', anchor=CENTER, width=80)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('Manschaft', text='Manschaft', anchor=CENTER)
        tv.heading('Score', text='Score', anchor=CENTER)
        tv.heading('Tore', text='Tore', anchor=CENTER)

        self.scoreList
        self.spieleList
        self.toreZusamenVerbinden

        nummer = 0
        for i in self.scoreList:
            st = i.split(' ')[0]
            print()
            print('1111111111111111111111111111111111')
            print(self.manschaftList_Sort[int(i.split(' ')[0])])
            tv.insert(parent='', index=nummer, iid=nummer, text='', values=(self.manschaftList_Sort[int(i.split(' ')[0])], self.scoreList[nummer].split(' ')[1], self.toreZusamenVerbinden[nummer].split(' ')[1]))
            nummer += 1
        tv.pack()

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
        x = 0
        str1 = ''
        # prufList = []
        print("rows _______________", rows)
        print("len(self.manschaftList_Sort)-1: _______________", len(self.manschaftList_Sort)-1)
        # self.manschaftList_Sort
        # while x < rows:
        while x <= len(self.manschaftList_Sort)-1:
            score = 0
            spiele = 0
            tore = 0
            toreN = 0
            for item in self.arr:
                # prufList.append(int(item[1]))
                if int(item[1]) == x:
                    if int(item[2])>int(item[3]):
                        score += 3
                    elif int(item[2])==int(item[3]):
                        score += 1
                    else:
                        score += 0  
                    spiele += 1
                    tore +=  int(item[2])           
                    toreN += int(item[3])
                               
            for item in self.arr:
                if int(item[4]) == x:
                    if int(item[3])>int(item[2]):
                        score += 3
                        spiele += 1
                    elif int(item[3])==int(item[2]):
                        if int(item[4])!=int(item[1]):
                            score += 1
                            spiele += 1
                    else:
                        score += 0
                        spiele += 1
                    print("tore--", tore)
                    print("tore2--", toreN)
                    tore += int(item[3])  
                    toreN += int(item[2])  
            if  spiele > 0:
                str1 = str(x) + ' ' + str(score)
                spl1 = str(x) + ' ' + str(spiele)
                tore1 = str(x) + ' ' + str(tore)
                tore2 = str(x) + ' ' + str(toreN)
                self.scoreList.append(str1)     # score list
                self.spieleList.append(spl1)    # spiele list
                self.toreList.append(tore1)    # tore list
                self.toreListNegativ.append(tore2)    # tore list

            x += 1
                
        print('SCORE------', self.scoreList)
        print('SPIELE------', self.spieleList)
        print('TORE------', self.toreList)
        print('TORE-Negativ------', self.toreListNegativ)

    def toreZusamenFunk(self):
        str1 = ''
        str2 = ''
        q = 0
        for i in self.toreList:
                str1 = i.split(" ")
                str2 = self.toreListNegativ[q].split(" ")
                str3 = str1[0] + ' ' + str1[1] + ':' + str2[1]
                self.toreZusamenVerbinden.append(str3)
                q+=1
        
        print("self.toreZusamenVerbinden", self.toreZusamenVerbinden)

    def sBerechnen(self):
        pass

    def uBerechnen(self):
        pass

    def nBerechnen(self):
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
