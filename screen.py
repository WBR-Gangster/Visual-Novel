import pygame, sys
from data import *

pygame.init()

#---------------------------------BUTTON---------------------------------#
class Button():
	def __init__(self, image,scale, pos, text_input, font, base_color, hovering_color):
        self.width = image.get_width()*scale
        self.height = image.get_height()*scale
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font_size = int(self.height/7.5)
        self.font = pygame.font.SysFont("timesnewroman", size)
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

			
#---------------------------------MAIN screen FONT---------------------------------#
def get_font(size):
    return pygame.font.SysFont("timesnewroman", size)

#---------------------------------screen---------------------------------#
def play():
global start_game
start_game.current = True

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")
        gapc = 200

        OPTIONS_TEXT = get_font(50).render("Options screen", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(screen_width/2, screen_height/3))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, 1,pos=(screen_width/2, screen_height/2 + gapc), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    screen.blit(introBG, (0, 0))
    gap = 180

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(50).render("VISUAL NOVEL", True, "black")
    MENU_RECT = MENU_TEXT.get_rect(center=(screen_width/2, screen_height/5))

    PLAY_BUTTON = Button(image=rectBtt, 1, pos=(screen_width/2, screen_height/3), 
                        text_input="PLAY", font=get_font(60), base_color="White", hovering_color="Green")
    OPTIONS_BUTTON = Button(image=rectBtt, 1,  pos=(screen_width/2, screen_height/2), 
                        text_input="OPTIONS", font=get_font(60), base_color="White", hovering_color="Green")
    QUIT_BUTTON = Button(image=rectBtt, 1,  pos=(screen_width/2, screen_height/2 + gap), 
                        text_input="QUIT", font=get_font(60), base_color="White", hovering_color="Green")

    screen.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                play()
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                options()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

