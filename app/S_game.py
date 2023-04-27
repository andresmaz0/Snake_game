import pygame, sys, random
from class_player import Player
from class_donas import Donas
from class_body import body

#Pygame initiation
pygame.init()

#Setting screen dimensions
width,height=690,590
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

#Screen movement variables
x=0
x_relativa=0
n_colisiones=0

#Fps
clock = pygame.time.Clock()
fps=30

#Loading pictures
icon = pygame.image.load("snake_game/app/imagenes/serpiente.png")
pygame.display.set_icon(icon)
background = pygame.image.load("snake_game/app/imagenes/fondo_d.PNG")
head = pygame.image.load("snake_game/app/imagenes/head_s.png")
dona_r = pygame.image.load("snake_game/app/imagenes/dona_rosa.png")
ball_body = pygame.image.load("snake_game/app/imagenes/circulo_body.png")
#Sprites group
sprites = pygame.sprite.Group()
cuerpo = body(image=ball_body)
jugador = Player(width=width,height=height,image=head)
sprites.add(jugador)

#Adding donas
grupo_donas = pygame.sprite.Group()
dona_rosa = Donas(width=width,height=height,image=dona_r)
grupo_donas.add(dona_rosa)

#Game loop
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Updating sprites
    sprites.update()
    screen.fill((255,255,255))

    #Performing sprites collision
    colision = pygame.sprite.spritecollide(jugador,grupo_donas,False)
    if colision:
        dona_rosa.reaparicion()
        sprites.add(cuerpo)
        n_colisiones+=1

    """x_relativa = x % background.get_rect().width
    screen.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa<width:
        screen.blit(background,(x_relativa,0))
    x -= 0.8"""
    sprites.draw(screen)
    grupo_donas.draw(screen)
    cuerpo.posicion(head_x=jugador.rect.x,head_y=jugador.rect.top)
    jugador.movimiento()
    pygame.display.update()

pygame.quit()