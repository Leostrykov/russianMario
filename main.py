import pygame
from pygame.locals import *
from Tiles import tiles, tiles_name


game_over = 0

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

        self.dead_img = pygame.image.load('img/ghost.png')
        self.dead_img = pygame.transform.scale(self.dead_img, (40, 40))

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

        if game_over == 0:
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

        elif game_over == -1:
            self.image = self.dead_img
            if self.rect.y > 30:
                self.rect.y -= 5


        screen.blit(self.image, self.rect)
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


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            #print('test')
            action = True
            self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)
        return action






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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2, 2, 3]
]

screen_width = 600
screen_height = 600
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
start_btn = pygame.image.load('img/start_btn.png')
restart_img = pygame.image.load('img/restart_btn.png')

restart_button = Button(screen_width // 2 - 50, screen_height // 2 - 100, restart_img)
if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    fraps = 60

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
        enemy_group.update()
        enemy_group.draw(screen)
        lava_group.draw(screen)
        player.update()

        if game_over == -1:
            if restart_button.draw():
                print('test')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()