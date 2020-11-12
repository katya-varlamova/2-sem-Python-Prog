import math as math
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
import tkinter.ttk as ttk
def f(x):
    return math.sin(x)#abs(abs(abs(x)-1)-1)
def newton(x1, eps):
    x2 = x1 - f(x1)/derivative(x1)
    iterat = 0
    while abs(x2-x1)>eps:
        x1 = x2
        x2 = x2 - f(x2)/derivative(x2)
        iterat += 1
    return x2, iterat
def findX(c, d):
    i = min(c,d)
    h = (abs(d-c))/100000
    while i<=max(c, d)+h:
        if derivative2(i)*f(i) >= 0:
            return i, True
        i+=h
    return i, False
def derivative(x):
    eps = 0.000000001
    x0 = x + eps
    return (f(x) - f(x0))/(x - x0)
def derivative2(x):
    eps = 0.001
    x0 = x + eps
    return ((f(x + eps) - f(x0 + eps))/((x + eps) - \
(x0 + eps)) - (f(x) - f(x0))/(x - x0))/eps

def main(a, b, h, eps, maxiter):
    rows=[]
    root = 0
    code = 0
    while a<b:
        if f(a+h)*f(a) <= 0:
            if (f(a+h)==0):
                a+=h
                continue
            minb = min(a+h, b)
            k, bol = findX(a, minb)
            if bol and k<=b:
                root += 1
                st = time.time()
                my, myit = newton(k, eps)
                myit += 1
                mytime = time.time() - st
                try:
                    code = 0
                    st = time.time()
                    lib = optimize.newton(f, k, tol=eps, maxiter = maxiter)
                    libtime = time.time() - st
                    rows.append([str(root), '{:^9.3f}'.format(a), '{:^9.3f}'.format(minb), '{:^12.8f}'.format(lib),\
                    '{:^10.0e}'.format(f(lib)), "x",'{:^11.2e}'.format(libtime), str(code), "scipy"])
                except:
                    code = 2
                    rows.append([str(root), '{:^9.3f}'.format(a), '{:^9.3f}'.format(minb), "-",\
                    "-", "-", "-", str(code), "scipy"])
                if myit>maxiter:
                    code = 1
                    rows.append([str(root), '{:^9.3f}'.format(a), '{:^9.3f}'.format(minb), "-",\
                    "-", "-", "-", str(code), "я"])
                else:
                    code = 0
                    rows.append([str(root), '{:^9.3f}'.format(a), '{:^9.3f}'.format(minb), '{:^12.8f}'.format(my),\
                    '{:^10.0e}'.format(f(my)), "x",'{:^11.2e}'.format(mytime), str(code), "я"])
                
        a+=h
    return rows

def find():
    try:
        a = float(e1.get())
        b = float(e2.get())
        h = float(e3.get())
        eps = float(e4.get())
        maxiter = int(e5.get())
    except:
        return
    rows = main(a, b, h, eps, maxiter)
    global table
    table.delete(*table.get_children())
    for row in rows:
        table.insert('', tk.END, values=tuple(row))
    lb17.grid(row = 10, column = 0, sticky = tk.W)
    lb18.grid(row = 11, column = 0, sticky = tk.W)
    lb19.grid(row = 12, column = 0, sticky = tk.W)
    table.grid(row = 13, column = 0, sticky = tk.W)
##    scrolltable = tk.Scrollbar(window, command=table.yview)
##    table.configure(yscrollcommand=scrolltable.set)
##    scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
##    table.pack(expand=tk.YES, fill=tk.BOTH)

def draw():
    try:
        a = float(e1.get())
        b = float(e2.get())
        n = int(e6.get())
    except:
        return
    x = np.linspace(a,b,n)
    y = np.sin(x)
    plt.plot(x,y,label = 'График')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('График')
    eps = 1e-3
    ymax = max(y)
    ymin = min(y)
    ticks = []
    for i in range(n-1):
        if y[i]*y[i+1] <= 0:
            k, bol = findX(x[i], x[i+1])
            root = optimize.newton(f, k)
            plt.scatter(root, 0)
            ticks.append(root)
        if abs(y[i] - ymax) < eps:
            plt.scatter(x[i],ymax)
            ticks.append(x[i])
        elif abs(y[i] - ymin) < eps:
            plt.scatter(x[i], ymin)
            ticks.append(x[i])
    plt.xticks(ticks)
    plt.show()



window = tk.Tk()
window.title('входные данные')
window.geometry('700x400')
app = tk.Frame(window)
app.grid()
headings=("№ корня", "начало отрезка", "конец отрезка", "корень",\
               "значение функции", "итерации", "время работы", "код", "метод")
lb10 = tk.Label(app, text = 'Входные данные')
lb10.grid(row = 1, column = 1, sticky = tk.W)
lb11 = tk.Label(app, text = 'начало отрезка')
lb11.grid(row = 2, column = 0, sticky = tk.W)
lb12 = tk.Label(app, text = 'конец отрезка')
lb12.grid(row = 3, column = 0, sticky = tk.W)
lb13 = tk.Label(app, text = 'шаг')
lb13.grid(row = 4, column = 0, sticky = tk.W)
lb14 = tk.Label(app, text = 'точность')
lb14.grid(row = 5, column = 0, sticky = tk.W)
lb15 = tk.Label(app, text = 'максимальное количество итераций')
lb15.grid(row = 6, column = 0, sticky = tk.W)
lb16 = tk.Label(app, text = 'количество разбиений отрезка')
lb16.grid(row = 8, column = 0, sticky = tk.W)

e1 = tk.Entry(app)
e1.grid(row = 2, column = 1, sticky = tk.W)
e2 = tk.Entry(app)
e2.grid(row = 3, column = 1, sticky = tk.W)
e3 = tk.Entry(app)
e3.grid(row = 4, column = 1, sticky = tk.W)
e4 = tk.Entry(app)
e4.grid(row = 5, column = 1, sticky = tk.W)
e5 = tk.Entry(app)
e5.grid(row = 6, column = 1, sticky = tk.W)

but = tk.Button(app, text = 'Найти', command = find)
but.grid(row = 7, column = 1, sticky = tk.W)

e6 = tk.Entry(app)
e6.grid(row = 8, column = 1, sticky = tk.W)

but1 = tk.Button(app, text = 'График', command = draw)
but1.grid(row = 9, column = 1, sticky = tk.W)

lb17 = tk.Label(app, text = '0 - все правильно')
lb18 = tk.Label(app, text = '1 - превышено количество итераций')
lb19 = tk.Label(app, text = '2 - ошибка scipy')
table = ttk.Treeview(window, show="headings", selectmode="browse")
table["columns"]=headings
table["displaycolumns"]=headings
for head in headings:
    table.heading(head, text=head, anchor=tk.CENTER)
    table.column(head, minwidth=10,width = 80, anchor=tk.CENTER)
window.mainloop()
