import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from artifact_handler import *
from random import randint


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
# artifact placement randomizer 

        places = [((9.5, 2.5)), (6.5, 2.5), (11.5,6.5),(8.5,12.5), (1.5,18.5), (14.5,18.5), (5.5,26.5), (10.5, 26.5), (7.5, 18.5), (10.5, 8.5), (1.5, 2.5)]
        place_1 = places[randint(0, len(places)-1)]
        places.remove(place_1)
        place_2 = places[randint(0, len(places)-1)]
        places.remove(place_2)
        place_3 = places[randint(0, len(places)-1)]
        places.remove(place_3)
        place_4 = places[randint(0, len(places)-1)]
        



        self.static_sprite_1 = SpriteObject(self, place_1, 1)
        self.static_sprite_2 = SpriteObject(self, place_2, 2)
        self.static_sprite_3 = SpriteObject(self, place_3, 3)
        self.static_sprite_4 = SpriteObject(self, place_4, 4)
        self.artifact_handler = ArtifactHandler(self,[self.static_sprite_1, self.static_sprite_2, self.static_sprite_3, self.static_sprite_4])
        # self.animated_sprite = AnimatedSprite(self, (8.5, 2.5))

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite_1.update()
        self.static_sprite_2.update()
        self.static_sprite_3.update()
        self.static_sprite_4.update()
        self.artifact_handler.update()
        
        # self.animated_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        
        # pg.draw.rect()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()



if __name__ == '__main__':

    game = Game()
    game.run()