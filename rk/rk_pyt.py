import pygame
import random
import math

pygame.init()
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

WIDTH = 400
HEIGHT = 500
size = [WIDTH, HEIGHT]

screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

s = 0.5       
def update(rect):
    rect.x = int(alpha)
    rect.y = int(50 - 50*math.sin(math.radians(alpha)))
    if rect.x + 100 >= WIDTH or rect.x < 0:
        return True
    


#fi = math.radians(30)
alpha = 0
fi = math.radians(float(input("Введите угол в градусах: ")))
zn = 1
if fi < 0:
    zn = -1
rect = pygame.Rect(0,0,100, 100)
dfi = 0
while done == False:
    clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    alpha += s
    if update(rect):
        s *= -1
    if dfi < abs(fi):
        dfi += 1e-2
    pygame.draw.arc(screen, red, rect, 0 - zn * dfi, math.pi/2 - zn * dfi, 50)
    pygame.draw.arc(screen, green, rect, math.pi/2 - zn * dfi, math.pi - zn * dfi,50)
    pygame.draw.arc(screen, blue, rect, math.pi - zn * dfi, 3*math.pi/2 - zn * dfi, 50)
    pygame.draw.arc(screen, black, rect, 3*math.pi/2 - zn * dfi, 2*math.pi - zn * dfi, 50)
    pygame.display.flip()

pygame.quit()
