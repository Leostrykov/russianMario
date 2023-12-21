import pygame

# список объектов мира
tiles = {
    'ground_start': pygame.image.load('img/Tiles/tile_0001.png'),
    'ground_center': pygame.image.load('img/Tiles/tile_0002.png'),
    'ground_end': pygame.image.load('img/Tiles/tile_0003.png'),
}
# получение списка ключей словаря tiles
tiles_name = list(tiles.keys())
