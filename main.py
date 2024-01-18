import pygame
import sqlite3
from random import randint
from game import Game
from classes.button import Button
from classes.sounds import completed_sound

# размер окна
screen_width = 900
screen_height = 600
# конфигурации уровней
levels = [[0, ((50, 470), (100, 470)), False], [0, ((50, 470), (100, 470)), True]]
db = sqlite3.connect('game.db')
cur = db.cursor()


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    fraps = 60

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Russian Mario')

    select_level = 0
    score = 0
    end_game = False
    start_time = None
    time_of_session = None

    start_btn = pygame.image.load('img/start_btn.png')
    start_img = pygame.image.load('img/start_btn.png')
    exit_img = pygame.image.load('img/exit_btn.png')
    logo_img = pygame.image.load('img/logo.png')
    logo_img = pygame.transform.scale(logo_img, (400, 200))

    start_img = pygame.transform.scale(start_img, (140, 60))
    exit_img = pygame.transform.scale(exit_img, (140, 60))

    start_button = Button(screen_width // 2 - 225, screen_height // 2 + 50, start_img, screen)
    exit_button = Button(screen_width // 2 + 40, screen_height // 2 + 50, exit_img, screen)
    # font = pygame.font.SysFont('counter', 70)
    font_start = pygame.font.Font('fonts\Pixeloid_font_0_4\TrueType (.ttf)/PixeloidSans.ttf', 70)
    font_dev = pygame.font.Font('fonts\Pixeloid_font_0_4\TrueType (.ttf)/PixeloidSans.ttf', 20)
    bold_font = pygame.font.Font('fonts\Pixeloid_font_0_4\TrueType (.ttf)/PixeloidSans-Bold.ttf', 30)
    # Цвета
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    main_menu = True

    run = True
    while run:
        if main_menu is True:
            # меню
            screen.fill(pygame.Color((0, 246, 245)))
            screen.blit(logo_img, (screen_width // 2 - 220, screen_height // 2 - 200))
            draw_text('by:', font_dev, white, screen_width - 180, screen_height // 2 + 180)
            draw_text('maxim antoniak', font_dev, white, screen_width - 180, screen_height // 2 + 200)
            draw_text('leo strukov', font_dev, blue, screen_width - 180, screen_height // 2 + 220)
            draw_text('egor barannikov', font_dev, red, screen_width - 180, screen_height // 2 + 240)

            if exit_button.draw():
                run = False
            if start_button.draw():
                start_time = pygame.time.get_ticks()
                main_menu = False
        else:
            if end_game is False:
                # запуск игры
                current_level = Game(f'level_{select_level}.txt', screen, levels[select_level][1])
                is_game = True
                clock = pygame.time.Clock()
                random_interval = randint(50, 100)

                while is_game:
                    fish = False
                    if random_interval > 0:
                        random_interval -= 1
                    elif random_interval == 0 and levels[select_level][2]:
                        fish = True
                        random_interval = randint(50, 100)
                    update = current_level.draw(fish)
                    if update == 'next_level':
                        if select_level < len(levels) - 1:
                            score += current_level.score
                        else:
                            time_of_session = pygame.time.get_ticks() - start_time
                            cur.execute(f'INSERT INTO score_table (time, score) VALUES ({time_of_session}, {score})')

                            end_game = True
                        select_level += 1
                        is_game = False
                    elif update == 'close':
                        is_game = False
                        run = False
                    elif update == 'game_over':
                        is_game = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            is_game = False
                            run = False
                    pygame.display.update()
            else:
                # финальное окно
                score_aft = cur.execute('SELECT MIN(time), MAX(score) FROM score_table').fetchone()

                screen.fill(pygame.Color((0, 246, 245)))

                draw_text('Нынешний счёт:', bold_font, black, screen_width // 2 - 400, screen_height // 2 - 50)
                new_reccord = False

                # лучший результат
                draw_text('Лучшие результаты:', bold_font, black, screen_width // 2 + 50, screen_height // 2 - 50)
                draw_text('Ваш счёт:' + str(score_aft[1]), font_dev, black,
                          screen_width // 2 + 50, screen_height // 2 - 20)
                draw_text('Время:' + str((score_aft[0] // 1000) // 60) + ':' + str((score_aft[0] // 1000) % 60),
                          font_dev, black, screen_width // 2 + 50, screen_height // 2 + 20)

                # нынешний результат
                if time_of_session < score_aft[0]:
                    draw_text('Время:' + str((score_aft[1])), font_dev, red,
                              screen_width // 2 - 400, screen_height // 2 + 20)
                    new_reccord = True
                else:
                    draw_text('Время:' + str((time_of_session // 1000) // 60) + ':' +
                              str((time_of_session // 1000) % 60), font_dev, black,
                                screen_width // 2 - 400, screen_height // 2 + 20)
                if score > score_aft[1]:
                    draw_text('Ваш счёт:' + str(score), font_dev, red, screen_width // 2 - 400,
                              screen_height // 2 - 20)
                    new_reccord = True
                else:
                    draw_text('Ваш счёт:' + str(score), font_dev, black, screen_width // 2 - 400,
                              screen_height // 2 - 20)
                if new_reccord:
                    draw_text('Новый рекорд', bold_font, red, screen_width // 2 - 400,
                              screen_height // 2 + 50)
                    completed_sound.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

db.commit()
pygame.quit()
