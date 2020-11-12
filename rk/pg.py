import pygame
import random
import math

pygame.init()
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pi = 3.141592653
WIDTH = 400
HEIGHT = 500
size = [WIDTH, HEIGHT]

screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
def find_center(points):
    xc = (points[1].rc[0] - points[0].rc[0]) / 2 + points[0].rc[0]
    yc = (points[2].rc[1] - points[1].rc[1]) / 2 + points[1].rc[1]
    return xc, yc
class Point:
    def __init__(self, x, y):
        self.c = [x, y]
        self.rc = [x, y]
    def rotate(self, xc, yc):
        self.c[0] = xc + (self.c[0] - xc) * math.cos(math.radians(beta)) + (self.c[1] - yc) * math.sin(math.radians(beta))
        self.c[1] = yc + (self.c[1] - yc) * math.cos(math.radians(beta)) - (self.c[0] - xc) * math.sin(math.radians(beta))
    def scale(self, xc, yc):
        self.c[0] = xc * (1 - kx) + kx * self.rc[0]
        self.c[1] = yc * (1 - ky) + ky * self.rc[1]
    def move(self, speedx, speedy):
        self.c[0] += speedx
        self.c[1] += speedy
        self.rc[0] += speedx
        self.rc[1] += speedy
        
class Rect():
    def __init__(self):
        self.width = 40
        self.height = 40
        self.rw = 40
        self.rh = 40
        x = random.randrange(400 - self.width)
        y = random.randrange(0, 40)
        self.points = [Point(x, y),
                       Point(x + self.width, y),
                       Point(x + self.width, y + self.height),
                       Point(x, y + self.height)]
        self.rx = x
        self.ry = y
        
        self.xc, self.yc = find_center(self.points)
        self.speedy = random.randrange(8, 15)
        self.speedx = 0#random.randrange(-3, 3)

    def update(self):
        self.xc, self.yc = find_center(self.points)
        
##        self.points[0].scale(self.xc, self.yc)
##        self.points[1].scale(self.xc, self.yc)
##        self.points[2].scale(self.xc, self.yc)
##        self.points[3].scale(self.xc, self.yc)
        
        self.points[0].rotate(self.xc, self.yc)
        self.points[1].rotate(self.xc, self.yc)
        self.points[2].rotate(self.xc, self.yc)
        self.points[3].rotate(self.xc, self.yc)

        self.points[0].move(self.speedx, self.speedy)
        self.points[1].move(self.speedx, self.speedy)
        self.points[2].move(self.speedx, self.speedy)
        self.points[3].move(self.speedx, self.speedy)
        if self.points[0].c[1] > HEIGHT - self.height or self.points[0].c[0] > WIDTH - self.width or self.points[0].c[0] < 0:
            x = random.randrange(400 - self.width)
            y = random.randrange(0, 40)
            self.points = [Point(x, y),
                           Point(x + self.width, y),
                           Point(x + self.width, y + self.height),
                           Point(x, y + self.height)]
        

rects = []
count = 1
kx = 1.0
ky = 1.0
step = -0.1
beta = 4
for i in range(count):
    rects.append(Rect())
while done == False:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    for i in range(count):
        rects[i].update()
        pygame.draw.polygon(screen, red,
                            (rects[i].points[0].c,
                             rects[i].points[1].c,
                             rects[i].points[2].c,
                             rects[i].points[3].c)
                            )
    if kx + step <= 0:
        step = math.fabs(step)
    elif kx + step >= 2:
        step *= (-1)
    else:
        kx += step
        ky += step
    pygame.display.flip()

pygame.quit()
