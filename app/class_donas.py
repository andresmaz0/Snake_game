import pygame, sys, random

class Donas (pygame.sprite.Sprite):
    def __init__(self,width:int,height:int,image):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        #obtengo el rectangulo de la imagen head
        self.rect = self.image.get_rect()
        self.reaparicion()

    #metodo para reapiricion de dona despues de colision
    def reaparicion(self):
        self.rect.x = random.randrange(self.width - self.rect.width)
        self.rect.y = random.randrange(self.height - self.rect.height)