import pygame, sys, random

#Se crea esta clase hija para que pueda heredar todas las herramientas para usar sprites
class Player(pygame.sprite.Sprite):
    def __init__(self,width:int,height:int,image):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        #obtengo el rectangulo de la imagen head
        self.rect = self.image.get_rect()
        self.rect.center = (width//2,height//2)
        #velocidad inicial
        self.velocidad_x = 0
        self.velocidad_y = 0

    def movimiento(self):
        #mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        self.velocidad_x = 0
        self.velocidad_y = 0

        #movimiento hacia la izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -5

        # movimiento hacia la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 5

        # movimiento hacia arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -5

        # movimiento hacia abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 5

        #actualiza la posicion de mi personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #limitacion de margenes
        #margen eje x
        if self.rect.left < 0:
            self.rect.right = self.width
        if self.rect.right > self.width:
            self.rect.left = 0
        #margen eje y
        if self.rect.top < 0:
            self.rect.bottom = self.height
        if self.rect.bottom > self.height:
            self.rect.top = 0