import pygame, sys, random

class Donas (pygame.sprite.Sprite):
    def __init__(self,width:int,height:int,image):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        #I get the rectangle of the image head
        self.rect = self.image.get_rect()
        self.reaparicion()

    #Method for dona reappearance after collision
    def reaparicion(self):
        self.rect.x = random.randrange(self.width - self.rect.width)
        self.rect.y = random.randrange(self.height - self.rect.height)