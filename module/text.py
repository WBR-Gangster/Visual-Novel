import pygame
import sys
import os
import word_limits

sys.path.insert(0, f'{os.getcwd()}')

from data import screen_width, screen_height, clickSound, general_font

pygame.init()

WHITE = (255,255,255)
DARK_YELLOW = (239, 204, 0)

class MessageBox(pygame.sprite.Sprite):
    def __init__(self, character_name, character_messages, x, y, width, height, speed):
        super().__init__()
        self.character_name = character_name
        self.character_messages = character_messages
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((255,165,0, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.gap = int(height/20)
        self.font_size = int(height/7)
        self.font = pygame.font.Font(general_font, self.font_size)
        self.speed = speed
        self.counter = 0
        # Word Limitation Distributin and Calculation
        self.gapSentence = self.gap/1.5
        self.text_sample = self.font.render("L", True, WHITE)
        self.word_width = self.text_sample.get_width()
        self.word_height = self.text_sample.get_height()
        self.limited_words_inline = 0 # not yet declare here
        self.lines = 3
        self.trigger_word = True
        # End here
        self.messages_index = 0
        self.message = self.character_messages[self.messages_index]
        self.sentences = []
        # self.sentence = ''
        self.sentence_index = [] #the Typing Animation Action by this this [0, 0, 0]
        self.sentences_index = 0
        self.sentence_appearence = [] # decide when will sentence appear [True, True, True]
        self.sentence_distribute = 0
        self.trigger = True
        self.sentence_done = False
        self.message_done = False
        self.complete_done = False
        self.clickSound = clickSound

    def update(self, screen, character_width, gapc):

        # create limited_words
        limit_width = self.width - character_width - gapc*2 - self.gap
        if self.trigger_word:
            self.limited_words_inline = int(limit_width / self.word_width)

            # Split Sentence
            message_splits= []
            message_element = ''
            current_words_inSentence = 0
            texts = self.message.split(' ')
            if len(self.message) > self.limited_words_inline:
                for text in texts:
                    text_length = len(text)
                    current_words_inSentence += text_length
                    if not (current_words_inSentence > self.limited_words_inline):
                        message_element += text + ' '
                    else:
                        message_element += text + ' '
                        message_splits.append(message_element)
                        message_element = ''
                        current_words_inSentence = 0
                message_splits.append(message_element)
            else:
                message_splits.append(self.message)
            
            print(message_splits)
            self.sentences = message_splits
            self.sentence_index = [0 for i in range(len(self.sentences))]

            self.sentence_appearence = [False for i in range(len(self.sentences))]
            self.sentence_appearence[0] = True
            # self.sentence = self.sentences[self.sentences_index]
            print(self.sentence_index)
            print(self.sentence_appearence)

            self.sentence_done = False
            self.trigger_word = False


        xn = self.rect.x + character_width + gapc*2
        yn = self.rect.y + gapc

        if self.character_name != '':
            name = self.font.render(self.character_name, True, DARK_YELLOW)
            name_height = name.get_height()
            screen.blit(name, (xn, yn))
        
        else:
            name_height = 0

        xm = xn
        ym = yn + name_height + self.gap

        # ------------------ SCROLLING ANIMATION ------------------ #

        if pygame.key.get_pressed()[pygame.K_RETURN] and self.sentence_done and self.message_done and self.messages_index < len(self.character_messages) - 1:
            self.clickSound.play()
            self.sentence_done = False
            self.message_done = False
            self.counter = 0
            self.messages_index += 1
            self.sentences_index = 0
            self.message = self.character_messages[self.messages_index]
            self.trigger_word = True

        if self.sentence_done and self.sentence_appearence == [True for i in range(len(self.sentences))]: #
            self.message_done = True

        if self.sentence_done and self.message_done and self.messages_index >= len(self.character_messages) - 1:
            self.complete_done = True

        if self.sentence_done and len(self.sentences) > 1 and self.message_done == False:
            self.sentences_index += 1
            # self.sentence_index
            self.sentence_appearence[self.sentences_index] = True 
            self.sentence_distribute = self.word_height + self.gapSentence
            self.sentence_done = False

        # print(self.sentence_index[self.sentences_index], len(self.sentences[self.sentences_index]))
        if self.sentence_index[self.sentences_index] == len(self.sentences[self.sentences_index]): #
            self.sentence_done = True

        if self.counter < self.speed:
            self.counter += 1

        if self.counter >= self.speed and self.sentence_done == False:
            self.sentence_index[self.sentences_index] += 1
            self.counter = 0

        for i in range(len(self.sentences)):
            if self.sentence_appearence[i]:
                screen.blit(self.font.render(self.sentences[i][0:self.sentence_index[i]], True, WHITE), (xm, ym + (self.sentence_distribute*i)))
        
        if self.message_done:
            xe = self.rect.x + self.width - self.gap
            ye = self.rect.y + self.height - self.gap

            enter = self.font.render("Enter", True, WHITE)
            screen.blit(enter, (xe-enter.get_width()-10, ye-enter.get_height()))

        # ------------------ END SCROLLING ANIMATION ------------------ #



