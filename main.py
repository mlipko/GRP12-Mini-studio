import pygame
import math
from character import *
from window import *
from weapons import *
from ennemies import *
from rectangle import *
from world import *

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




#Liste des objets à l'écran
#objectsList = [Basic(window, window.largeur+20, 100, 50, 50, 5), Basic(window, window.largeur+20, 200, 50, 50, 5), Basic(window, window.largeur+20, 300, 50, 50, 5)]
#objectsList = [[],[Idle(window, window.largeur+20, 100, 50, 50, 5)],[]]

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

#On initialise la variable de cooldown du shoot
shootCd = 0

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
    if pygame.K_SPACE in keys and shootCd == 0:
        objectsList[2].append(classic.bullet(window.screen, rect.getCoordinates()[0], rect.getCoordinates()[1]+40, 20, 10, 30, "ally"))
        shootCd = classic.tear
    
    if shootCd > 0:
        shootCd -= 1

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
    rect.draw()



    #On fait avancer chaque objets
    for object in objectsList[0]:
        object.go_on()

    for stun in tempon :
        stun.move_left()
        if stun.getCoordinates()[0] <= window.largeur:
            objectsList[1].append(stun)
            tempon.remove(stun)
            

    #On active les go_on ennemies
    for object in objectsList[1]:
        object.go_on(objectsList)



    #Operations des balles
    for bullet in objectsList[2]:
        #Déplacement
        bullet.go_on()
        #Check des collisions avec les objets de objectsList
        for referencial in objectsList[0]:
            if bullet.rect.colliderect(referencial):
                objectsList[2].remove(bullet)
                if referencial.destructible :
                    objectsList[0].remove(object)
                break
        for referencial in objectsList[1]:
            if bullet.rect.colliderect(referencial):
                objectsList[2].remove(bullet)
                objectsList[1].remove(referencial)
                break
        #Destruction des balles une fois le field traversé sans avoir rien touché
        if bullet.getCoordinates()[0] == window.largeur+20 :
            objectsList[2].remove(bullet)


    # Rafraîchissement de l'affichage
    window.screen.blit(mouse, mouse_pos)
    window.screen.blit(option, option_pos)
    pygame.display.flip()

    
    '''World.draw(window.screen)'''

    pygame.display.update()

pygame.quit()