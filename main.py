import pygame
from pygame.locals import *
from Tiles import tiles, tiles_name


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, n_player, *group):
        super().__init__(*group)
        self.images_walk = []
        self.index = 0
        self.animation_speed = 10  # Скорость анимации
        self.animation_count = 0  # Счётчик анимации
        self.n_player = n_player

        # Загрузка картинок ходьбы
        if self.n_player == 0:
            image_walk_1 = pygame.image.load('img/Tiles/Characters/tile_0000.png')
            image_walk_1 = pygame.transform.scale(image_walk_1, (60, 60))

            image_walk_2 = pygame.image.load('img/Tiles/Characters/tile_0001.png')
            image_walk_2 = pygame.transform.scale(image_walk_2, (60, 60))
            self.images_walk.append(image_walk_1)
            self.images_walk.append(image_walk_2)
        elif self.n_player == 1:
            image_walk_1 = pygame.image.load('img/Tiles/Characters/tile_0002.png')
            image_walk_1 = pygame.transform.scale(image_walk_1, (60, 60))

            image_walk_2 = pygame.image.load('img/Tiles/Characters/tile_0003.png')
            image_walk_2 = pygame.transform.scale(image_walk_2, (60, 60))
            self.images_walk.append(image_walk_1)
            self.images_walk.append(image_walk_2)
        self.image = self.images_walk[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0

        self.jumped = False
        self.jumped_count = 0

    def update(self):
        global game_over

        new_x = 0
        new_y = 0

        key = pygame.key.get_pressed()
        # кнопки сохраняются в виде отдельных переменых
        k_left = None
        k_right = None
        k_up = None
        # Для каждого игрока назначаются определённые кнопки
        if self.n_player == 0:
            k_left = key[K_LEFT]
            k_right = key[K_RIGHT]
            k_up = key[K_UP]
        elif self.n_player == 1:
            k_left = key[K_a]
            k_right = key[K_d]
            k_up = key[K_w]

        if k_up and self.jumped is False:
            if self.jumped_count != 2:
                self.vel_y = -15
                self.jumped = True
                self.jumped_count += 1
            else:
                self.jumped = False
        if k_up is False:
            self.jumped = False
        if k_left:
            new_x -= 5
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.index += 1
                self.image = pygame.transform.flip(self.images_walk[self.index % len(self.images_walk)], False, False)
        if k_right:
            new_x += 5
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.index += 1
                self.image = pygame.transform.flip(self.images_walk[self.index % len(self.images_walk)], True, False)

        if self.index >= len(self.images_walk):
            self.index = 0

        # Свободное падение
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        new_y += self.vel_y

        # проверки столкновений (коллизия)
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + new_x, self.rect.y, self.width, self.height):
                new_x = 0

            if tile[1].colliderect(self.rect.x, self.rect.y + new_y, self.width, self.height):
                if self.jumped_count == 2:
                    self.jumped_count = 0

                if self.vel_y < 0:
                    new_y = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    new_y = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        # столкновение с врагами и водоёмом, вследствии игрок проигрывает
        if pygame.sprite.spritecollide(self, enemy_group, False):
            game_over = -1
            print('enemy')
        if pygame.sprite.spritecollide(self, lava_group, False):
            game_over = -1
            print('lava')

        self.rect.x += new_x
        self.rect.y += new_y

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        screen.blit(self.image, self.rect)
        # Нужен для показа коллизий
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


class World:
    def __init__(self, data):
        row_count = 0
        self.tile_list = []
        for row_count, row in enumerate(data):
            col_count = 0
            for count, tile in enumerate(row):
                if tile - 1 <= len(tiles_name) and tile != 0 and tile != 4 and tile != 6:
                    img = pygame.transform.scale(tiles[tiles_name[tile - 1]], (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect)
                    self.tile_list.append(tile)
                # Сохранение водоёмов и врагов в отдельные классы
                if tile == 4:
                    enemy = Enemy(count * tile_size, row_count * tile_size - 10)
                    enemy_group.add(enemy)
                if tile == 6:
                    lava = Lava(count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
            col_count += 1
        row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # Нужен для показа коллизий
            # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Tiles/Characters/tile_0015.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direct = 1
        self.counter = 0

    def update(self):
        self.rect.x += self.move_direct
        self.counter += 1
        if abs(self.counter) > 30:
            self.move_direct *= -1
            self.counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/Tiles/tile_0053.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# фукция для сохранения уровня в виде txt файла
def save_level_in_file(level, file_name):
    file = open(file_name, 'w', encoding='utf8')
    for row in level:
        line = ''
        for i in row:
            line += str(i)
        file.write(line + '\n')
    file.close()


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


world = []

load_level_from_file(world, 'level_0.txt')
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    fraps = 60

    screen_width = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Russian Mario')

    # размер одного блока (клеточки)
    tile_size = 30
    game_over = 1
    all_sprites = pygame.sprite.Group()
    player_1 = Player(100, screen_height - 130, 0, all_sprites)
    player_2 = Player(300, screen_height - 130, 1, all_sprites)
    world = World(world)

    # enemy_group = pygame.sprite.Group()
    run = True

    while run:
        clock.tick(fraps)
        if game_over == 1:
            screen.fill(pygame.Color((0, 246, 245)))
            all_sprites.draw(screen)
            all_sprites.update()
            world.draw()

            enemy_group.update()
            enemy_group.draw(screen)
            lava_group.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
