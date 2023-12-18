import pygame
from pygame.locals import *

pygame.init()


clock = pygame.time.Clock()
fraps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Russian Mario')

tile_size = 50


background = pygame.image.load('img/sky.png')


class Player():
    def __init__(self, x, y):
        self.images_walk = []
        self.index = 0
        self.counter = 0
        image_walk_1 = pygame.image.load('extra/Alien sprites/alienPink_walk1.png')
        image_walk_2 = pygame.image.load('extra/Alien sprites/alienPink_walk2.png')
        self.image_walk_1 = pygame.transform.scale(image_walk_1, (40, 80))
        self.image_walk_2 = pygame.transform.scale(image_walk_2, (40, 80))
        self.images_walk.append(self.image_walk_1)
        self.images_walk.append(self.image_walk_2)
        image = pygame.image.load('extra/Alien sprites/alienPink_stand.png')
        self.image = pygame.transform.scale(image, (40, 80))

        self.image_all = self.images_walk[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):

        new_x = 0
        new_y = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_UP] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            new_x -= 5
        if key[pygame.K_RIGHT]:
            new_x += 5


        self.index += 1
        if self.index >= len(self.images_walk):
            self.index = 0
        self.image_all = self.images_walk[self.index]


        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        new_y += self.vel_y

        self.rect.x += new_x
        self.rect.y += new_y

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            new_y = 0

        screen.blit(self.image, self.rect)


class World():
    def __init__(self, data):
        self.tile_list = []

        snow = pygame.image.load('ice/Tiles/tundraMid.png')
        candy = pygame.image.load('candy/Tiles/cake.png')
        snow_center = pygame.image.load('ice/Tiles/tundraCenter.png')

        row_count = 0
        for row in data:
            count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(snow_center, (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(candy, (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(snow, (tile_size, tile_size))
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
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]
]


player = Player(100, screen_height - 130)
world = World(world)

run = True
while run:

    clock.tick(fraps)

    screen.blit(background, (0, 0))

    world.draw()
    player.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()