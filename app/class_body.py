import pygame, sys, random

class body (pygame.sprite.Sprite):
    def __init__(self,width:int,height:int,image):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        #I get the rectangle of the image head
        self.rect = self.image.get_rect()
    
    """def posicion
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y"""
        