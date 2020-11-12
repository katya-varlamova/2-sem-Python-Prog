import math as math
import scipy.optimize as optimize
import time
def notEqual(i, m):
    r = True
    for j in m:
        if i == j:
            r = False
    return r
def printTopOfHeader(m):
    print('\u250C', end = "")
    for i in range(0, z):
        if notEqual(i, m):
            print('\u2500', end = "")
        else:
            print('\u252C', end = "")           
    print('\u2510')
def printBottomOfHeader(m):
    print('\u251C', end ="")
    for i in range(0, z):
        if notEqual(i, m):
           print('\u2500', end = "")
        else:
            print('\u253C', end = "")
    print('\u2524', end="")
    print()
def printBottomOfLine(m):
    print('\u251C', end ="")
    for i in range(0, z):
        if notEqual(i, m):
            print('\u2500', end = "")
        else:
            print('\u253C', end = "")
    print('\u2524', end="")
    print()
def printBottomOfTable(m):
    print('\u2514', end = "")
    for i in range(0, z):
        if notEqual(i, m):
           print('\u2500', end = "")
        else:
            print('\u2534', end = "")
    print('\u2518', end = "")
    print()
def formForPrint():
    s = ""
    last = 0
    for i in range(len(m)):
        s+= "\u2502" + "{:^"+str(m[i]-last)+"}" 
        last = m[i] + 1
    s+= "\u2502" + "{:^"+str(z-last)+"}" + "\u2502"
    return s
def formForPrint2():
    s = ""
    last = 0
    for i in range(len(m)):
        s+= "\u2502" + "{:^"+str(m[i]-last)+".9}" 
        last = m[i] + 1
    s+= "\u2502" + "{:^"+str(z-last)+".9}" + "\u2502"
    return s
def f(x):
    return math.sin(x)
def newton(x1):
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
    iterat = 0
    while i<max(c, d)+h:
        iterat += 1
        if derivative2(i)*f(i) > 0:
            return i, True, iterat
        i+=h
    return i, False, iterat
def derivative(x):
    eps = 0.000000001
    x0 = x + eps
    return (f(x) - f(x0))/(x - x0)
def derivative2(x):
    eps = 0.001
    x0 = x + eps
    return ((f(x + eps) - f(x0 + eps))/((x + eps) - \
(x0 + eps)) - (f(x) - f(x0))/(x - x0))/eps
a, b, h, eps = map(float, input().split())

#size of columns and its quantity
m = []
m.append(9)
m.append(21)
m.append(35)
m.append(53)
m.append(69)
m.append(79)
#last symbol of column
z = 95

printTopOfHeader(m)

s = formForPrint()
print(s.format("№ корня", "начало", "конец", "корень",\
               "значение", "число", "время"))
print(s.format("", "отрезка", "отрезка", "",\
               "функции", "итераций", "работы"))
printBottomOfHeader(m)
root = 0
s = formForPrint2()
y = True
while a<b:
    if f(a+h)*f(a) < 0:
        k, bol, myiter = findX(a, a+h)
        if bol and k<=b:
            if y:
                y = False
            else:
                printBottomOfLine(m)
            root += 1   
            st = time.time()
            my, myit = newton(k)
            myiter += myit
            mytime = time.time() - st

            st = time.time()
            lib = optimize.newton(f, k)
            libtime = time.time() - st
            
            print(s.format(str(root), round(a, 9), round(a+h,9), lib,\
               f(lib), "x", round(libtime, 9)))
            print(s.format(str(root), round(a, 9), round(a+h, 9), my,\
               f(my), str(myiter), mytime))
    a+=h
printBottomOfTable(m)
