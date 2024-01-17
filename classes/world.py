import pygame
from classes.enemy import Enemy
from classes.Tiles import tiles
from classes.next_level import NextLevel
from classes.lava import Lava
from classes.coin import Coin


class World:
    def __init__(self, data, screen, tile_size, game_session):
        self.tile_list = []
        self.screen = screen
        for row_count, row in enumerate(data):
            for count, tile in enumerate(row):
                if tile != 0 and tile != 4 and tile != 6 and tile != 7 and tile != 8 and tile in tiles:
                    img = None
                    if tile in tiles:
                        img = pygame.transform.scale(tiles[tile][1], (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect)
                    self.tile_list.append(tile)
                # Сохранение водоёмов и врагов в отдельные классы
                if tile == 4:
                    enemy = Enemy(count * tile_size, row_count * tile_size - 10)
                    game_session.enemy_group.add(enemy)
                if tile == 6:
                    lava = Lava(count * tile_size, row_count * tile_size, tile_size)
                    game_session.lava_group.add(lava)
                if tile == 7:
                    coin = Coin(count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    game_session.coin_group.add(coin)
                if tile == 8:
                    end = NextLevel(count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2),
                                    tile_size)
                    game_session.end_game_group.add(end)

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            # Нужен для показа коллизий
            # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

