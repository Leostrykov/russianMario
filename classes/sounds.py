import pygame
from pygame import mixer

mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

# звуки
coin_sound = pygame.mixer.Sound('sound/coin.wav')
coin_sound.set_volume(0.5)
jump_sound = pygame.mixer.Sound('sound/jump.wav')
jump_sound.set_volume(0.5)
game_over_sound = pygame.mixer.Sound('sound/game_over.wav')
game_over_sound.set_volume(0.5)
completed_sound = pygame.mixer.Sound('sound/not_complete.wav')
completed_sound.set_volume(0.5)
diamond_sound = pygame.mixer.Sound('sound/diamond.wav')
diamond_sound.set_volume(0.5)
