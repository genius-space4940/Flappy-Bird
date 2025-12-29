# Модулі
from pygame import *
import sys
init()

from button import Button

# Кольори
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Розміри вікна
WIDTH = 800
HEIGHT = 600

# FPS
FPS = 60

# Вікно
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Flappy Bird")

# Фон
bg = image.load("images/bg.png").convert_alpha()
size_bg = (WIDTH, HEIGHT+200)
bg = transform.scale(bg, size_bg)

# Годинник
clock = time.Clock()

# Кнопки
font_btn = font.SysFont(None, 50)
btn_play = Button(WIDTH//2-100, HEIGHT//2-50, 200, 70, GRAY, font_btn, "PLAY")
btn_exit = Button(WIDTH//2-100, HEIGHT//2+50, 200, 70, GRAY, font_btn, "EXIT")

# Гра
game = True
menu = True
finish = True

while game:
    while menu:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                menu = False
                game = False

        window.blit(bg, (0, 0))

        btn_play.show(window)
        btn_exit.show(window)

        if btn_play.is_clicked(events):
            menu = False
            finish = False

        if btn_exit.is_clicked(events):
            quit()
            sys.exit()

        display.flip()
        clock.tick(FPS)

    while not finish:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                quit()
                sys.exit()

        window.blit(bg, (0, 0))

        display.flip()
        clock.tick(FPS)

    display.flip()
    clock.tick(FPS)
