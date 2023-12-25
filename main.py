import pygame
from pygame.locals import *
from Tiles import tiles, tiles_name


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.images_walk = []
        self.index = 0
        self.animation_speed = 10  # Скорость анимации
        self.animation_count = 0  # Счётчик анимации

        # Загрузка картинок ходьбы
        image_walk_1 = pygame.image.load('img/Tiles/Characters/tile_0000.png')
        image_walk_1 = pygame.transform.scale(image_walk_1, (60, 60))

        image_walk_2 = pygame.image.load('img/Tiles/Characters/tile_0001.png')
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
        new_x = 0
        new_y = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped is False:
            if self.jumped_count != 2:
                self.vel_y = -15
                self.jumped = True
                self.jumped_count += 1
            else:
                self.jumped = False
        if key[pygame.K_UP] is False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            new_x -= 5
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.index += 1
                self.image = pygame.transform.flip(self.images_walk[self.index % len(self.images_walk)], False, False)
        if key[pygame.K_RIGHT]:
            new_x += 5
            self.animation_count += 1
            if self.animation_count >= self.animation_speed:
                self.animation_count = 0
                self.index += 1
                self.image = pygame.transform.flip(self.images_walk[self.index % len(self.images_walk)], True, False)

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        new_y += self.vel_y

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

        self.rect.x += new_x
        self.rect.y += new_y

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


class World:
    def __init__(self, data):
        row_count = 0
        self.tile_list = []
        for row_count, row in enumerate(data):
            col_count = 0
            for count, tile in enumerate(row):
                if tile - 1 <= len(tiles_name) and tile != 0 and tile != 4:
                    img = pygame.transform.scale(tiles[tiles_name[tile - 1]], (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    enemy = Enemy(400, row_count * tile_size)
                    enemy_group.add(enemy)
            col_count += 1
        row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Tiles/Characters/tile_0015.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


world = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2, 2, 3]
]

enemy_group = pygame.sprite.Group()


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
    all_sprites = pygame.sprite.Group()
    player = Player(100, screen_height - 130, all_sprites)
    world = World(world)

    # enemy_group = pygame.sprite.Group()
    run = True

    while run:
        screen.fill(pygame.Color((0, 246, 245)))
        clock.tick(fraps)
        all_sprites.draw(screen)
        all_sprites.update()
        world.draw()

        enemy_group.draw(screen)

        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
