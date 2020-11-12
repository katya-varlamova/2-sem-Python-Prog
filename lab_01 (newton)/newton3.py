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
        if i == 4:
            s+= "\u2502" + "{:^"+str(m[i]-last)+".2}"
            last = m[i] + 1
            continue
        if i == 6:
            s+= "\u2502" + "{:^"+str(m[i]-last)+".5}"
            last = m[i] + 1
            continue
        s+= "\u2502" + "{:^"+str(m[i]-last)+".9}" 
        last = m[i] + 1
    s+= "\u2502" + "{:^"+str(z-last)+".9}" + "\u2502"
    return s
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


a, b = map(float, input("введите границы для поиска корня: ").split())
h, eps = map(float, input("введите шаг и точность: ").split())

#size of columns and its quantity
m = []
m.append(7)
m.append(15)
m.append(23)
m.append(39)
m.append(55)
m.append(60)
m.append(70)
m.append(75)
#last symbol of column
z = 81
maxiter = int(input("введите максимальное количество итераций: "))
print("0- все правильно, 1 - превышено количсетво итераций, 2 - ошибка scipy")
printTopOfHeader(m)

s = formForPrint()
print(s.format("№", "начало", "конец", "корень",\
               "значение", "итер", "время", "код", "метод"))
print(s.format("корня", "отрезка", "отрезка", "",\
               "функции", "ации", "работы", "",""))
printBottomOfHeader(m)

root = 0
s = formForPrint2()
y = True
code = 0
while a<=b:
    if f(a+h)*f(a) <= 0:
        if (f(a+h)==0):
            a+=h
            continue
        st = time.time()
        k, bol = findX(a, a+h)
        st1 = time.time() - st
        if bol and k<=b:
            if y:
                y = False
            else:
                printBottomOfLine(m)
            root += 1
            st = time.time()
            my, myit = newton(k, eps)
            myit += 1
            mytime = time.time() - st + st1
            try:
                code = 0
                st = time.time()
                lib = optimize.newton(f, k, tol=eps, maxiter = maxiter)
                libtime = time.time() - st + st1
                print(s.format(str(root), round(a, 9), round(a+h,9), lib,\
                f(lib), "x", round(libtime, 9), str(code), "scipy"))
            except:
                code = 2
                print(s.format(str(root), round(a, 9), round(a+h,9), "-",\
                "-", "-", "-", str(code), "scipy")) 
            if myit>maxiter:
                code = 1
                print(s.format(str(root), round(a, 9), round(a+h, 9), "-",\
                "-", "-", "-", str(code), "я"))
            else:
                code = 0
                print(s.format(str(root), round(a, 9), round(a+h, 9), my,\
                f(my), str(myit), mytime, str(code), "я"))      
            
    a+=h
printBottomOfTable(m)
