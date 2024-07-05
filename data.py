import pygame

IMAGE_DIR = 'C:\\Users\\HawlerMathew\\Documents\\code\\Handmade project\\Game\\images'

def load_image(filename):
    return pygame.image.load(f'{IMAGE_DIR}\\{filename}')

# Character
wriothesley = load_image('wriothesley.webp')

# Background
fontaine = load_image('fontaine.jpg')

# Situtation
fatui = load_image('fatui.jpg')