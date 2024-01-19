import pygame


# класс алмазов, в отличии от монеток они дают больше баллов, но и добраться до них сложнее
class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/Tiles/tile_0067.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)