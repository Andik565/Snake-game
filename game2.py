import pygame as p
import random

import pygame.font

p.init()

GAME_WIDTH, GAME_HEIGHT = 600, 600

screen = p.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
p.display.set_caption("Snake game")
fps = p.time.Clock()
font = pygame.font.Font(None, 36)

def start(message, color):
    mess = font.render(message, True, color)
    x = GAME_WIDTH // 2 - mess.get_width() // 2
    y = GAME_HEIGHT // 2 - mess.get_height() // 2
    screen.blit(mess, (x, y))

def food():
    x = random.randint(0, GAME_WIDTH - 20)
    y = random.randint(0, GAME_HEIGHT - 20)

    while x % 20 != 0:
        x += 1
    while y % 20 != 0:
        y += 1
    return x, y

def game():
    x = GAME_WIDTH // 2
    y = GAME_HEIGHT // 2
    x_step, y_step = 0, 0
    x_food, y_food = food()
    plrs = []
    plr_len = 1

    game_over = False
    game_menu = True
    while not game_over:
        while game_menu:
            for event in p.event.get():
                if event.type == p.QUIT:
                    game_over = True
                    game_menu = False
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_SPACE:
                        game_menu = False

            screen.fill((244, 90, 60))
            start('Press Spase to start', (255, 255, 255))
            pygame.display.update()
        for event in p.event.get():
            if event.type == p.QUIT:
                game_over = True
            elif event.type == p.KEYDOWN:
                if event.key == p.K_w:
                    y_step = -20
                    x_step = 0
                elif event.key == p.K_s:
                    y_step = 20
                    x_step = 0
                elif event.key == p.K_a:
                    y_step = 0
                    x_step = -20
                elif event.key == p.K_d:
                    y_step = 0
                    x_step = 20



        x += x_step
        y += y_step

        if x < 0:
            game_over = True
        elif x - 20 > GAME_WIDTH:
            game_over = True
        elif y + 20 > GAME_HEIGHT:
            game_over = True
        elif y < 0:
            game_over = True

        if x == x_food and y == y_food:
            x_food, y_food = food()
            plr_len += 1

        plr_head = [x, y]

        plrs.append(plr_head)
        if len(plrs) > plr_len:
            del plrs[0]

        for item in plrs[:-1]:
            if item == plr_head:
                game_over = True

        screen.fill((255, 187, 0))

        p.draw.ellipse(screen, (235, 0, 20), p.Rect(x_food, y_food, 20, 20))
        for n in plrs:
            p.draw.rect(screen, (135, 254, 0), p.Rect(n[0], n[1], 20, 20))
        p.display.update()
        fps.tick(10)



game()
p.quit()
