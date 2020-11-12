from tkinter import *
from calculate import *
from tkinter import messagebox as mb
def infoAuthor():
    mb.showinfo('Разработчик',message = "Варламова Екатерина ИУ7-21Б")
def infoProgram():
    mb.showinfo('Калькулятор',message = "Производятся вычисления в 4 сс\n\n\
Доступные операции: сложение и вычитание")
    
def repeat():
    global last_number1
    p = calculate(last_number1, last_number2, last_operation)
    last_number1 = p
    input1.delete(0,  END)
    input1.insert(0, p)
        
def clear():
    global last_number1, last_number2, last_operation, operation
    input1.delete(0,  END)
    input1.insert(0, "0")
    last_operation = 1
    operation = 1
    last_number1 = 0
    last_number2 = 0
    
def erase():
    input1.delete(0,  END)
    input1.insert(0, "0")
def defineDot(a):
    a = str(a)
    for i in a:
        if i == ".":
            return True
    return False
    
    
def zero():
    t = "0"
    try:
        a = input1.get()
        if float(a) < 1e-10 and a[len(a)-1] != ".":
            t = "0"
        else:
            t = str(a + "0")
    except:
        show_error("Число не в 4 системе счисления")
        
    input1.delete(0,  END)
    input1.insert(0, t)
def one():
    t = "0"
    try:
        a = input1.get()
        if float(a) < 1e-10 and a[len(a)-1] != ".":
            t = "1"
        else:
            t = str(a + "1")
    except:
        show_error("Число не в 4 системе счисления")
    input1.delete(0,  END)
    input1.insert(0, t)

def two():
    t = "0"
    try:
        a = input1.get()
        if float(a) < 1e-10 and a[len(a)-1] != ".":
            t = "2"
        else:
            t = str(a + "2")
    except:
        show_error("Число не в 4 системе счисления")
        
    input1.delete(0,  END)
    input1.insert(0, t)

def three():
    t = "0.0"
    try:
        a = input1.get()
        if float(a) < 1e-10 and a[len(a)-1] != ".":
            t = "3"
        else:
            t = str(a + "3")
    except:
       show_error("Число не в 4 системе счисления")
        
    input1.delete(0,  END)
    input1.insert(0, t)
def dot():
    t = "0"
    try:
        a = input1.get()
        if defineDot(a):
            return
        t = input1.get() + "."
    except:
       show_error("Число не в 4 системе счисления")  
    input1.delete(0,  END)
    input1.insert(0, t)
def toIntValues(a, b):
    va = a
    vb = b
    p = 0
    sa = str(a)
    sb = str(b)
    ka = len(sa)
    kb = len(sb)
    
    if ka > kb:
        sb += "0"*(ka-kb)
    else:
        sa += "0"*(kb-ka)
    kf = False
    for i in sa:
        if kf:
            va *= 10
            vb *=10
            p += 1
        if i == ".":
            kf = True
    return int(va), int(vb), p
    
        
def equal():
    global last_number1, last_number2, turned_on, last_operation
    try:
        t = float(input1.get())
        if abs(t - last_number2) > 1e-10 and abs(last_number1 - t) > 1e-10:
            last_number2 = t
        a = last_number1
        b = last_number2
    except:
        show_error("Недостаточно чисел")
        return
    k, t, por = toIntValues(a, b)
    p = calculate(k, t, operation)
    p /= pow(10, por)
    turned_on = 0
    if p == None:
        show_error("Число не в 4 системе счисления")
        return
    last_operation = operation
    last_number1 = p
    last_number2 = b
    last_p = p
    input1.delete(0,  END)
    input1.insert(0, p)
def change():
    try:
        t = float(input1.get())
    except:
        show_error("Число не в 4 системе счисления")
        return
    if t > 0:
        t = "-" + str(t)
        input1.delete(0,  END)
        input1.insert(0, t)
    else:
        t = str(abs(t))
        input1.delete(0,  END)
        input1.insert(0, t)     
def show_error(message):
    mb.showwarning("Ошибка", message)
def check(a):
    j = str(a)
    for i in j:
        if i != "." and i > "3":
            return 0
    return 1
def plus():
    global turned_on, operation, last_number1
    operation = 1
    turned_on = 1
    try:
        t = float(input1.get())
    except:
        show_error("Число не в 4 системе счисления")
        return
    if check(t):
        last_number1 = t
        erase()
    else:
        show_error("число не в 4 сс")
    button_minus["state"] = NORMAL
    button_plus["state"] = ACTIVE

def minus():
    global turned_on, operation, last_number1
    operation = 0
    turned_on = 1
    try:
       t = float(input1.get())
    except:
        show_error("Число не в 4 системе счисления")
        return
    if check(t):
        last_number1 = t
        erase()
    else:
        show_error("Число не в 4 системе счисления")
    button_minus["state"] = ACTIVE
    button_plus["state"] = NORMAL

window = Tk()
kol_zn = 8
operation = 1
turned_on = 0
last_operation = 1
last_number1 = 0
last_number2 = 0
input1 = Entry(window, width=25, text = "0")
input1.insert(0, "0")
input1.grid(row=0,columnspan=3, pady=5)

button_clear = Button(window,width=5, text = "CE", command = clear,
                activebackground = "#105",
                background="#555",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button_clear.grid(column=0, row=1)

button_erase1 =  Button(window,width = 5, text = "C", command = erase,
                        activebackground = "#555",
                        background="#105",
                        foreground="#000",
                        padx="15",
                        pady="15",
                        font="16")
button_erase1.grid(column=1, row=1)

button_change = Button(window,width=5, text = "+/-", command = change,
                activebackground = "#105",
                background="#555",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button_change.grid(column=2, row=1)

button01 = Button(window,width=5, text = "0", command = zero,
                activebackground = "#105",
                background="#555",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button01.grid(column=0, row=2)
button11 = Button(window,width=5, text = "1", command = one,
                activebackground = "#555",
                background="#105",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button11.grid(column=1, row=2)
button_plus = Button(window,width=5, text = "+", command = plus,
                    activebackground = "#555",
                    background="#105",
                    foreground="#ccc",
                    padx="15",
                    pady="15",
                    font="16")


button_plus.grid(column=2, row=2)


button21 = Button(window,width=5, text = "2", command = two,
                activebackground = "#555",
                background="#105",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button21.grid(column=0, row=3)
button31 = Button(window,width=5, text = "3", command = three,
                activebackground = "#555",
                background="#105",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button31.grid(column=1, row=3)

button_minus = Button(window,width=5, text = "-", command = minus,
                activebackground = "#555",
                background="#105",
                foreground="#ccc",
                padx="15",
                pady="15",
                font="16")
button_minus.grid(column=2, row=3)

button_dot =  Button(window,width=5, text = ".", command = dot,
                activebackground = "#105",
                background="#555",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button_dot.grid(column=0, row=4)

button_equals = Button(window,width=5, text = "=", command = equal,
                activebackground = "#105",
                background="#555",
                foreground="#000",
                padx="15",
                pady="15",
                font="16")
button_equals.grid(column=1, row=4)

menu_bar = Menu(window)
window.configure(menu = menu_bar)
general = Menu(menu_bar)
general.add_command(label = "Повторить", command = repeat)
general.add_command(label = "Очистить", command = clear)
menu_bar.add_cascade(label = "Действия", menu = general)

information = Menu(menu_bar)
information.add_command(label = "Об авторе", command = infoAuthor)
information.add_command(label = "О программе", command = infoProgram)
menu_bar.add_cascade(label = "Информация", menu = information)

window.title("калькулятор")
window.geometry('250x300')

window.mainloop()
