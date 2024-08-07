import pygame
import sys
from data import *

nums_of_module = 4

for i in range(nums_of_module):
    sys.path.insert(i, f'{USER_FILEPATH}\\module')

from character import Character
from background import Background
from text import MessageBox
from situation import Situation

def create_board(screen, character, character_name, character_messages, background, situation):

	global trigger

	# Character Scale
	crscale = (heightb - gapc*2)/(character.get_height())
	siscale = (screen_height/1.5)/(situation.get_height())

	if trigger:
		current_character = Character(character, xc + (character.get_width()*crscale)/2 + gapc, yc, crscale)
		current_text = MessageBox(character_name, character_messages, xb, yb, widthb, heightb)
		current_situation = Situation(situation, xsi, ysi, siscale)
		current_background = Background(background)

		character_group.add(current_character)
		text_group.add(current_text)
		situation_group.add(current_situation)
		background_group.add(current_background)

		trigger = False


	background_group.draw(screen)

	situation_group.draw(screen)

	text_group.draw(screen)
	text_group.update(screen, character.get_width()*crscale, gapc)

	character_group.draw(screen)