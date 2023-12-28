import pygame

# список объектов мира
tiles = {
    'ground_start': pygame.image.load('img/Tiles/tile_0001.png'), #1
    'ground_center': pygame.image.load('img/Tiles/tile_0002.png'), #2
    'ground_end': pygame.image.load('img/Tiles/tile_0003.png'),   #3
    'pass': (''), #4-блок для врага
    'ground_underground': pygame.image.load('img/Tiles/tile_0006.png'), #5
    #'water': pygame.image.load('img/Tiles/tile_0053.png'), #6
}
# получение списка ключей словаря tiles
tiles_name = list(tiles.keys())