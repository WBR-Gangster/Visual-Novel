import pygame
import sys
import time

class DialogueBox:
    def __init__(self, max_words=50):
        self.max_words = max_words
        self.current_text = ""
        self.word_buffer = []
        self.dialogue_ended = False

    def set_max_words(self, new_max_words):
        """Set a new maximum word limit for the dialogue box."""
        self.max_words = new_max_words

    def add_text(self, text):
        """Add text to the dialogue box, respecting the word limit."""
        if self.dialogue_ended:
            time.sleep(5)
            self.dialogue_ended = False
        
        words = text.split()
        for word in words:
            if len(self.word_buffer) < self.max_words:
                self.word_buffer.append(word)
            else:
                self.flush()
                self.word_buffer.append(word)

        # Flush remaining words if any
        self.flush()

    def flush(self):
        """Output the current buffer and reset it."""
        self.current_text = ' '.join(self.word_buffer)
        self.word_buffer = []

    def end_dialogue(self):
        """Ensure the remaining text in the buffer is output and set the dialogue as ended."""
        if self.word_buffer:
            self.flush()
        self.dialogue_ended = True

    def get_current_text(self):
        """Return the current text for display."""
        return self.current_text

def display_text(screen, text, font, position, bg_color, text_color):
    """Display text on the Pygame screen."""
    screen.fill(bg_color)  # Clear screen with background color
    rendered_text = font.render(text, True, text_color)  # Render text with text color
    screen.blit(rendered_text, position)
    pygame.display.flip()

def main():
    pygame.init()

    # Get device screen size
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h

    # Configuration settings based on screen size
    config = {
        "screen_width": screen_width/1.5 ,
        "screen_height": screen_height/1.5 ,
        "bg_color": (0, 0, 0),  # Black
        "text_color": (255, 255, 255),  # White
        "font_size": int(screen_height * 0.025),  # 5% of screen height
        "dialogue_max_words": 50,
        "font_path": None  # Default Pygame font
    }

    # Screen settings
    screen = pygame.display.set_mode((config["screen_width"], config["screen_height"]))
    pygame.display.set_caption("Visual Novel Dialogue Box")
    font = pygame.font.Font(config["font_path"], config["font_size"])

    # Dialogue box settings
    dialogue_box = DialogueBox(max_words=config["dialogue_max_words"])

    # Main loop
    running = True
    dialogues = [
        "This is the first dialogue sentence to demonstrate how the dialogue box works.",
        "Here is another sentence that will be added to the buffer.",
        "This is the second dialogue sentence, shown after the first dialogue."
    ]
    dialogue_index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if dialogue_index < len(dialogues):
                        dialogue_box.add_text(dialogues[dialogue_index])
                        dialogue_box.end_dialogue()
                        dialogue_index += 1
                    else:
                        running = False
                elif event.key == pygame.K_q:
                    running = False

        # Display the current text
        display_text(screen, dialogue_box.get_current_text(), font, (100, 50), config["bg_color"], config["text_color"])

        if dialogue_box.dialogue_ended and dialogue_index < len(dialogues):
            time.sleep(2)
            dialogue_box.dialogue_ended = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
