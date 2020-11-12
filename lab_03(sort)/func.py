from random import *
def sorted_array(n):
    a = []
    step = randint(1, n)
    begin = randint(n*-2, n)
    for i in range(begin, begin + n*step, step):
        a.append(i)
    return a

def random_array(n):
    a =[]
    for i in range(n):
        a.append(randint(-1000, 1000))
    return a

def sorted_reversed_array(n):
    a = []
    step = randint(1, n)
    step *= -1
    begin = randint(n*-1, 2*n)
    for i in range(begin, begin + n*step, step):
        a.append(i)
    return a
def shell(a, n):
    k = 2
    while k <= n:
        k<<=1
    k>>=1
    k -= 1
    while k>0:
        for i in range(n):
            j = i
            while j-k>=0 and a[j-k]>a[j]:
                a[j], a[j-k] = a[j-k], a[j]
                j -= k
        k //= 2
    return a
#print(sorted_array(10))
#print(randomized_array(10))
#print(sorted_reversed_array(10))

