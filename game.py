import pygame
from random import randint
from classes.player import Player
from classes.world import World
from classes.coin import Coin
from classes.button import Button
from classes.fish import Fish
from classes.key import Key
from classes.thorns import Thorns
from classes.sounds import *


# функция загрузки уровня из txt уровня
def load_level_from_file(level, file_name):
    file = open(file_name, 'r', encoding='utf8')
    for line in file.readlines():
        one_piece = []
        for i in line.rstrip():
            if i.isdigit():
                one_piece.append(int(i))
            else:
                one_piece.append(i)
        level.append(one_piece)


def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# фукция для сохранения уровня в виде txt файла
def save_level_in_file(level, file_name):
    file = open(file_name, 'w', encoding='utf8')
    for row in level:
        line = ''
        for i in row:
            line += str(i)
        file.write(line + '\n')
    file.close()


# класс игры
class Game:
    def __init__(self, level_file, screen, pl_coords):
        self.world_list = []
        self.screen = screen
        load_level_from_file(self.world_list, level_file)

        # все группы спрайтов
        self.enemy_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.end_game_group = pygame.sprite.Group()
        self.non_material_objects = pygame.sprite.Group()
        self.fish_group = pygame.sprite.Group()
        self.key_group = pygame.sprite.Group()
        self.thorns_group = pygame.sprite.Group()
        self.diamonds_group = pygame.sprite.Group()

        # размер одного блока (клеточки)
        self.tile_size = 30

        # изображения
        restart_img = pygame.image.load('img/restart_btn.png')

        # создание монетки в верхнем_левом углу, по секрету вы можете её собрать ;)
        score_coin = Coin(self.tile_size // 2, self.tile_size // 2, self.tile_size)
        self.coin_group.add(score_coin)

        # кнопки
        self.restart_button = Button(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 - 100,
                                     restart_img, self.screen)

        # шрифты
        self.font_score = pygame.font.SysFont('counter', 30)
        self.font_key_score = pygame.font.SysFont('key_counter', 30)
        self.font_hint = pygame.font.SysFont('hint', 20)

        self.clock = pygame.time.Clock()
        self.fraps = 60

        self.game_over = 0
        self.score = 0
        self.key_score = 0
        self.hint_bool = False
        self.key_bool = False
        self.key_count_invis = 0

        self.players = pygame.sprite.Group()
        Player(pl_coords[0][0], pl_coords[0][1], 0, self.screen, self.players)
        Player(pl_coords[1][0], pl_coords[1][1], 1, self.screen,  self.players)
        # создание мира
        self.world = World(self.world_list, self.screen, self.tile_size, self)

    def draw(self, fish):
        self.screen.fill(pygame.Color((0, 246, 245)))
        self.clock.tick(self.fraps)
        self.world.draw()
        self.players.update(self)
        self.enemy_group.update()
        self.end_game_group.update()
        self.coin_group.update()
        self.fish_group.update()

        # добавление рыбок в мир
        if fish is True:
            Fish(randint(0, 900), self.tile_size, self.fish_group)

        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 128, 0)

        draw_text('X' + str(self.score), self.font_score, white, self.tile_size, 8, self.screen)
        if self.key_bool:
            draw_text(f'{self.key_score}/3', self.font_key_score, green, self.tile_size + 840, 490, self.screen)
        else:
            draw_text(f'{self.key_score}/3', self.font_key_score, red, self.tile_size + 840, 490, self.screen)
        if self.key_count_invis == 3:
            completed_sound.play()
            self.key_bool = True
            self.key_count_invis = 0
        if self.key_score < 3 and self.hint_bool:
            draw_text(f'Сначала собери ключи', self.font_hint, red, self.tile_size + 400, 8, self.screen)

        self.coin_group.draw(self.screen)
        self.key_group.draw(self.screen)
        self.diamonds_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.end_game_group.draw(self.screen)
        self.thorns_group.draw(self.screen)
        self.fish_group.draw(self.screen)
        self.lava_group.draw(self.screen)

        if self.game_over == -1:
            # если игрок проиграл игровой цикл заканчивается и загружается новый с этим же уровнем
            if self.restart_button.draw() and self.restart_button.clicked:
                return 'game_over'
        if self.game_over == 1:
            # если игроки прошли уровень то игровой цикл заканчивается и загружается новый уровень
            return 'next_level'
        for event in pygame.event.get():
            # если закрыли окно заканчивается вся программа
            if event.type == pygame.QUIT:
                return 'close'
