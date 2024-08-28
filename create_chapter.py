import pygame, sys
import os
from background import Background

sys.path.insert(0, f'{os.getcwd()}')

from data import *

WHITE = (255,255,255)
background_image = load_image('grey.jfif')
board_image = load_image('rect.jfif')
x_board = screen_width/2
y_board = screen_height/2
scale_board = (screen_width/1.4)/(board_image.get_width())

class Board(pygame.sprite.Sprite):
	def __init__(self, image, pos, scale, text):
		super().__init__()
		self.width = image.get_width()*scale
		self.height = image.get_height()*scale
		self.image = pygame.transform.scale(image, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.text = text
		self.font_size = int((image.get_height()*scale)/8)
		self.font = pygame.font.SysFont('timesnewroman', self.font_size)

	def update(self):
		chapter_text = self.font.render(self.text, True, WHITE)
		xch = self.rect.x + self.width/2 - chapter_text.get_width()/2
		ych = self.rect.y + self.height/2 - chapter_text.get_height()/2
		screen.blit(chapter_text, (xch, ych))

def create_chapter(text):

	global chapter_group
	global chapter_board_group
	global trigger_chapter
	global trigger_space
	global open_chapter
	global current_board

	if trigger_chapter:
		chapterSound.play()
		current_background = Background(background_image)
		current_board = Board(image = board_image, pos = (x_board, y_board), scale = scale_board, text= text)

		chapter_board_group.add(current_board)
		chapter_group.add(current_background)

		trigger_chapter = False

	chapter_group.draw(screen)

	chapter_board_group.draw(screen)
	chapter_board_group.update()

	if not pygame.mixer.get_busy():
		space = pygame.font.SysFont('timesnewroman', int(current_board.font_size/1.6)).render("Space to continue", True, WHITE)
		xsp = screen_width/2 - space.get_width()/2
		ysp = screen_height - space.get_height() - 15
		screen.blit(space, (xsp, ysp))

		if pygame.key.get_pressed()[pygame.K_SPACE] and trigger_space:
			open_chapter.current = False
			trigger_chapter = True
			chapter_group.empty()


