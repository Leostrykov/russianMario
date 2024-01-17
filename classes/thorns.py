import pygame


class Thorns(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/Tiles/tile_0068.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y