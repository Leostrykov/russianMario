import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen = pygame.display.set_mode((800, 600))

# Установка цвета текста и фона
text_color = (255, 255, 255)
background_color = (0, 0, 0)

# Создание шрифта
font = pygame.font.Font(None, 36)

# Флаги для отображения и скрытия текста
show_text = False
show_text_time = 0

# Отображение надписи на экране
def display_text():
    text = font.render("Привет", True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (400, 300)
    screen.blit(text, text_rect)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            show_text = True
            show_text_time = pygame.time.get_ticks()  # Запоминаем время отображения текста

    if show_text:
        current_time = pygame.time.get_ticks()
        if current_time - show_text_time < 300:  # Показываем текст в течение 3 секунд
            screen.fill(background_color)  # Очищаем экран
            display_text()  # Отображаем текст
        else:
            show_text = False  # Скрываем текст после 3 секунд

    pygame.display.flip()

pygame.quit()
