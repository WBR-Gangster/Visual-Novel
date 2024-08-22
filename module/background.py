import pygame
import sys
import os

sys.path.insert(0, f'{os.getcwd()}')

from data import BG_width, BG_height, BG_x, BG_y

class Background(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.image = pygame.transform.scale(image, (BG_width, BG_height))
		self.rect = self.image.get_rect()
		self.rect.center = [BG_x, BG_y]