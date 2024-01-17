import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600
size = (width, height)

# Создание окна
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Growing Circle")

# Цвета
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Параметры круга
circle_radius = 10
circle_growing = False
circle_shrinking = False

clock = pygame.time.Clock()

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not circle_growing and not circle_shrinking:
                circle_growing = True

    screen.fill(blue)

    if circle_growing:
        circle_radius += 10  # Увеличение радиуса
        pygame.draw.circle(screen, yellow, pygame.mouse.get_pos(), circle_radius)
        if circle_radius >= min(width, height):
            circle_growing = False
            circle_shrinking = True
    elif circle_shrinking:
        circle_radius -= 10  # Уменьшение радиуса
        if circle_radius <= 0:
            circle_shrinking = False
            circle_radius = 10  # Сброс радиуса
        else:
            pygame.draw.circle(screen, yellow, pygame.mouse.get_pos(), circle_radius)

    pygame.display.flip()
    clock.tick(10)  # 10 кадров в секунду