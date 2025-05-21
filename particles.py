import pygame
import random

class Particle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen_width)
        self.y = random.randint(self.screen_height // 2, self.screen_height)
        self.radius = random.randint(1, 5)
        self.alpha = random.randint(100, 255)
        self.speed_y = random.uniform(0.3, 0.7)

    def update(self):
        self.y -= self.speed_y
        self.alpha -= 0.5
        if self.alpha <= 0 or self.y < 0:
            self.reset()

    def draw(self, screen):
        surface = pygame.Surface((6, 6), pygame.SRCALPHA)
        pygame.draw.circle(surface, (255, 202, 113, int(self.alpha)), (3, 3), self.radius)
        screen.blit(surface, (self.x, self.y))
