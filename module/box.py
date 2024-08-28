import pygame

class Box(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color):
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		pass


class Cancel(pygame.sprite.Sprite):
	def __init__(self, image, x, y, size):
		super().__init__()
		self.size = size
		self.image = pygame.transform.scale(image, (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.midright = [x, y]

	def update(self):
		pass

