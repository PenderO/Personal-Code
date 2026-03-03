import pygame
import math
from map import *
from settings import *

class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.radius = 3
        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationAngle = 0
        self.moveSpeed = 0.5
        self.rotationSpeed = 1 * (math.pi/180)
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        self.turnDirection = 0
        self.walkDirection = 0
        
        if keys[pygame.K_d]:
            #self.turnDirection = 1
            self.x+=self.moveSpeed
        if keys[pygame.K_a]:
            #self.turnDirection = -1
            self.x-=self.moveSpeed
        if keys[pygame.K_w]:
            #self.walkDirection = 1
            self.y-=self.moveSpeed
        if keys[pygame.K_s]:
            #self.walkDirection = -1
            self.y+=self.moveSpeed
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1

        mouse_pos = pygame.mouse.get_pos()
            
        moveStep = self.walkDirection * self.moveSpeed
        self.rotationAngle += self.turnDirection * self.rotationSpeed
        self.x += math.cos(self.rotationAngle) * moveStep
        self.y += math.sin(self.rotationAngle) * moveStep
        
    def render(self,screen):
        pygame.draw.circle(screen,(255,0,0),(self.x-scroll[0],self.y-scroll[1]),self.radius)
        
        pygame.draw.line(screen,(255,0,0),(self.x-scroll[0],self.y-scroll[1]),(self.x-scroll[0]+math.cos(self.rotationAngle)*50,self.y-scroll[1]+math.sin(self.rotationAngle)*50))