import pygame as pg
import sys
from settings import *
from main import *


class ArtifactHandler:

    def __init__(self, game, artifacts):
            self.artifacts = artifacts
            self.points = 0
            self.pick_up = pg.mixer.Sound('resources/sounds/item_get.ogg')
            self.monster_s_1 = pg.mixer.Sound('resources/sounds/monster_sound_2.ogg')
            self.monster_s_2 = pg.mixer.Sound('resources/sounds/monster_sound_1.ogg')
            self.monster_s_a = pg.mixer.Sound('resources/sounds/monster_attack.ogg')
            self.mission_c = pg.mixer.Sound('resources/sounds/mission_complete.ogg')
            self.points_needed = len(artifacts)
            self.collected = False
            self.won = False
            self.lost = False
            self.lost_text = False
            self.game = game
            self.w_text = pg.image.load("resources/sprites/text_sprites/mission_complete.png").convert_alpha()
            self.l_text = pg.image.load("resources/sprites/text_sprites/you_died.png").convert_alpha()
            self.text_1 = pg.image.load("resources/sprites/text_sprites/text_1.png").convert_alpha()
            self.text_2 = pg.image.load("resources/sprites/text_sprites/text_2.png").convert_alpha()
            self.text_3 = pg.image.load("resources/sprites/text_sprites/text_3.png").convert_alpha()
            self.monster = pg.image.load("resources/sprites/static_sprites/monster.png").convert_alpha()
            self.monster = pg.transform.scale(self.monster, (WIDTH,HEIGHT))
            self.text = 0
            self.wait_len = 20000
            

    def gather(self):
        self.points += 1
        self.wait_len += 5000
        pg.mixer.Sound.play(self.pick_up)

    def check_collected(self):
        if(self.points >= self.points_needed):
            self.collected = True

    def texter(self):
        cur_time = pg.time.get_ticks()
        global start_time
        if self.text == 0:
            start_time = pg.time.get_ticks()
            self.text = 1
        elif self.text ==1 and cur_time - 5000 > start_time:
            start_time = pg.time.get_ticks()
            self.text = 2
        elif self.text == 2 and cur_time - 5000 > start_time:
            start_time = pg.time.get_ticks()
            self.text = 3
        elif self.text == 3 and cur_time - 5000 > start_time:
            self.text = 4
        else:
            pass
    

    def monster_timer(self):
        cur_time = pg.time.get_ticks()

        if cur_time - self.wait_len + 10000 > 0 and cur_time - self.wait_len + 9980 < 0:
            pg.mixer.Sound.play(self.monster_s_1)

        if cur_time - self.wait_len + 5000 > 0 and cur_time - self.wait_len + 4980 < 0:
            pg.mixer.Sound.play(self.monster_s_2)

        if cur_time - self.wait_len > 0:

            if self.lost == False and self.won == False:
                pg.mixer.Sound.play(self.monster_s_a)
            self.lost = True
            
        if cur_time - self.wait_len - 5000 > 0:
            self.lost_text = True
            
        if cur_time - self.wait_len - 9000 > 0:
            pg.quit()
            sys.exit()

            


    def update(self):
        self.monster_timer()
        self.texter()
        cur_time = pg.time.get_ticks()
        start_time = 0
        if self.collected == False:
            self.check_collected()
        else:
            if self.game.player.map_pos == (7,33) or self.game.player.map_pos == (8,33):
                start_time = pg.time.get_ticks()
                if self.won == False:
                    pg.mixer.Sound.play(self.mission_c)
                self.won = True

            if self.won == True:

                if cur_time - 5000 > start_time:
                    pg.quit()
                    sys.exit()
                


            
                
                
    def draw(self):
        if self.won == True and self.lost == False:
            self.game.screen.blit(self.w_text, (350, 100))
        if self.text == 1:
            self.game.screen.blit(self.text_1, (350, 600))
        if self.text == 2:
            self.game.screen.blit(self.text_2, (350, 600))
        if self.text == 3:
            self.game.screen.blit(self.text_3, (350, 600))
        if self.lost == True and self.won == False:
            pg.draw.rect(self.game.screen, (0,0,0), (0,0,WIDTH,HEIGHT))
        if self.lost == True and self.won == False and self.lost_text == False:
            self.game.screen.blit(self.monster, (0, 0))
        if self.lost == True and self.won == False and self.lost_text == True:
            self.game.screen.blit(self.l_text, (350, 100))

            

            


            
        

        
            
