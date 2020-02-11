import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)
GREY = (155, 181, 196)

#pygame settings

WIDTH = 1024
HEIGHT = 768
FPS = 60

TITLE = "Project "
BGCOLOR = GREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


WALL_IMG = 'towerSquare_sampleD.png'

# joueur settings
PLAYER_SPEED = 500
PLAYER_ROT_SPEED = 250
#rotation speed du joueur
PLAYER_IMG = 'spaceAstronauts.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

#Mobs settings
MOB_IMG = 'spaceAstronauts_005.png'
MOB_SPEED = 250
