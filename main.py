import pygame as pg
import random

pg.init()

W = 600
H = 600

screen = pg.display.set_mode((600, 600))

clock = pg.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pg.font.SysFont("Arial", 25)
score_font = pg.font.SysFont("Arial", 35)


def Your_score(score):
    value = score_font.render("Your Score:" + str(score), True, 'green')
    screen.blit(value, [300, 0])
    return score


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(screen, 'red', [x[0], x[1], snake_block, snake_block])


def messege(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [W / 6, H / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = W / 2
    y1 = H / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, W - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, H - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill('blue')
            score = Your_score(Length_of_snake)
            messege(f"Игра оконченаю. Вы набрали {Your_score(score)}", 'red')
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K.SPASE:
                        gameLoop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= W or x1 < 0 or y1 >= H or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        screen.fill('blue')

        pg.draw.rect(screen, 'green', [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(Length_of_snake - 1)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, W - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, H - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pg.display.update()
        clock.tick(snake_speed)

    pg.quit()
    quit()



gameLoop()