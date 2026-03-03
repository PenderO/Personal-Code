import pygame
from settings import *
from mapconstants import *


class Map:
    def __init__(self):
        self.game_map = other_load_map('mapfile')
            
    def has_wall_at(self,x,y):
        print(x)
        print(y)
        print(TILESIZE)
        return self.game_map[int(y//TILESIZE)][int(x//TILESIZE)]
     #find some way to only render whats 
     #near the screen cause omg this is slow
    def render(self,screen):
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                #pixel coords
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE
                
                if int(self.game_map[i][j]) == 0:
                    pygame.draw.rect(screen,(140,140,140),(tile_x-scroll[0],tile_y-scroll[1],TILESIZE,TILESIZE))
                elif int(self.game_map[i][j]) == 1:
                    pygame.draw.rect(screen,(40,40,40),(tile_x-scroll[0],tile_y-scroll[1],TILESIZE,TILESIZE))