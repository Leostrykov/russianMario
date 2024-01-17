import pygame

# список объектов мира
tiles = {
    1: ['ground_start', pygame.image.load('../img/Tiles/tile_0001.png')],
    2: ['ground_center', pygame.image.load('../img/Tiles/tile_0002.png')],
    3: ['ground_end', pygame.image.load('../img/Tiles/tile_0003.png')],
    5: ['ground_underground', pygame.image.load('../img/Tiles/tile_0006.png')],
    6: ['water', pygame.image.load('../img/Tiles/tile_0053.png')],
    7: ['coin', pygame.image.load('../img/Tiles/tile_0151.png')],
    8: ['end_game', pygame.image.load('../img/Tiles/tile_0112.png')]
}

backgrounds = {
    1: pygame.image.load('../img/Tiles/Backgrounds/tile_0000.png'),
    2: pygame.image.load('../img/Tiles/Backgrounds/tile_0008.png'),
    3: pygame.image.load('../img/Tiles/Backgrounds/tile_0009.png'),
    4: pygame.image.load('../img/Tiles/Backgrounds/tile_0010.png')
}

backgrounds_styles = {
    'forest': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
}

# получение списка ключей словаря tiles
tiles_name = list(tiles.keys())