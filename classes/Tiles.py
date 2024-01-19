import pygame

# список объектов мира
tiles = {
    # ключ на карте: ['название', картинка, является ли материальной]
    1: ['ground_start', pygame.image.load('img/Tiles/tile_0001.png'), True],
    2: ['ground_center', pygame.image.load('img/Tiles/tile_0002.png'), True],
    3: ['ground_end', pygame.image.load('img/Tiles/tile_0003.png'), True],
    5: ['ground_underground', pygame.image.load('img/Tiles/tile_0006.png'), True],
    6: ['water', pygame.image.load('img/Tiles/tile_0200.png'), False],
    7: ['coin', pygame.image.load('img/Tiles/tile_0151.png'), False],
    8: ['end_game', pygame.image.load('img/Tiles/tile_0112.png'), False],
    9: ['key', pygame.image.load('img/Tiles/tile_0027.png'), False],
    'q': ['earth1', pygame.image.load('img/Tiles/tile_0004.png'), True],
    'w': ['earth2', pygame.image.load('img/Tiles/tile_0005.png'), True],
    'e': ['earth3', pygame.image.load('img/Tiles/tile_0104.png'), True],
    'r': ['sight', pygame.image.load('img/Tiles/tile_0088.png'), False],
    't': ['1block', pygame.image.load('img/Tiles/tile_0000.png'), True],
    'y': ['thorn', pygame.image.load('img/Tiles/tile_0068.png'), False],
    'u': ['diamond', pygame.image.load('img/Tiles/tile_0067.png'), False]
}

# получение списка ключей словаря tiles
tiles_name = list(tiles.keys())
