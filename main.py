import pygame

pygame.init()
ecran = pygame.display.set_mode((810, 540), pygame.RESIZABLE)

pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert()
pygame.display.set_icon(icon)

jouer = True

while jouer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jouer = False

pygame.quit()