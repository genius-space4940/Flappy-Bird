# Модулі
from pygame import *
from random import randint
import sys
init()

from button import Button

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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

# Бали
score = 0
record = 0

# Швидкість
speed = 5

# Текст
font_t = font.SysFont(None, 60)
title = font_t.render("FLAPPY BIRD", True, WHITE)
text_lose = font_t.render("You lost!", True, WHITE)

font_score = font.SysFont(None, 40)
text_score = font_score.render(f"Score: {score}", True, WHITE)
text_record = font_score.render(f"Record: {record}", True, WHITE)

# Кнопки
font_btn = font.SysFont(None, 50)
btn_play = Button(WIDTH//2-100, HEIGHT//2-50, 200, 70, GRAY, font_btn, "PLAY")
btn_restart = Button(WIDTH//2-100, HEIGHT//2-50, 200, 70, GRAY, font_btn, "RESTART")
btn_exit = Button(WIDTH//2-100, HEIGHT//2+50, 200, 70, GRAY, font_btn, "EXIT")

buttons = [btn_play, btn_exit, btn_restart]

# Пташка
y = HEIGHT//2-25

flappy_bird = image.load("images/flappy_bird.png").convert_alpha()
flappy_bird_size = (50, 50)
flappy_bird = transform.scale(flappy_bird, flappy_bird_size)

# Генерація труб
def generate_pipes(count, pipe_width=140, gap=280, min_height=50, max_height=440, distance=650):
    pipes = []
    start_x = WIDTH

    for i in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap, pipe_width, HEIGHT - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes
    
pipes = generate_pipes(150)

# Гра
game = True
menu = True
finish = True

while menu:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            menu = False
            game = False

    window.blit(bg, (0, 0))

    window.blit(title, (WIDTH//3, HEIGHT//6))

    hover_btn = False

    for btn in buttons:
        btn_play.show(window)
        btn_exit.show(window)

        if btn.is_hovered():
            hover_btn = True

    if btn_play.is_clicked(events):
        menu = False
        finish = False

    if btn_exit.is_clicked(events):
        quit()
        sys.exit()

    mouse.set_cursor(SYSTEM_CURSOR_HAND if hover_btn else SYSTEM_CURSOR_ARROW)

    display.flip()
    clock.tick(FPS)

while game:
    while not finish:
        events = event.get()
        keys = key.get_pressed()
        for e in events:
            if e.type == QUIT:
                quit()
                sys.exit()

        window.blit(bg, (0, 0))

        window.blit(text_score, (10, 10))
        window.blit(text_record, (WIDTH-text_record.get_width()-10, 10))

        mouse.set_cursor(SYSTEM_CURSOR_ARROW)

        bird_rect = flappy_bird.get_rect(topleft=(100, y))
        window.blit(flappy_bird, bird_rect)
        if (keys[K_DOWN] or keys[K_s]) and y <= HEIGHT-55:
            y += 5

        elif (keys[K_UP] or keys[K_w]) and y >= 5:
            y -= 5

        if len(pipes) < 8:
            pipes += generate_pipes(150)

        for pipe in pipes[:]:
            pipe.x -= speed
            draw.rect(window, 'green', pipe)
            if pipe.x < -100:
                pipes.remove(pipe)
                score += 0.5
                text_score = font_score.render(f"Score: {int(score)}", True, WHITE)
                speed += 0.02

            if bird_rect.colliderect(pipe):
                window.blit(text_lose, (WIDTH//1.65-text_lose.get_width(), HEIGHT//4-text_lose.get_height()))
                if record < score:
                    record = score
                    window.blit(text_record, (WIDTH-text_record.get_width()-10, 10))
                finish = True

        display.flip()
        clock.tick(FPS)
    
    while finish:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                quit()
                sys.exit()

        hover_btn = False

        for btn in buttons:
            btn.show(window)
            if btn.is_hovered():
                hover_btn = True

        if btn_exit.is_clicked(events):
            quit()
            sys.exit()

        if btn_restart.is_clicked(events):
            pipes = generate_pipes(150)
            y = HEIGHT//2-25
            score = 0
            speed = 5
            text_score = font_score.render(f"Score: {score}", True, WHITE)
            text_record = font_score.render(f"Record: {int(record)}", True, WHITE)
            finish = False

        mouse.set_cursor(SYSTEM_CURSOR_HAND if hover_btn else SYSTEM_CURSOR_ARROW)

        display.flip()
        clock.tick(FPS)

    display.flip()
    clock.tick(FPS)
