import pygame, sys, random

class body (pygame.sprite.Sprite):
    def __init__(self,head_x:int,head_y:int,image):
        super().__init__()
        self.image = image
        self.head_x = head_x
        self.head_y = head_y
        #I get the rectangle of the image head
        self.rect = self.image.get_rect()
    
    """def posicion(self):
        self.rect.x = 
        self.rect.y = self.velocidad_y"""
        