import pygame


# класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images_walk = []
        im1 = pygame.image.load('img/Tiles/Characters/tile_0015.png')
        self.images_walk.append(pygame.transform.scale(im1, (40, 40)))
        im2 = pygame.image.load('img/Tiles/Characters/tile_0016.png')
        self.images_walk.append(pygame.transform.scale(im2, (40, 40)))
        self.index = 0
        self.animation_speed = 10  # Скорость анимации
        self.animation_count = 0  # Счётчик анимации

        self.image = self.images_walk[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.move_direct = 1
        self.counter = 0

    def update(self):
        self.rect.x += self.move_direct
        self.counter += 1
        self.animation_count += 1
        if self.animation_count >= self.animation_speed:
            if self.index == 1:
                self.index = 0
            else:
                self.index += 1
            self.animation_count = 0
            self.image = self.images_walk[self.index]
        if abs(self.counter) > 30:
            self.move_direct *= -1
            self.counter *= -1

