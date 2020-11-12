from func import *
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
def show_error(message):
    mb.showwarning("Ошибка", message)
def check_float(st):
    for i in st:
        if i == ".":
            return 1
    return 0
def show_sort():
    try:
        a = list(map(int, e6.get().split()))
    except:
        show_error("введите числа")
        return
    a = shell(a, len(a))
    lb3["text"] = a
    
def show_table():
    m = []
    headings = [""]
    try:
        m.append(e1.get())
        m.append(e2.get())
        m.append(e3.get())
        for i in range(3):
            if check_float(m[i]):
                show_error("размеры должны быть целыми числами")
                return
            m[i] = int(m[i])
            if m[i] <= 0:
                show_error("размеры должны быть положительными числами")
                return
            headings.append(str(m[i]))
    except:
        show_error("размеры должны быть числами")
        return
    drawTable(m, headings)
def show_graph():
    try:
        f = (e4.get())
        s = (e5.get())
       
        if check_float(f) or check_float(s):
            show_error("размеры должны быть целыми числами")
            return
        f = int(f)
        s = int(s)
        if f <= 0 or s <= 0:
            show_error("размеры должны быть положительными числами")
            return
        if s - f < 9:
            show_error("начало диапазона должно быть меньше конца, \
а также диапазон должен включать в себя не менее 10 целых значений")
            return
    except:
        show_error("размеры должны быть числами")
        return
    drawGraph(f, s)
def drawTable(m, headings):
    rows = []
    p = ["sorted array"]
    for i in m:
        a = sorted_array(i)
        beg_time = time.time()
        a = shell(a, i)
        s = time.time() - beg_time
        p.append("{:^11.2e}".format(s))
    rows.append(p)
    p = ["random array"]
    for i in m:
        a = random_array(i)
        beg_time = time.time()
        a = shell(a, i)
        s = time.time() - beg_time
        p.append("{:^11.2e}".format(s))
    rows.append(p)
    p = ["reversed array"]
    for i in m:
        a = sorted_reversed_array(i)
        beg_time = time.time()
        a = shell(a, i)
        s = time.time() - beg_time
        p.append("{:^11.2e}".format(s))
    rows.append(p)
    window1 = tk.Tk()
    window1.title('table')
    window1.geometry('500x100')
    table = ttk.Treeview(window1, show="headings", selectmode="browse")
    table["columns"]=tuple(headings)
    table["displaycolumns"]=tuple(headings)
    for head in headings:
        table.heading(head, text=head, anchor=tk.CENTER)
        table.column(head, minwidth=10,width = 120, anchor=tk.CENTER)
    table.delete(*table.get_children())
    for row in rows:
        table.insert('', tk.END, values=tuple(row))
    table.grid(row = 0, column = 0, sticky = tk.W)
def drawGraph(begin, end):
    step = (end - begin + 1) // 10
    x = []
    for i in range(10):
        x.append(begin)
        begin += step
    y = []
    for i in range(10):
        a = random_array(x[i])
        beg_time = time.time()
        a = shell(a, x[i])
        s = time.time() - beg_time
        y.append(s)
    plt.plot(x,y,label = 'Graph')
    plt.grid(True)
    plt.xlabel('n - quantity of elements')
    plt.ylabel('t - shell-sort time')
    plt.title('shell sort')
    plt.xticks(x)
    plt.yticks(y)
    plt.show()

    
window = tk.Tk()
window.title('input')
window.geometry('600x220')
app = tk.Frame(window)
app.grid()

lb0 = tk.Label(app, text = 'Введите 3 размерности')
lb0.grid(row = 0, column = 0, columnspan=2, sticky = tk.W)
e1 = tk.Entry(app)
e1.grid(row = 1, column = 0, sticky = tk.W)
e2 = tk.Entry(app)
e2.grid(row = 1, column = 1, sticky = tk.W)
e3 = tk.Entry(app)
e3.grid(row = 1, column = 2, sticky = tk.W)
but_table = tk.Button(app, text = 'Показать таблицу', command = show_table)
but_table.grid(row = 2, column = 0, sticky = tk.W)

lb2 = tk.Label(app, text = 'Введите диапазон для 10 размерностей')
lb2.grid(row = 3, column = 0, columnspan=3, sticky = tk.W)
e4 = tk.Entry(app)
e4.grid(row = 4, column = 0, sticky = tk.W)
e5 = tk.Entry(app)
e5.grid(row = 4, column = 1, sticky = tk.W)
but_table = tk.Button(app, text = 'Показать график', command = show_graph)
but_table.grid(row = 5, column = 0, sticky = tk.W)
lb2 = tk.Label(app, text = 'Array: ')
lb2.grid(row = 6, column = 0, sticky = tk.W)
e6 = tk.Entry(app)
e6.grid(row = 6, column = 1, columnspan=2, sticky = tk.W)
but_demo = tk.Button(app, text = 'Показать сортировку', command = show_sort)
but_demo.grid(row = 7, column = 0, sticky = tk.W)
lb3 = tk.Label(app, text = '')
lb3.grid(row = 7, column = 1, sticky = tk.W)
window.mainloop()
