import pygame

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

circle_radius = 0
circle_color = (0, 246, 245)

running = True
clock = pygame.time.Clock()

mouse_pos = (0, 0)
draw_circle = False

while running:
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                draw_circle = True
                circle_radius = 0

    if draw_circle:
        circle_radius += 10
        pygame.draw.circle(screen, circle_color, mouse_pos, circle_radius)


    pygame.display.flip()
    clock.tick(60)