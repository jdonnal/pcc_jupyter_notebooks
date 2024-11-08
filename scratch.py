import pygame
import time


class Character:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('../images/ship_alt.png')
        self.rect = self.image.get_rect()
        # center the character
        self.rect.center = self.screen.get_rect().center

    def draw(self):
        self.screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((170, 240, 240))
character = Character(screen)
character.draw()

pygame.display.flip()
time.sleep(8)