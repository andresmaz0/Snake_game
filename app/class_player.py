import pygame, sys, random

#This child class is created so that it can inherit all the tools for using sprites.
class Player(pygame.sprite.Sprite):
    def __init__(self,width:int,height:int,image):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        #I get the rectangle of the image head
        self.rect = self.image.get_rect()
        self.rect.center = (width//2,height//2)
        #initial velocity
        self.velocidad_x = 0
        self.velocidad_y = 0

    def movimiento(self):
        #keep the keys pressed
        teclas = pygame.key.get_pressed()
        self.velocidad_x = 0
        self.velocidad_y = 0

        #leftward movement
        if teclas[pygame.K_a]:
            self.velocidad_x = -5

        #rightward movement
        if teclas[pygame.K_d]:
            self.velocidad_x = 5

        #Upward movement
        if teclas[pygame.K_w]:
            self.velocidad_y = -5

        #Downward movement
        if teclas[pygame.K_s]:
            self.velocidad_y = 5

        #Update my character's position
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Margin limitation
        #X-axis margin
        if self.rect.left < 0:
            self.rect.right = self.width
        if self.rect.right > self.width:
            self.rect.left = 0
        #Y-axis margin
        if self.rect.top < 0:
            self.rect.bottom = self.height
        if self.rect.bottom > self.height:
            self.rect.top = 0