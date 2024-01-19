import pygame


# класс рыбок
class Fish(pygame.sprite.Sprite):
    def __init__(self, x, tile_size, *group):
        super().__init__(*group)
        self.group = group
        self.steps = [pygame.image.load('img/Tiles/Characters/tile_0013.png'),
                      pygame.image.load('img/Tiles/Characters/tile_0014.png')]
        self.animation_count = 0
        self.animation_speed = 10
        self.index = 0
        self.tile_size = tile_size

        img = self.steps[0]
        img = pygame.transform.scale(img, (tile_size, tile_size))
        self.image = img
        self.mask = pygame.mask.from_surface(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, 635)

    def update(self):
        self.animation_count += 1
        if self.animation_count >= self.animation_speed:
            self.index += 1
            self.image = self.steps[self.index % 2]
            self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
            self.animation_count = 0
        if self.rect.y > -5:
            self.rect.y -= 5
        else:
            # если рыбки улутели за верхний край экрана, то они исчезают
            self.kill()
