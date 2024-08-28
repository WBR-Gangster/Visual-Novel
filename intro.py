import pygame, sys
from data import *

sys.path.insert(0, f'{USER_FILEPATH}\\module')

from button import Button

def play():
	global start_game
	start_game.current = True

def create_intro(USER_MOUSE_POS):

	global trigger_intro
	global PLAY_BUTTON
	global QUIT_BUTTON

	screen.blit(introBG, (0, 0))

	MENU_TEXT = pygame.font.SysFont(general_font, int(screen_height/12)).render("VISUAL NOVEL", True, "black")
	MENU_RECT = MENU_TEXT.get_rect(center=(screen_width/2, screen_height/5))

	if trigger_intro:

		gap = 100

		PLAY_BUTTON = Button(image=rectBtt, scale=0.6, pos=(screen_width/2, screen_height/2.5), 
			text_input="PLAY", font=general_font, font_size=None, base_color="White", hovering_color="Green")
		QUIT_BUTTON = Button(image=rectBtt, scale=0.6, pos=(screen_width/2, screen_height/2.5 + gap), 
			text_input="QUIT", font=general_font, font_size=None, base_color="White", hovering_color="Green")

		button_group.add(PLAY_BUTTON)
		button_group.add(QUIT_BUTTON)

		trigger_intro = False

	screen.blit(MENU_TEXT, MENU_RECT)

	button_group.draw(screen)
	button_group.update(screen, USER_MOUSE_POS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if PLAY_BUTTON.checkForInput(USER_MOUSE_POS):
				PLAY_BUTTON.kill()
				QUIT_BUTTON.kill()
				trigger_intro = True
				play()
			if SETTINGS_BUTTON.checkForInput(USER_MOUSE_POS):
				settings()
			if QUIT_BUTTON.checkForInput(USER_MOUSE_POS):
				running = False
				pygame.quit()
				sys.exit()
