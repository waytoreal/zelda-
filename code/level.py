import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprite = YSortCameraGroup()
        self.obstacles_sprite = pygame.sprite.Group()

        # sprite setup
        self.create_map()
    
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
            'grass' : import_csv_layout('./map/map_Grass.csv'),
            'object' : import_csv_layout('./map/map_Objects.csv'),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacles_sprite], 'invisible')
                        if style == 'grass':
                            pass
                        if style == 'object':
                            pass
        # for row_index, row in enumerate(WORLD_MAP):
        #     for col_index, col in enumerate(row):
        #         x = col_index * TILESIZE
        #         y = row_index * TILESIZE
        #         if col == 'x':
        #             Tile((x,y), [self.visible_sprite, self.obstacles_sprite])
        #         if col == 'p':
        #             self.player = Player((x,y), [self.visible_sprite], self.obstacles_sprite)
        self.player = Player((2000,1430), [self.visible_sprite], self.obstacles_sprite)

    def run(self):
        # update and draw the game
        self.visible_sprite.custom_draw(self.player)
        self.visible_sprite.update()
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf = pygame.image.load('./graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
    
    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        