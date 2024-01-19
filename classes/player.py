from pygame.locals import *
from classes.sounds import *


# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, n_player, screen, *group):
        super().__init__(*group)
        self.screen = screen
        self.images_walk = []
        self.index = 0
        self.animation_speed = 10  # Скорость анимации
        self.animation_count = 0  # Счётчик кадра
        self.n_player = n_player

        # Загрузка картинок ходьбы
        if self.n_player == 0:
            image_walk_1 = pygame.image.load('img/Tiles/Characters/tile_0000.png')
            image_walk_1 = pygame.transform.scale(image_walk_1, (50, 50))

            image_walk_2 = pygame.image.load('img/Tiles/Characters/tile_0001.png')
            image_walk_2 = pygame.transform.scale(image_walk_2, (50, 50))
            self.images_walk.append(image_walk_1)
            self.images_walk.append(image_walk_2)
        elif self.n_player == 1:
            image_walk_1 = pygame.image.load('img/Tiles/Characters/tile_0002.png')
            image_walk_1 = pygame.transform.scale(image_walk_1, (50, 50))

            image_walk_2 = pygame.image.load('img/Tiles/Characters/tile_0003.png')
            image_walk_2 = pygame.transform.scale(image_walk_2, (50, 50))
            self.images_walk.append(image_walk_1)
            self.images_walk.append(image_walk_2)
        self.image = self.images_walk[0]

        # картинка при проигрыше
        self.dead_img = pygame.image.load('img/scull.png')
        self.dead_img = pygame.transform.scale(self.dead_img, (40, 40))

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0

        self.jumped = False
        self.jumped_count = 0

    def update(self, game_session):
        if game_session.game_over == 0:
            new_x = 0
            new_y = 0
            key = pygame.key.get_pressed()
            # кнопки сохраняются в виде отдельных переменых
            k_left = None
            k_right = None
            k_up = None
            # Для каждого игрока назначаются определённые кнопки
            if self.n_player == 0:
                k_left = key[K_LEFT]
                k_right = key[K_RIGHT]
                k_up = key[K_UP]
            elif self.n_player == 1:
                k_left = key[K_a]
                k_right = key[K_d]
                k_up = key[K_w]

            # прыжки
            if k_up and self.jumped is False:
                if self.jumped_count != 2:
                    jump_sound.play()
                    self.vel_y = -15
                    self.jumped = True
                    self.jumped_count += 1
                else:
                    self.jumped = False
            if k_up is False:
                self.jumped = False

            # ходьба налево
            if k_left:
                new_x -= 5
                self.animation_count += 1
                if self.animation_count >= self.animation_speed:
                    self.animation_count = 0
                    self.index += 1
                    self.image = pygame.transform.flip(self.images_walk[self.index % len(self.images_walk)],
                                                       False, False)
            # ходьба направо
            if k_right:
                new_x += 5
                self.animation_count += 1
                if self.animation_count >= self.animation_speed:
                    self.animation_count = 0
                    self.index += 1
                    self.image = pygame.transform.flip(self.images_walk[self.index % len(self.images_walk)],
                                                       True, False)
            # свободное падение
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            new_y += self.vel_y

            # проверки столкновений (коллизия)
            for tile in game_session.world.tile_list:
                if tile[1].colliderect(self.rect.x + new_x, self.rect.y, self.width, self.height) and tile[2] is True:
                    new_x = 0

                if tile[1].colliderect(self.rect.x, self.rect.y + new_y, self.width, self.height) and tile[2] is True:
                    if self.jumped_count == 2:
                        self.jumped_count = 0

                    if self.vel_y < 0:
                        new_y = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        new_y = tile[1].top - self.rect.bottom
                        self.vel_y = 0

            # столкновение с врагами
            for enemy in game_session.enemy_group:
                if pygame.sprite.collide_mask(self, enemy):
                    game_session.game_over = -1
                    game_over_sound.play()

            # столкновение с лавой
            if pygame.sprite.spritecollide(self, game_session.lava_group, False):
                game_session.game_over = -1
                game_over_sound.play()

            # столкновение р рыбой
            for fish in game_session.fish_group:
                if pygame.sprite.collide_mask(self, fish):
                    game_session.game_over = -1
                    game_over_sound.play()

            # столкновение с ширами
            for thorn in game_session.thorns_group:
                if pygame.sprite.collide_mask(self, thorn):
                    game_session.game_over = -1
                    game_over_sound.play()

            # столкновение с монетками
            if pygame.sprite.spritecollide(self, game_session.coin_group, True):
                game_session.score += 1
                coin_sound.play()

            # столкновение с алмазом
            if pygame.sprite.spritecollide(self, game_session.diamonds_group, True):
                game_session.score += 10
                diamond_sound.play()

            # окончание игры, столкновение с флажком
            if game_session.key_bool:
                if pygame.sprite.spritecollide(self, game_session.end_game_group, False):
                    game_session.game_over = 1
            else:
                if pygame.sprite.spritecollide(self, game_session.end_game_group, False):
                    game_session.hint_bool = True
                else:
                    game_session.hint_bool = False
            # собирание ключей
            if pygame.sprite.spritecollide(self, game_session.key_group, True):
                game_session.key_score += 1
                game_session.key_count_invis += 1
                coin_sound.play()

            self.rect.x += new_x
            self.rect.y += new_y

            if self.rect.bottom > self.screen.get_height():
                self.rect.bottom = self.screen.get_height()

            # if self.rect.right > self.screen.get_width():
                # self.rect.right = self.screen.get_width

            # if self.rect.left < self.screen.get_width():
                # self.rect.left = self.screen.get_width

        # game over, показ картинки при проигрыше
        elif game_session.game_over == -1:
            self.image = self.dead_img
            if self.rect.y > 30:
                self.rect.y -= 5

        self.screen.blit(self.image, self.rect)
        # Нужен для показа коллизий
        # pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2)
