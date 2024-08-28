import pygame
from intro import create_intro
# from create_boxes import settings
from create_board import create_board
from create_chapter import create_chapter
from create_ending import create_ending
from multiple_choice import multiple_choice
# Data
from data import *

def single_implementing(config):
	create_board(screen, config['character_image'],config['character_name'],config['character_messages'], config['message_frame_type'], config['text_speed'], config['background'],config['situation'], config['next'])

def multiple_choices_implementing(config):
	multiple_choice(screen, config['character_image'],config['character_name'],config['character_messages'], config['message_frame_type'], config['text_speed'], config['background'],config['choices'], config['next'])

# Problem when user ran into an error it does not safe user state
# background is the orange board only
# background is no longer take out the hold window but just 80% to 90% of it
# situation contain multiple element to show including the background the character is in
# multiple choice should add situation
# should create our own orange message box and additional img in the middle of the board for character expression

while running:

	if state.page_state == 'end':
		end_capacity = state.chapter[state.page_state]
		first_end_key = list(end_capacity.keys())[0]
		
		state.chapter_phrase = state.page_state
		state.page_state = first_end_key

	if state.page_state == 'end_chapter':
		state.chapter = chapters[chapters.index(state.chapter) + 1]
		state.chapter_phrase = 'start'
		print(list(state.chapter[state.chapter_phrase].keys())[0])

		start_capacity = state.chapter[state.chapter_phrase]
		first_start_key = list(start_capacity.keys())[0]

		state.page_state = list(start_capacity.keys())[0]
		open_chapter.current = True
	
	if state.page_state == 'end_game':
		start_game.current = False
		end_game.current = True
	
	USER_MOUSE_POS = pygame.mouse.get_pos()

	screen.fill('black')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			with open("user_state.txt", "w") as f:
				f.write(f"{chapters.index(state.chapter)} {state.chapter_phrase} {state.page_state} {open_chapter.current}")
			running = False
		if SETTINGS_BUTTON.checkForInput(USER_MOUSE_POS):
			settings()
	
	if start_game.current and open_chapter.current:
		create_chapter(chapter_names[chapters.index(state.chapter)])

	elif start_game.current:
		if state.page_state.split('-')[0] == 'single':
			single_implementing(state.chapter[state.chapter_phrase][state.page_state])

		elif state.page_state.split('-')[0] == 'multiple':
			multiple_choices_implementing(state.chapter[state.chapter_phrase][state.page_state])

		else:
			print('error:', state.page_state)

	elif start_game.current == False and end_game.current:
		create_ending(screen)

	else:
		create_intro(USER_MOUSE_POS)

	pygame.display.update()

pygame.quit()