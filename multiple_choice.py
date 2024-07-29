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

def multiple_choice(screen, character, character_name, character_messages, background, choices):

	global trigger

	# Character Scale
	crscale = (heightb - gapc*2)/(character.get_height())

	if trigger:
		current_character = Character(character, xc + (character.get_width()*crscale)/2 + gapc, yc, crscale)
		current_text = MessageBox(character_name, character_messages, xb, yb, widthb, heightb)
		current_background = Background(background)

		character_group.add(current_character)
		text_group.add(current_text)
		background_group.add(current_background)

		trigger = False


	background_group.draw(screen)

	generate_choices(choices, choices_group, yb)

	text_group.draw(screen)
	text_group.update(screen, character.get_width()*crscale, gapc)

	character_group.draw(screen)

	choices_group.draw(screen)
	choices_group.update(screen)