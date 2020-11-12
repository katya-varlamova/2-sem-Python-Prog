def multy(ax,ay,bx,by):
    return ax*by-bx*ay
def cross_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    eps = 1e-10
    v1=multy(x4-x3,y4-y3,x1-x3,y1-y3)
    v2=multy(x4-x3,y4-y3,x2-x3,y2-y3)
    v3=multy(x2-x1,y2-y1,x3-x1,y3-y1)
    v4=multy(x2-x1,y2-y1,x4-x1,y4-y1)
    return (v1*v2)<eps and (v3*v4)<eps
print(cross_lines(1, 1, 5, 5, 0, 3, 4, 0))
print()
print(cross_lines(1, 1, 5, 5, -1, 3, 0, -1))
