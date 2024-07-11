import pygame

class Character(pygame.sprite.Sprite):
	def __init__(self, image, x, y, scale):
		super().__init__()
		self.image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
