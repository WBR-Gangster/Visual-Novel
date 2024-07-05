import pygame
from create_board import create_board
from data import *

pygame.init()

screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Visual Novel')

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	create_board(screen, wriothesley, 'Wriothesley', 'There shall be Plea for Justice', fontaine, fatui)

	pygame.display.update()

pygame.quit()