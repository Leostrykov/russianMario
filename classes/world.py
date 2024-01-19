import pygame
from classes.enemy import Enemy
from classes.Tiles import tiles
from classes.next_level import NextLevel
from classes.lava import Lava
from classes.coin import Coin
from classes.key import Key
from classes.thorns import Thorns
from classes.diamond import Diamond
from classes.fish import Fish


# класс мира
class World:
    def __init__(self, data, screen, tile_size, game_session):
        # список блоков земли и т.д.
        self.tile_list = []
        self.screen = screen
        for row_count, row in enumerate(data):
            for count, tile in enumerate(row):
                # если не имеет своего класса
                if (tile != 0 and tile != 4 and tile != 6 and tile != 7 and tile != 8 and tile != 9 and tile != 'y'
                        and tile != 'u' and tile in tiles):
                    img = None
                    if tile in tiles:
                        img = pygame.transform.scale(tiles[tile][1], (tile_size, tile_size))
                    rect = img.get_rect()
                    rect.x = count * tile_size
                    rect.y = row_count * tile_size
                    tile = (img, rect, tiles[tile][2])
                    self.tile_list.append(tile)
                # Сохранение водоёмов и врагов и т.д в отдельные классы
                if tile == 4:
                    enemy = Enemy(count * tile_size, row_count * tile_size - 10)
                    game_session.enemy_group.add(enemy)
                if tile == 6:
                    lava = Lava(count * tile_size, row_count * tile_size, tile_size)
                    game_session.lava_group.add(lava)
                if tile == 7:
                    coin = Coin(count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2),
                                tile_size)
                    game_session.coin_group.add(coin)
                if tile == 8:
                    end = NextLevel(count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2),
                                    tile_size)
                    game_session.end_game_group.add(end)
                if tile == 9:
                    key = Key(count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2),
                              tile_size)
                    game_session.key_group.add(key)
                if tile == 'y':
                    thorn = Thorns(count * tile_size, row_count * tile_size, tile_size)
                    game_session.thorns_group.add(thorn)
                if tile == 'u':
                    diamond = Diamond(count * tile_size + (tile_size // 2),
                                      row_count * tile_size + (tile_size // 2), tile_size)
                    game_session.diamonds_group.add(diamond)

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            # Нужен для показа коллизий
            # pygame.draw.rect(self.screen, (255, 255, 255), tile[1], 2)
