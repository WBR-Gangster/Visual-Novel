import pygame
import sys
import os

sys.path.insert(0, f'{os.getcwd()}')

from data import screen_width, screen_height

pygame.init()

WHITE = (255,255,255)
DARK_YELLOW = (239, 204, 0)

class MessageBox(pygame.sprite.Sprite):
    def __init__(self, character_name, character_messages, x, y, width, height):
        super().__init__()
        self.character_name = character_name
        self.character_messages = character_messages
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0,0,0, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.gap = int(height/12)
        self.font_size = int(height/7.5)
        self.font = pygame.font.SysFont('Arial', self.font_size)
        self.speed = 3
        self.counter = 0
        self.messages_index = 0
        self.message_index = 0
        self.message = self.character_messages[self.messages_index]
        self.trigger = True
        self.done = False
        self.complete_done = False

    def update(self, screen, character_width, gapc):

        xn = self.rect.x + character_width + gapc*2
        yn = self.rect.y + gapc

        name = self.font.render(self.character_name, True, DARK_YELLOW)
        screen.blit(name, (xn, yn))

        xm = xn
        ym = yn + self.font_size + self.gap

        if pygame.key.get_pressed()[pygame.K_RETURN] and self.done and self.messages_index < len(self.character_messages) - 1:
            self.done = False
            self.counter = 0
            self.messages_index += 1
            self.message_index = 0
            self.message = self.character_messages[self.messages_index]

        if self.done and self.messages_index >= len(self.character_messages) - 1:
            self.complete_done = True

        if self.message_index == len(self.message):
            self.done = True

        if self.counter < self.speed:
            self.counter += 1

        if self.counter >= self.speed and self.done == False:
            self.message_index += 1
            self.counter = 0

        snip = self.font.render(self.message[0:self.message_index], True, WHITE)
        screen.blit(snip, (xm, ym))


