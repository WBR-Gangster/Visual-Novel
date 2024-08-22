import pygame
import sys
from data import *

nums_of_module = 4

for i in range(nums_of_module):
    sys.path.insert(i, f'{USER_FILEPATH}\\module')

from character import Character
from background import Background
from text import MessageBox
from multiple_option import generate_choices

def multiple_choice(screen, character, character_name, character_messages, text_speed, background, choices, _next):

	global trigger_mc
	global current_text

	USER_MOUSE_POS = pygame.mouse.get_pos()

	# Character Scale
	crscale = (heightb - gapc*2)/(character.get_height())

	# trigger_mc là cần thiết vì nếu không có thì các sprite như text, character,... sẽ bị tạo liên tục
	# khi page đã được user đọc xong nhớ chuyển trigger hiện tại đang là False về True vì nếu không trang tiếp theo ko thể được thiết lập
	# trigger_mc được trả về true ở module multiple_option
	# thì trigger_mc đã là False r thì khối lệnh bên dưới đâu đc chạy, mà đâu đc chạy thì không tạo sprite
	if trigger_mc:
		current_character = Character(character, xc + (character.get_width()*crscale)/2 + gapc, yc, crscale)
		current_text = MessageBox(character_name, character_messages, xb, yb, widthb, heightb, text_speed)
		current_background = Background(background)

		character_group.add(current_character)
		text_group.add(current_text)
		background_group.add(current_background)

		trigger_mc = False

	SETTINGS_BUTTON = settings_button()

	background_group.draw(screen)

	button_group.draw(screen)
	button_group.update(screen, USER_MOUSE_POS)

	# khi mà nhân vật xong hội thoại thì mới hiện các choices
	if current_text.complete_done:
		generate_choices(choices, choices_group, _next, yb)	

	text_group.draw(screen)
	text_group.update(screen, character.get_width()*crscale, gapc)

	character_group.draw(screen)

	choices_group.draw(screen)
	choices_group.update(screen)