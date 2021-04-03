import pygame as pg
from math import sin

pg.init()
win = pg.display.set_mode((500, 500))

pg.display.set_caption("RK Cvetkov IU7-23B")

clock = pg.time.Clock()
FPS = 60

run = True
x = 50
y = 150
a = 100
b = 100


alpha1 = 0
alpha2 = 1/2*(3.14)
alpha3 = (3.14)
alpha4 = 3/2*(3.14)
alpha5 = 2*(3.14)

reverse = True


while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    y = sin(x/10)*10 + 100

    win.fill((0, 0, 0))


    alpha1-=0.05
    alpha2-=0.05
    alpha3-=0.05
    alpha4-=0.05
    alpha5-=0.05
    pg.draw.arc(win, (255, 255 , 0), (x, y, a, b), alpha1, alpha2, 50)
    pg.draw.arc(win, (255, 0 , 0), (x, y, a, b), alpha2, alpha3, 50)
    pg.draw.arc(win, (255, 0 , 255), (x, y, a, b), alpha3, alpha4, 50)
    pg.draw.arc(win, (73, 255 , 0), (x, y, a, b), alpha4, alpha5, 50)

    if (reverse == True) and (x < 500 - 50):
        x += 1
    else:
        reverse = False

    if (reverse == False) and (x > 30):
        x -= 1
    else:
        reverse = True
    pg.display.update()
