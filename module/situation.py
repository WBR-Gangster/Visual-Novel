import pygame
import sys
import os

sys.path.insert(0, f'{os.getcwd()}')

from data import trigger_situation, situation_group

class Situation(pygame.sprite.Sprite):
	def __init__(self, image, width, height, x, y):
		super().__init__()
		self.scale = 0.8
		self.image = pygame.transform.scale(image, (width, height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

def config_situation(config):
	return [config['image'],config['img_width'],config['img_height'],config['img_x'],config['img_y']]

def generate_situations(situations):

	global trigger_situation

	if trigger_situation:
		for situation in situations:
			current_situation = Situation(*config_situation(situation)) # when situation is None then Situation sprite wont be created
			situation_group.add(current_situation)

			trigger_situation = False