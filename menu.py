import pygame
import sys
import os

# Initialisation
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Charge le fond
menu_path = os.path.join("assets", "menu.png")  # ou le nom réel de ton image
menu_image = pygame.image.load(menu_path).convert()
menu_image = pygame.transform.scale(menu_image, (screen_width+70, screen_height+50))

# Boucle du menu
running = True
while running:
    screen.blit(menu_image, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # clic gauche
            mouse_x, mouse_y = event.pos
            if 24<=mouse_x<=85 and 21<=mouse_y<=74:  # quit
                running = False

pygame.quit()
sys.exit()