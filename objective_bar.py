import pygame as pg
from settings import *
from main import *

class ObjectiveBar:

    def __init__(self, game):
        self.image = pg.image.load("resources/sprites/static_sprites/meter/level_0.png").convert_alpha()
        self.game = game

    
    def update(self):
        if self.game.artifact_handler.points == 1:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_1.png").convert_alpha()
        elif self.game.artifact_handler.points == 2:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_2.png").convert_alpha()
        elif self.game.artifact_handler.points == 3:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_3.png").convert_alpha()
        elif self.game.artifact_handler.points == 4:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_4.png").convert_alpha()
        

    def draw(self):
        self.game.screen.blit(self.image, (80, -10))