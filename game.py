import pygame
# Function create game board
from create_board import create_board
# Data
from data import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Visual Novel')

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	create_board(screen, wriothesley_image, wriothesley_name, 'There shall be Plea for Justice', fontaine, fatui)

	pygame.display.update()

pygame.quit()