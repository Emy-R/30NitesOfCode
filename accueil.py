import pygame
import sys
import os
from particles import Particle
import subprocess


# Initialisation
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Charger le fond
background_path = os.path.join("assets", "accueil.png")
background = pygame.image.load(background_path).convert()
background = pygame.transform.scale(background, (screen_width + 70, screen_height + 50))


# Créer les particules
particles = [Particle(screen_width, screen_height) for _ in range(50)]

# Boucle de l'accueil
running = True
while running:
    screen.blit(background, (0, 0))

    for p in particles:
        p.update()
        p.draw(screen)

    pygame.display.flip()
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # clic gauche
            mouse_x, mouse_y = event.pos
            if 24<=mouse_x<=85 and 21<=mouse_y<=74:  # quit
                running = False
            if 586<=mouse_x<=1224 and 637<=mouse_y<=867:    # clique sur le livre
                subprocess.run(["python", "menu.py"])  # lance menu.py
                pygame.quit()
                sys.exit()

pygame.quit()
sys.exit()
