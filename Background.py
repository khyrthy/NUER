import pygame

# Class file for the background
# Needed to make it scroll

class Background:
    def __init__(self, image, position, origin, replace, speed):

        # Will load the backrgound image
        self.background = pygame.image.load(image)
        self.rect = self.background.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        # Allows the background to scroll
        self.do_slide = True

        # The origin position of the background, equal to the screen width
        self.origin = origin

        # The place where the background will be replaced
        self.replace_pos = replace

        # The scroll speed is 2 by default
        self.slide_velocity = speed

    # Replace the background at his origin position
    def return_to_origin(self):
        self.rect.x = self.origin[0]
        self.rect.y = self.origin[1]

    def replace(self):

        self.rect.x = self.replace_pos[0]
        self.rect.y = self.replace_pos[1]



    # Functions that changes x value
    def slide_horizontal(self):

        # Checks if the background is allowed to scroll
        if self.do_slide:

            self.rect.x -= self.slide_velocity

            # If the background isn't visible yet
            if self.rect.x + self.rect.width <= 2:

                # It will be replaced
                self.replace()

    # Same thing here with vertical sliding
    def slide_vertical(self):
        if self.do_slide:

            self.rect.y -= self.slide_velocity

            if self.rect.y + self.rect.height <= 0:

                self.replace()

# Code ends here
