import sys
import pygame

nums_of_module = 4

for i in range(nums_of_module):
	sys.path.insert(i, 'C:\\Users\\HawlerMathew\\Documents\\code\\Handmade project\\Game\\module')

from character import Character
from background import Background
from text import MessageBox
from situation import Situation

screen_width = 1200
screen_height = 700

# Gap for Characrer in MessageBox
gapc = 20

# Message Box
gapb = 40
widthb = screen_width - gapb*2
heightb = screen_height/3
xb = gapb
yb = screen_height - heightb - gapb

# Situation // fix scale more flexible
siscale = 0.4
xsi = screen_width/2
ysi = screen_height/2

# Character
xc = xb
yc = yb + heightb/2

# Group
character_group = pygame.sprite.Group()
text_group = pygame.sprite.Group()
situation_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()

# Trigger for occuring once
trigger = True

def create_board(screen, character, character_name, character_text,background, situation):

	global trigger

	# Character Scale
	crscale = (heightb - gapc*2)/(character.get_height())
	
	if trigger:
		current_character = Character(character, xc + (character.get_width()*crscale)/2 + gapc, yc, crscale)
		current_text = MessageBox(character_name, character_text, xb, yb, widthb, heightb)
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