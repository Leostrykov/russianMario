import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../img/Tiles/tile_0151.png')
        self.image = pygame.transform.scale(img, (x, y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
