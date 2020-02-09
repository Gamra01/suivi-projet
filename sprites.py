import pygame as pg
from settings import *
vec = pg.math.Vector2

# class joueur
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
        # self.vx, self.vy = 0, 0
        # self.x = x * TILESIZE
        # # X * & Y * TILESIZE TO SPAWN BY TILE
        # self.y = y * TILESIZE

    def get_keys(self):
    # get_keys function
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
        # if self.vel.x != 0 and self.vel.y != 0:
        #     self.vel *= 0.7071

    # def move(self, dx=0, dy=0):
    #     # defines which square i want to move in to
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy



    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y



        # #dont go through walls , arreter le joueur a chaque obstacle
        # for wall in self.game.walls:
        #     if wall.x == self.x + dx and wall.y == self.y + dy:
        #         return True
        # return False

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        # rotation 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        # image roatation
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
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
