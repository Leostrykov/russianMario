import pygame
from pygame.locals import *
from Tiles import tiles, tiles_name


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.images_walk = []
        self.index = 0
        # Загрузка картинок ходьбы
        image_walk_1 = pygame.image.load('img/Tiles/Characters/tile_0000.png')
        image_walk_1 = pygame.transform.scale(image_walk_1, (40, 40))

        image_walk_2 = pygame.image.load('img/Tiles/Characters/tile_0001.png')
        image_walk_2 = pygame.transform.scale(image_walk_2, (40, 40))
        self.images_walk.append(image_walk_1)
        self.images_walk.append(image_walk_2)
        image = self.images_walk[0]
        self.image = pygame.transform.scale(image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):

        new_x = 0
        new_y = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped is False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_UP] is False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            new_x -= 5
            self.image = pygame.transform.flip(self.images_walk[self.index], False, False)
        if key[pygame.K_RIGHT]:
            new_x += 5
            self.image = pygame.transform.flip(self.images_walk[self.index], True, False)
        self.index += 1
        if self.index >= len(self.images_walk):
            self.index = 0

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        new_y += self.vel_y

        self.rect.x += new_x
        self.rect.y += new_y

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        screen.blit(self.image, self.rect)


class World:
    def __init__(self, data):
        row_count = 0
        self.tile_list = []
        for row in data:
            count = 0
            for tile in row:
                if tile - 1 <= len(tiles_name) and tile != 0:
                    img = pygame.transform.scale(tiles[tiles_name[tile - 1]], (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect)
                    self.tile_list.append(tile)
                    count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
]

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
    run = True

    while run:
        screen.fill(pygame.Color((223, 246, 245)))
        clock.tick(fraps)
        all_sprites.draw(screen)
        all_sprites.update()
        world.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
