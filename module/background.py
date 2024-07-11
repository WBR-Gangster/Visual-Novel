import pygame
import sys
import os

sys.path.insert(0, f'{os.getcwd()}')

from data import screen_width, screen_height

class Background(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.image = pygame.transform.scale(image, (screen_width, screen_height))
		self.rect = self.image.get_rect()
		self.rect.topleft = [0, 0]