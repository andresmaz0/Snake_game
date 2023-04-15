import pygame, sys, random
from class_player import Player

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
icon = pygame.image.load("app/imagenes/serpiente.png")
pygame.display.set_icon(icon)
background = pygame.image.load("app/imagenes/fondo_d.PNG")
head = pygame.image.load("app/imagenes/head_s.png")
dona_r = pygame.image.load("app/imagenes/dona_rosa.png")

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
jugador = Player(width=width,height=height,head=head)
sprites.add(jugador)

#añadiendo las donas
grupo_donas = pygame.sprite.Group()
dona_rosa = Donas()
grupo_donas.add(dona_rosa)

#bucle del juego
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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