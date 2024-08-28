import pygame
import sys
from data import *

sys.path.insert(0, f'{USER_FILEPATH}\\module')

from box import Box, Cancel

# Not finished Do Not Use

ORANGE = (255, 102, 0)
box_group = pygame.sprite.Group()

def settings():

	global trigger_box
	global box_group

	if trigger_box:
		print(x_settings, y_settings)
		settings = Box(width_settings, height_settings, x_settings, y_settings, ORANGE)
		# settings_cancel = Cancel(cancel_settings, x_cancel_settings, y_cancel_settings, size_cancel_settings)
		box_group.add(settings)
		print(settings)
		# box_group.add(settings_cancel)
		trigger_box = False

	box_group.draw(screen)
	box_group.update()


def donation():
	pass

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill('white')

	settings()

	pygame.display.update()

pygame.quit()