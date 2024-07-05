import pygame

pygame.init()

font_size = 30

arial = pygame.font.SysFont('Arial', font_size)
WHITE = (255,255,255)
DARK_YELLOW = (239, 204, 0)

class MessageBox(pygame.sprite.Sprite):
    def __init__(self, character_name, character_text, x, y, width, height):
        super().__init__()
        self.gap = 20
        self.character_name = character_name
        self.character_text = character_text
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0,0,0, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, screen, character_width, gapc):
        
        xn = self.rect.x + character_width + gapc*2
        yn = self.rect.y + gapc

        name = arial.render(self.character_name, True, DARK_YELLOW)
        screen.blit(name, (xn, yn))

        xm = xn
        ym = yn + font_size + self.gap

        message = arial.render(self.character_text, True, WHITE)
        screen.blit(message, (xm, ym))

