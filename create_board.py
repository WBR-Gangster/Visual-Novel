import pygame
import sys
from dataclasses import dataclass
from data import *

nums_of_module = 4

for i in range(nums_of_module):
    sys.path.insert(i, f'{USER_FILEPATH}\\module')

from character import Character
from background import Background
from text import MessageBox
from situation import generate_situations

Sclick_one = True

def create_board(screen, character, character_name, character_messages, text_speed, background, situation, _next): # _next would be 'end' when the story end

	global state
	global trigger_cb
	global trigger_situation
	global Sclick_one
	global result
	global current_character
	global current_text
	global current_background
	global current_situation

	USER_MOUSE_POS = pygame.mouse.get_pos()

	# khi mà character và situation là None thì không tạo sprite cho nó và khi character là None thì không tạo tên nhận vật luôn 

	# Character Scale
	if character != None:
		crscale = (heightb - gapc*2)/(character.get_height())
		character_width = character.get_width()*crscale
	else:
		character_width = 0
		character_name = ''

	# trigger_cb là cần thiết vì nếu không có thì các sprite như text, character,... sẽ bị tạo liên tục
	# khi page đã được user đọc xong nhớ chuyển trigger hiện tại đang là False về True vì nếu không trang tiếp theo ko thể được thiết lập
	# thì trigger_cb đã là False r thì khối lệnh bên dưới đâu đc chạy, mà đâu đc chạy thì không tạo sprite =)))
	if trigger_cb:
		if character != None:
			current_character = Character(character, xc + (character.get_width()*crscale)/2 + gapc, yc, crscale)
			character_group.add(current_character)

		current_text = MessageBox(character_name, character_messages, xb, yb, widthb, heightb, text_speed)
		current_background = Background(background)

		text_group.add(current_text)
		background_group.add(current_background)

		Sclick_one = True
		trigger_cb = False	# chuyển False để các sprite ko đc tạo nữa

	if situation != None:
		generate_situations(situation)

	if current_text.complete_done and Sclick_one:
		# khi bấm enter thì user đã đọc xong hội thoại nhân vật và bước qua trang tiếp theo
		if pygame.key.get_pressed()[pygame.K_RETURN]:
			current_text.clickSound.play()

			character_group.empty()
			text_group.empty()
			situation_group.empty()
			background_group.empty()

			# trigger_cb đã được trả về True ở đây
			trigger_cb = True
			trigger_situation = True
			Sclick_one = False

			state.page_state = _next

	background_group.draw(screen)

	button_group.draw(screen)
	button_group.update(screen, USER_MOUSE_POS)

	situation_group.draw(screen)

	text_group.draw(screen)
	text_group.update(screen, character_width, gapc)

	character_group.draw(screen)

