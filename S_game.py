import pygame, sys, random
from pygame.locals import*

#iniciacion de pygame
pygame.init()

#Estableciendo dimensiones de la pantalla
width,height=690,590
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

#variables movimiento de pantalla
x=0
x_relativa=0

#fps
clock = pygame.time.Clock()
fps=30

#cargando imagenes
icon = pygame.image.load("Snake game/imagenes/serpiente.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Snake game/imagenes/fondo_d.PNG")
head = pygame.image.load("Snake game/imagenes/head_s.png")
dona_r = pygame.image.load("Snake game/imagenes/dona_rosa.png")

#Se crea esta clase hija para que pueda heredar todas las herramientas para usar sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = head
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
            self.rect.right = width
        if self.rect.right > width:
            self.rect.left = 0
        #margen eje y
        if self.rect.top < 0:
            self.rect.bottom = height
        if self.rect.bottom > height:
            self.rect.top = 0

class Donas (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dona_r
        #obtengo el rectangulo de la imagen head
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(height - self.rect.height)

    #metodo para reapiricion de dona despues de colision
    def reaparicion(self,colision):
        if colision:

            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(height - self.rect.height)

#grupo de sprites
sprites = pygame.sprite.Group()
jugador = Player()
sprites.add(jugador)

#añadiendo las donas
grupo_donas = pygame.sprite.Group()
dona_rosa = Donas()
grupo_donas.add(dona_rosa)

#bucle del juego
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #actualizando los sprites
    sprites.update()
    screen.fill((255,255,255))

    #realizando colision de sprites
    colision = pygame.sprite.spritecollide(jugador,grupo_donas,False)
    dona_rosa.reaparicion(colision)

    """x_relativa = x % background.get_rect().width
    screen.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa<width:
        screen.blit(background,(x_relativa,0))
    x -= 0.8"""
    sprites.draw(screen)
    grupo_donas.draw(screen)
    jugador.movimiento()
    pygame.display.update()

pygame.quit()