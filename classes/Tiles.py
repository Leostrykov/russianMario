import pygame

# список объектов мира
tiles = {
    1: ['ground_start', pygame.image.load('img/Tiles/tile_0001.png')],
    2: ['ground_center', pygame.image.load('img/Tiles/tile_0002.png')],
    3: ['ground_end', pygame.image.load('img/Tiles/tile_0003.png')],
    5: ['ground_underground', pygame.image.load('img/Tiles/tile_0006.png')],
    6: ['water', pygame.image.load('img/Tiles/tile_0200.png')],
    7: ['coin', pygame.image.load('img/Tiles/tile_0151.png')],
    8: ['end_game', pygame.image.load('img/Tiles/tile_0112.png')],
    9: ['key', pygame.image.load('img/Tiles/tile_0027.png')],
    'q': ['earth1', pygame.image.load('img/Tiles/tile_0004.png')],
    'w': ['earth2', pygame.image.load('img/Tiles/tile_0005.png')],
    'e': ['earth3', pygame.image.load('img/Tiles/tile_0104.png')],
    'r': ['sight', pygame.image.load('img/Tiles/tile_0088.png')],
    't': ['1block', pygame.image.load('img/Tiles/tile_0000.png')],
    'y': ['thorn', pygame.image.load('img/Tiles/tile_0068.png')],
    'u': ['diamond', pygame.image.load('img/Tiles/tile_0067.png')]
}

backgrounds = {
    1: pygame.image.load('img/Tiles/Backgrounds/tile_0000.png'),
    2: pygame.image.load('img/Tiles/Backgrounds/tile_0008.png'),
    3: pygame.image.load('img/Tiles/Backgrounds/tile_0009.png'),
    4: pygame.image.load('img/Tiles/Backgrounds/tile_0010.png')
}

backgrounds_styles = {
    'forest': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
}

# получение списка ключей словаря tiles
tiles_name = list(tiles.keys())