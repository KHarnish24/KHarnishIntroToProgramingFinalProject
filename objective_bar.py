import pygame as pg
from settings import *
from main import *
from random import randint

class ObjectiveBar:

    def __init__(self, game):
        self.image = pg.image.load("resources/sprites/static_sprites/meter/level_0.png").convert_alpha()
        self.game = game
        self.flicked = False
        self.opas = 100

    
    def update(self):
        if self.game.artifact_handler.points == 1:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_1.png").convert_alpha()
        elif self.game.artifact_handler.points == 2:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_2.png").convert_alpha()
        elif self.game.artifact_handler.points == 3:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_3.png").convert_alpha()
        elif self.game.artifact_handler.points == 4:
            self.image = pg.image.load("resources/sprites/static_sprites/meter/level_4.png").convert_alpha()
        self.fog_flicker()

    def fog_flicker(self):
        global time_len
        global start_time
        cur_time = pg.time.get_ticks()
        if self.flicked == False:
            self.flicked = True
            start_time = pg.time.get_ticks()
            self.opas = randint(100,200)
            time_len = randint(2000, 6000)
        elif cur_time - time_len > start_time:
            self.flicked = False
        self.fog = pg.Surface((WIDTH,HEIGHT))
        self.fog.fill((0,0,0))
        self.fog.set_alpha(self.opas)


        
        

    def draw(self):
        
        self.game.screen.blit(self.fog, (0,0))
        self.game.screen.blit(self.image, (80, -10))
        