import pygame as pg
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip()) # strip every additional line 

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def updat(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        # limit map scrolling
        x = min(0, x) # limit map scrolling à gauche
        y = min(0, y) # limit map scrolling top
        x = max(-(self.width - WIDTH), x) # à droite
        y = max(-(self.height - HEIGHT), y) # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
