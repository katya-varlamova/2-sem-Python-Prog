def toInt(a):
    dec = 1
    p = 0
    for i in range(len(a)):
        p += dec*a[i]
        dec *= 10
    return p

def summa(a, b):
    next_ = 0
    j = 0
    for j in range(max(len(a), len(b))):
        if j == len(a):
            a.append(0)
        if j == len(b):
            j -= 1
            break
        p = (a[j] + b[j] + next_) // 4
        a[j] = (a[j] + b[j] + next_) % 4
        next_ = p
    j += 1
    while (next_ > 0):
        if j == len(a):
            a.append(0)
        p = (a[j] + next_) // 4
        a[j] = (a[j] + next_) % 4
        next_ = p
        j += 1
    return toInt(a)

def minus(a, b):
    for i in range(len(a)):
        if i == len(b):
            b.append(0)
        if a[i] - b[i] < 0:
            if a[i+1] > 0:
                a[i+1] -= 1
                a[i] = 4 + a[i] - b[i]
            else:
                j = 1
                while (a[i+j] < 0):
                    a[i+j] += 3
                    j += 1
                a[i+j] -= 1
                a[i] = 4 + a[i] - b[i]
        else:
            a[i] -= b[i]
    
    return toInt(a)
                
                
                
            
            
def calculate(c1, c2, operation):
    f = c1
    s = c2
    if f != 0:
        zf = f//abs(f)
    else:
        zf = 1
    if s != 0:
        zs = s//abs(s)
    else:
        zs = 1
    a = []
    b = []
    f = abs(f)
    s = abs(s)
    while f > 0:
        if f % 10 > 3:
            return
        a.append(f%10)
        f //= 10
        
    while s > 0:
        if s % 10 > 3:
            return
        b.append(s%10)
        s //= 10
        
    f = abs(c1)
    s = abs(c2)
    if (operation == 1 and zf*zs > 0) or (operation == 0 and zf*zs < 0):
        if zf < 0:
            return -1 * summa(a, b)
        else:
            return summa(a, b)
    else:
        if zf > 0:
            if f < s:
                return -1 * minus(b, a)
            else:
                return minus(a, b)
        else:
            if f < s:
                return minus(b, a)
            else:
                return -1 * minus(a, b)
