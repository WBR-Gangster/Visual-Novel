import pygame, sys

class Button(pygame.sprite.Sprite):
	def __init__(self, image,scale, pos, text_input, font, font_size, base_color, hovering_color):
		super().__init__()
		if image != None:
			self.width = image.get_width()*scale
			self.height = image.get_height()*scale
			self.image = pygame.transform.scale(image, (self.width, self.height))
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		if font_size != None:
			self.font_size = font_size
		else:
			self.font_size = int(self.height/2)
		self.font = pygame.font.SysFont(font, self.font_size)
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		if self.text_input != None:
			self.text = self.font.render(self.text_input, True, self.base_color)
		if image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		if text_input != None:
			self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

		if self.text_input != None:
			screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			if pygame.mouse.get_pressed()[0] == 1:
				return True
		return False