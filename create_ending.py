import pygame
import sys
from PIL import Image, ImageFilter
from data import *

# Define colors
WHITE = (255, 255, 255)

# Function to apply blur using Pillow and convert to Pygame surface
def apply_blur(image_path, blur_radius, new_width, new_height):
    # Open the image using Pillow
    pil_image = Image.open(image_path)
    
    # Apply Gaussian blur
    blurred_pil_image = pil_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Resize the image to the new width and height
    blurred_pil_image = blurred_pil_image.resize((new_width, new_height))
    
    # Convert the blurred PIL image to a format Pygame understands
    image_bytes = blurred_pil_image.tobytes()
    mode = blurred_pil_image.mode
    surface = pygame.image.fromstring(image_bytes, blurred_pil_image.size, mode)
    
    return surface

def create_ending(screen):

    global ending_background_path
    global font_size_factor
    global scroll_speed_factor
    global y_position
    global trigger_endingSound

    if trigger_endingSound:
        endingSound.play(-1)  # -1 makes the music loop indefinitely
        trigger_endingSound = False

    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            # Calculate new window dimensions while maintaining aspect ratio
            width, height = event.w, event.h
            if width / height > aspect_ratio:
                width = int(height * aspect_ratio)
            else:
                height = int(width / aspect_ratio)
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # Get current window dimensions
    width = screen.get_width()
    height = screen.get_height()

    # Load and blur the background dynamically based on window size
    blurred_background = apply_blur(ending_background_path, 5, width, height)

    # Draw the blurred background image
    screen.blit(blurred_background, (0, 0))

    # Dynamically adjust font size and scroll speed
    font_size = height // font_size_factor
    font = pygame.font.SysFont('arial', font_size)
    scroll_speed = height // scroll_speed_factor

    # Create surface for credits text and calculate its height
    credit_surfaces = [font.render(line, True, WHITE) for line in credits]
    
    # Calculate the position of the starting text
    y = y_position

    # Render each line of text, adjusting y positions
    for surface in credit_surfaces:
        screen.blit(surface, (width // 2 - surface.get_width() // 2, y))
        y += surface.get_height()  # Add spacing between lines

    # Move the credits upwards
    y_position -= scroll_speed

    # Check if the credits have scrolled off-screen
    if y < 0:
        running = False  # End the loop when credits are fully scrolled out

# Stop the music when the credits are done
# pygame.mixer.music.stop()


