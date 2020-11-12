from calculate import *
f1 = open("out.txt", "w")
f1.write("")
f1.close()
file = open("test.txt")
for i in range(10):
    c1 = file.readline()
    c2 = file.readline()
    f1 = open("out.txt", "a")
    f1.write(str(calculate(int(c1), int(c2), 1)) + "\n")
    f1.close()
for i in range(9):
    c1 = file.readline()
    c2 = file.readline()
    f1 = open("out.txt", "a")
    f1.write(str(calculate(int(c1), int(c2), 0)) + "\n")
    f1.close()
r = open("right.txt")
o = open("out.txt")
for i in range(19):
    f = r.readline()
    s = o.readline()
    if f != s:
        print("{} строка: out: {}\nright: {}".format(i+1, s, f))
    else:
        print(i+1, "OK")
