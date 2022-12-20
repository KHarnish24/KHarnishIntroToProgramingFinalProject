import pygame as pg
import sys
from settings import *
from main import *


class ArtifactHandler:

    def __init__(self, game, artifacts):
            self.artifacts = artifacts
            self.points = 0
            self.points_needed = len(artifacts)
            self.collected = False
            self.won = False
            self.lost = False
            self.game = game
            self.w_text = pg.image.load("resources/sprites/text_sprites/mission_complete.png").convert_alpha()
            self.text_1 = pg.image.load("resources/sprites/text_sprites/mission_complete.png").convert_alpha()
            self.text = 0
            

    def gather(self):
        self.points += 1

    def check_collected(self):
        if(self.points >= self.points_needed):
            self.collected = True

    def text(self):
        cur_time = pg.time.get_ticks()
        start_time = 0
        if self.text == 0:
            start_time = pg.time.get_ticks()
            self.text = 1
        elif self.text ==1 and cur_time - 5000 > start_time:
            start_time = pg.time.get_ticks()
            self.text = 2
        elif self.text == 2 and cur_time - 5000 > start_time:
            start_time = 3
        else:
            pass
            


    def update(self):
        cur_time = pg.time.get_ticks()
        start_time = 0
        if self.collected == False:
            self.check_collected()
        else:
            if self.game.player.map_pos == (7,33) or self.game.player.map_pos == (8,33):
                start_time = pg.time.get_ticks()
                self.won = True

            if self.won == True:

                if cur_time - 5000 > start_time:
                    pg.quit()
                    sys.exit()
                


            
                
                
    def draw(self):
        if self.won == True and self.lost == False:
            self.game.screen.blit(self.w_text, (350, 100))
        if self.text == 1

            
        

        
            
