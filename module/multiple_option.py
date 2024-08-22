import pygame
import sys
import os

sys.path.insert(0, f'{os.getcwd()}')

from data import *

# Option Information
gap = screen_height/100
xo = screen_height/8
widtho_scale = screen_height/74
heighto = screen_height/18

class Choice(pygame.sprite.Sprite):
	def __init__(self, character_message, option_type, _next, x, y, width, height):
		super().__init__()
		self.character_message = character_message
		self.option_type = option_type
		self.next = _next
		self.image = pygame.Surface((width, height), pygame.SRCALPHA)
		pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), border_radius=15)
		self.rect = self.image.get_rect()
		self.rect.topleft = [x, y]
		self.text_gap_x = height/3
		self.text_gap_y = height/6
		self.text_color = (255,255,255)
		self.font_size = int(height/1.8)
		self.font = pygame.font.Font(general_font, self.font_size)
		self.clickSound = clickSound
		self.trigger = True

	def update(self, screen):

		global state
		global trigger_mc
		global character_group
		global text_group
		global background_group
		global choices_group

		cursor = pygame.mouse.get_pos()

		if self.rect.collidepoint(cursor):
			# khi người dùng chọn xong choices thì bước qua trang tiếp theo
			if pygame.mouse.get_pressed()[0] == 1 and self.trigger:
				self.clickSound.play()

				character_group.empty()
				text_group.empty()
				background_group.empty()
				choices_group.empty()

				# thay đổi phrase và page
				state.chapter_phrase = self.option_type
				state.page_state = self.next

				# có hay không cx đc, cơ bản tui thêm vô cho chắc :v
				self.trigger = False
				
				# trigger_mc đã được trả về True ở đây
				trigger_mc = True

				# trigger_mopt đã được trả về True ở đây
				trigger_mopt = True

		xt = self.rect.x + self.text_gap_x
		yt = self.rect.y + self.text_gap_y

		text = self.font.render(self.character_message, True, self.text_color)
		screen.blit(text, (xt, yt))

# chúng ta cần choices space để làm cho các options nằm giữa khoảng space mình muốn user thấy
def generate_choices(choices, choices_group, _next, choices_space):
	
	global trigger_mopt

	if trigger_mopt:
		distribute = 0
		yo = choices_space/2 - (len(choices)*heighto + (len(choices)-1)*(gap))/2

		for option, message in choices.items():
			choice_board = Choice(message, option, _next, xo, yo + distribute, widtho_scale*(max(len(x) for x in list(choices.values()))), heighto)
			choices_group.add(choice_board)

			distribute += heighto + gap

		trigger_mopt = False




		