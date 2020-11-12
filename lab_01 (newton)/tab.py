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


#size of columns and its quantity
m = []
m.append(9)
m.append(16)
m.append(31)
m.append(45)

#last symbol of column
z = 50


printTopOfHeader(m)

s = formForPrint()
print(s.format("1", "2", "3", "4", "5"))
printBottomOfHeader(m)


for i in range(10):
    print(s.format("1", "2", "3", "4", "5"))
    if i!=9:
        printBottomOfLine(m)

printBottomOfTable(m)
