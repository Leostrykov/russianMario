import pygame


# класс флажка для прохождения уровня
class NextLevel(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.steps = [pygame.image.load('img/Tiles/tile_0112.png'), pygame.image.load('img/Tiles/tile_0111.png')]
        self.image = pygame.transform.scale(self.steps[0], (tile_size, tile_size))
        self.index = 0
        self.animation_speed = 15  # Скорость анимации
        self.animation_count = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.animation_count += 1
        if self.animation_count >= self.animation_speed:
            self.index += 1
            self.image = self.steps[self.index % 2]
            self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
            self.animation_count = 0
