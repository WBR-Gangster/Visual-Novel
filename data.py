import pygame
import os
import sys

USER_FILEPATH = os.getcwd()

IMAGE_DIR = f'{USER_FILEPATH}\\images'

def load_image(filename):
    return pygame.image.load(f'{IMAGE_DIR}\\{filename}')

# ------------------ CONFIRGURATION ------------------ #

# Screen Size
screen_width = 1200
screen_height = 700

# Message Box
gapb = 40
widthb = screen_width - gapb*2
heightb = screen_height/3
xb = gapb
yb = screen_height - heightb - gapb

# Situation // fix scale more flexible
xsi = screen_width/2
ysi = screen_height/2

# Gap for Characrer in MessageBox
gapc = int(heightb/12)

# Character
xc = xb
yc = yb + heightb/2

# Sprite Group
character_group = pygame.sprite.Group()
text_group = pygame.sprite.Group()
situation_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
choices_group = pygame.sprite.Group()

# Trigger for occuring once
trigger = True

# ------------------ DATA ------------------ #

# Character
wriothesley_name = 'Wriothesley'
wriothesley_image = load_image('wriothesley.webp')

# Background
fontaine = load_image('fontaine.jpg')

# Situtation
fatui = load_image('fatui.jpg')

