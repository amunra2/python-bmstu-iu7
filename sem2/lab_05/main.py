import pygame as pg

pg.init()
win = pg.display.set_mode((1300, 700))

pg.display.set_caption("Save Yoda Game (Tsvetkov Ivan IU7-23B) (alpha 0.2)")

# Добавление картинок
player_stand = pg.image.load("./assets/vader.png")

yoda = pg.image.load('./assets/yoda.png')

bullet = pg.image.load('./assets/bullet.png')

trooper = pg.image.load('./assets/trooper.png')

game_over = pg.image.load('./assets/game_over.jpg')

bg = pg.image.load('./assets/bg.png')

clock = pg.time.Clock()



x = 100
y = 400
width = 150
height = 300
speed = 5
pows = []
FPS = 120
flag = 0

# Уровень сложности
laser_speed = 3
difficulty = "easy"
time = 0
easy = 0
normal = FPS * 3
hard = FPS * 5
extreme = FPS * 7

# Для прыжка
isJump = False
jump_count = 10

run = True

# Анимация движения
left = False
right = False
animCount = 0

walk_right = [pg.image.load('./assets/vader1.png'), pg.image.load('./assets/vader2.png')]
walk_left = [pg.image.load('./assets/vader1_left.png'), pg.image.load('./assets/vader2_left.png')]

# Для выстрела
class laser():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.vel = speed

    def draw_laser(self, win):
        win.blit(bullet, (self.x, self.y))


def draw():
    global animCount

    win.blit(bg, (0, 0))
    win.blit(yoda, (30, 300))
    win.blit(trooper, (1040, 270))

    if animCount + 1 >= 15:
        animCount = 0 

    if left:
        win.blit(walk_left[animCount // 8], (x, y))
        animCount += 1
    elif right:
        win.blit(walk_right[animCount // 8], (x, y))
        animCount += 1
    else:
        win.blit(player_stand, (x, y))

    for i in pows:
        i.draw_laser(win)

    pg.display.update()

    if flag == 1:
        win.blit(game_over, (0, 0))
        pg.display.update()
        pg.time.wait(3000)



while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Передвижение лазера
    for i in pows:
        if i.x > 50:
            i.x -= i.vel
        else:
            pows.pop(pows.index(i))
            run = False
            flag = 1

    # Новый выстрел
    if len(pows) < 1:
        pows.append(laser(1040, 370, laser_speed))

    # Пересечение объектов
    for i in pows:
        if (i.x > x + (width - 40)) and (i.x < x + width) and (y < 350):
            pows.pop(pows.index(i))

    # Передвижение по зажатым кнопкам
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and (x > 5):
        x -= speed
        left = True
        right = False
    elif keys[pg.K_RIGHT] and (x < (700 - width - 5)):
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):
        if keys[pg.K_SPACE]:
            isJump = True
    else: # Реализация прыжка
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2 
            else:
                y -= (jump_count ** 2) / 2 
            jump_count -= 1
        else:
            isJump = False
            jump_count = 10

    time += 1

    if (time > normal) and (difficulty == "easy"):
        laser_speed = 10
        difficulty = "normal"

    if (time > hard) and (difficulty == "normal"):
        laser_speed = 20
        difficulty = "hard"

    if (time > extreme) and (difficulty == "hard"):
        laser_speed = 30
    draw()