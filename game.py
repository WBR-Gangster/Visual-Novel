import pygame
# Function create game board
from create_board import create_board
# Function create multiple-choices board
from multiple_choice import multiple_choice
# Data
from data import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Visual Novel')

# Chapter Trail by Dictionary

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	multiple_choice(screen, 
		wriothesley_image, 
		wriothesley_name, 
		['I will give you options, my Friend. Don\'t worry I am a nice Doggy',
		'So... My options for you is...'], 
		fontaine, 
		['One, You go to jail', 
			'Two, You pay the Fine', 
			'Three, you receive my Verdict', 
			'Or, be my goddamn slave']
		)

	pygame.display.update()

pygame.quit()