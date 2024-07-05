import pygame

screen_width = 1200
screen_height = 700

class Background(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.image = pygame.transform.scale(image, (screen_width, screen_height))
		self.rect = self.image.get_rect()
		self.rect.topleft = [0, 0]