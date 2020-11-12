from func import *
f1 = open("out.txt", "w")
f1.write("")
f1.close()
file = open("test.txt")
for i in range(9):
    c = list(map(int, file.readline().split()))
    f1 = open("out.txt", "a")
    s = ""
    c = shell(c, len(c))
    for j in c:
        s += str(j) + " "
    f1.write(s + "\n")
    f1.close()
r = open("right.txt")
o = open("out.txt")
for i in range(9):
    f = r.readline()
    s = o.readline()
    if f != s:
        print("{} строка: out: {}\nright: {}".format(i+1, s, f))
    else:
        print(i+1, "OK")
