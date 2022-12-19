import pygame as pg
from settings import *
from main import *

class ArtifactHandler:

    def __init__(self, game, artifacts):
            self.artifacts = artifacts
            self.points = 0
            self.points_needed = len(artifacts)
            self.collected = False
            self.game = game

    def gather(self):
        self.points += 1

    def check_collected(self):
        if(self.points >= self.points_needed):
            self.collected = True

    def update(self):
        if self.collected == False:
            self.check_collected()
        else:
            if self.game.player.map_pos == (7,33) or self.game.player.map_pos == (8,33):
                print('you win')
                pass

        
            
