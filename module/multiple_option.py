import pygame
import sys
import os

sys.path.insert(0, f'{os.getcwd()}')

from data import screen_width, screen_height

# Option Information
gap = screen_height/100
xo = screen_height/8
widtho_scale = screen_height/74
heighto = screen_height/18

class Choice(pygame.sprite.Sprite):
	def __init__(self, character_text, x, y, width, height):
		super().__init__()
		self.character_text = character_text
		self.image = pygame.Surface((width, height), pygame.SRCALPHA)
		pygame.draw.rect(self.image, (0, 0, 0, 128), self.image.get_rect(), border_radius=15)
		self.rect = self.image.get_rect()
		self.rect.topleft = [x, y]
		self.text_gap_x = height/3
		self.text_gap_y = height/6
		self.text_color = (255,255,255)
		self.font_size = int(height/1.8)
		self.font = pygame.font.SysFont('Arial', self.font_size)

	def update(self, screen): 
		xt = self.rect.x + self.text_gap_x
		yt = self.rect.y + self.text_gap_y

		text = self.font.render(self.character_text, True, self.text_color)
		screen.blit(text, (xt, yt))

# chúng ta cần choices space để làm cho các options nằm giữa khoảng space mình muốn user thấy
def generate_choices(choices, choices_group, choices_space):
	
	distribute = 0
	yo = choices_space/2 - (len(choices)*heighto + (len(choices)-1)*(gap))/2

	for i in range(len(choices)):
		choice_board = Choice(choices[i], xo, yo + distribute, widtho_scale*(max(len(x) for x in choices)), heighto)
		choices_group.add(choice_board)

		distribute += heighto + gap




		