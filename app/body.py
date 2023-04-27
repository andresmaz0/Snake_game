import pygame, sys, random

class body (pygame.sprite.Sprite):
    def __init__(self,screen,color,head_x,head_y):
        super().__init__()
        self.image = pygame.draw.circle(screen,color,(head_x,head_y),30,0)