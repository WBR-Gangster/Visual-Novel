import pygame
import os

USER_FILEPATH = os.getcwd()

IMAGE_DIR = f'{USER_FILEPATH}\\images'

def load_image(filename):
    return pygame.image.load(f'{IMAGE_DIR}\\{filename}')

# Screen Size
screen_width = 844
screen_height = 390

# Character
wriothesley_name = 'Wriothesley'
wriothesley_image = load_image('wriothesley.webp')

# Background
fontaine = load_image('fontaine.jpg')

# Situtation
fatui = load_image('fatui.jpg')

