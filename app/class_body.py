import pygame, sys, random

class body (pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
    
    #Updating the position of my body
    def posicion(self,index_x:int,index_y:int):
        self.index_x = index_x
        self.index_y = index_y
        self.rect.x = self.index_x + 5
        self.rect.y = self.index_y - 20
        
        