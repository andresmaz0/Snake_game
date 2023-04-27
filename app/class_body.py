import pygame, sys, random

class body (pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
    
    #Updating the position of my body
    def posicion(self,head_x:int,head_y:int):
        self.head_x = head_x
        self.head_y = head_y
        self.rect.x = self.head_x + 5
        self.rect.y = self.head_y - 30
        