import pygame
from character import *
import math
from window import *

pygame.init()


window = Window()


clock = pygame.time.Clock()
FPS = 60

black = (0, 0, 0)
white = (255, 255, 255)

pygame.font.init()
pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)
option = pygame.image.load("ressources/img/option.png").convert_alpha()
option_pos = (1600, 150)
mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (0, 0)
pygame.mouse.set_visible(0)


rect_width = 50
rect_height = 100
rect_x = (window.largeur - rect_width) // 2
rect_y = (window.hauteur - rect_height) // 2
rect_speed = 15
rect = Rectangle(window.screen, rect_x, rect_y, rect_width, rect_height, rect_speed)


test = Rectangle(screen, 1500, 500, rect_width, rect_height, rect_speed)

objectsList = [test]

keys = []

#Liste des balles à l'écran
bulletList = []

# Image background
bg = pygame.image.load("ressources/img/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(window.largeur / bg_width) + 1

# Blit the background image
for i in range(0, tiles):
    window.screen.blit(bg, (i * bg_width, 0))

# Boucle de jeu
running = True
while running:
    # Affichage du scorlling background
    clock.tick(FPS)


    # Gestion des événements pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys.append(event.key)
        elif event.type == pygame.KEYUP:
            keys.remove(event.key)
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event == pygame.MOUSEBUTTONDOWN == option:
            pygame.draw.rect(window.screen, (0, 0, 0), (0, 0, 100, 100))

    # Déplacement continu avec collisions
    if pygame.K_z in keys:
        rect.move_up()
    if pygame.K_s in keys:
        rect.move_down()
    if pygame.K_q in keys:
        rect.move_left()
    if pygame.K_d in keys:
        rect.move_right()

    #Tir
    if pygame.K_SPACE in keys:
        bulletList.append(Bullet(screen, rect.getCoordinates()[0], rect.getCoordinates()[1]+40, 20, 10, 30))

    # Effacement de l'écran
    # screen.fill(white)

    # Blit the background image with scrolling
    for i in range(0, tiles):
        window.screen.blit(bg, (i * bg_width + scroll, 0))

    #Scrolling background
    scroll -= 5

    #boucle du background
    if abs(scroll) > bg_width:
        scroll = 0

    # Dessin du rectangle
    rect.draw(white)

    test.draw(black)


    #Operations des balles
    for bullet in bulletList:
        #Déplacement
        bullet.go_on()
        #Check des collisions avec les objets de objectsList
        for object in objectsList:
            if bullet.rect.colliderect(test):
                bulletList.remove(bullet)
        #Destruction des balles une fois le field traversé sans avoir rien touché
        if bullet.getCoordinates()[0] == screen_width-20 :
            bulletList.remove(bullet)


    # Rafraîchissement de l'affichage
    window.screen.blit(mouse, mouse_pos)
    window.screen.blit(option, option_pos)
    pygame.display.flip()

    pygame.display.update()

pygame.quit()
