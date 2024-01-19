import pygame


# класс монеток
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.steps = [pygame.image.load('img/Tiles/tile_0151.png'), pygame.image.load('img/Tiles/tile_0152.png')]
        self.animation_count = 0
        self.animation_speed = 10
        self.index = 0
        self.tile_size = tile_size

        img = self.steps[0]
        img = pygame.transform.scale(img, (tile_size, tile_size))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.animation_count += 1
        if self.animation_count >= self.animation_speed:
            self.index += 1
            self.image = self.steps[self.index % 2]
            self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
            self.animation_count = 0
