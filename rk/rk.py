import pygame
import math

def find_center(x, y, rw, rh):
    xc = (2 * x + rw) // 2
    yc = (2 * y + rh) // 2
    return xc, yc

HEIGHT = 540
WIDTH = 400
COLOUR = (255, 0, 0)
run = True

win = pygame.display.set_mode((WIDTH, HEIGHT))

x = 100
y = 100
rh = 50
rw = 50
xc, yc = find_center(x, y, rw, rh)
kx = 1.0
ky = 1.0
step = -0.1

while run:
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    x1 = xc * (1 - kx) + kx * x
    y1 = yc * (1 - ky) + ky * y
    w1 = rw * kx
    h1 = rh * ky
    win.fill((0, 0, 0))
    #pygame.draw.rect(win, (0, 255, 0), (x, y, rw, rh))
    pygame.draw.rect(win, COLOUR, (x1, y1, w1, h1))
    if kx + step <= 0:
        step = math.fabs(step)
    elif kx + step >= 2:
        step *= (-1)
    else:
        kx += step
        ky += step

    pygame.display.update()
