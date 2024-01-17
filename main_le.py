import pygame
from game import Game
from classes.button import Button

screen_width = 900
screen_height = 600


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

    start_btn = pygame.image.load('img/start_btn.png')
    start_img = pygame.image.load('img/start_btn.png')
    exit_img = pygame.image.load('img/exit_btn.png')

    start_img = pygame.transform.scale(start_img, (140, 60))
    exit_img = pygame.transform.scale(exit_img, (140, 60))

    start_button = Button(screen_width // 2 - 225, screen_height // 2 - 50, start_img, screen)
    exit_button = Button(screen_width // 2 + 40, screen_height // 2 - 50, exit_img, screen)
    # font = pygame.font.SysFont('counter', 70)
    font_start = pygame.font.SysFont('start', 70)
    font_dev = pygame.font.SysFont('dev', 30)
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    main_menu = True

    run = True
    while run:
        if main_menu is True:
            screen.fill(pygame.Color((0, 246, 245)))
            draw_text('RUSSIAN MARIO', font_start, white, screen_width // 2 - 220, screen_height // 2 - 200)
            draw_text('by:', font_dev, white, screen_width - 180, screen_height // 2 + 180)
            draw_text('maxim antoniak', font_dev, white, screen_width - 180, screen_height // 2 + 200)
            draw_text('leo strukov', font_dev, blue, screen_width - 180, screen_height // 2 + 220)
            draw_text('egor barannikov', font_dev, red, screen_width - 180, screen_height // 2 + 240)

            if exit_button.draw():
                run = False
            if start_button.draw():
                main_menu = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        else:
            current_level = Game(f'level_{select_level}.txt', screen)
            print(current_level)
            is_game = True
            #key = pygame.key.get_pressed()
            #if key[pygame.K_q]:
            #    main_menu = True
            #    print('main_menu')
            while is_game:
                update = current_level.draw()
                if update == 'next_level':
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
        pygame.display.update()
    pygame.quit()