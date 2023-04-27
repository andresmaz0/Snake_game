import pygame, sys, random

class body (pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
    
    #Updating the position of my body
    def posicion(self,head_x:int,head_y:int,colisiones:int):
        self.colisiones = colisiones
        self.head_x = head_x
        self.head_y = head_y
        if colisiones >= 1:
            self.rect.x = self.head_x + 5
            self.rect.y = self.head_y - 20 - ((colisiones-1)*10)
        
        