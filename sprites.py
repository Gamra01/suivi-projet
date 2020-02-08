import pygame as pg
from settings import *

# class joueur
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        # X * & Y * TILESIZE TO SPAWN BY TILE
        self.y = y * TILESIZE

    def get_keys(self):
    # get_keys function
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
                self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.vy = PLAYER_SPEED
        if self.x != 0 and self.y != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    # def move(self, dx=0, dy=0):
    #     # defines which square i want to move in to
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy



    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y



        # #dont go through walls , arreter le joueur a chaque obstacle
        # for wall in self.game.walls:
        #     if wall.x == self.x + dx and wall.y == self.y + dy:
        #         return True
        # return False

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

        # if pg.sprite.spritecollideany(self, self.game.walls):
        # #if the sprite self hit anything in groupe game.walls
        #     self.x -= self.vx * self.game.dt
        #     self.y -= self.vy * self.game.dt
        #     self.rect.x = (self.x, self.y)
        # self.rect.x = self.x * TILESIZE
        # self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
# class obstacle
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
