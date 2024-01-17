import pygame


class Button:
    def __init__(self, x, y, image, screen):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
            self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.screen.blit(self.image, self.rect)
        return self.clicked
