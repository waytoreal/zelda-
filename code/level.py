import pygame
from setting import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprite = pygame.sprite.Group()
        self.obstacles_sprite = pygame.sprite.Group()

        # sprite setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprite, self.obstacles_sprite])
                if col == 'p':
                    Player((x,y), [self.visible_sprite])

    def run(self):
        # update and draw the game
        self.visible_sprite.draw(self.display_surface)