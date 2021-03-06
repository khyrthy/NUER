# GUI controll stuff
# With button stuff

import pygame
from random import randint

# The Button class
class Button:
    def __init__(self, normal, hover, pos):

        # Loads 2 images and the pos argument that is a tuple
        self.image_normal = pygame.image.load(normal)
        self.image_hover = pygame.image.load(hover)
        self.image_selected = pygame.image.load(hover)
        self.pos = pos

        self.selected = False

        # Sounds
        self.select1 = pygame.mixer.Sound("Assets/Sound/select1.ogg")
        self.select2 = pygame.mixer.Sound("Assets/Sound/select2.ogg")

        # Image and rect
        self.image = self.image_normal
        self.rect = self.image.get_rect()

        # Pos definition
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        # State variable
        self.is_hover = False

    # Check if the button is hover
    def check_mouse(self, mousepos):

        # If the player's mouse x pos is between button x pos and button x pos + button width
        if mousepos[0] > self.rect.x and mousepos[0] < self.rect.x + self.rect.width:
            # If the player's mouse y pos is between button y pos and button y pos + button height
            if mousepos[1] > self.rect.y and mousepos[1] < self.rect.y + self.rect.height:
                # Change state to hover
                self.is_hover = True

                self.image = self.image_hover


            else:

                if self.selected:
                    self.image = self.image_selected
                    self.is_hover = False
                else:
                    # change state to normal
                    self.is_hover = False
                    self.image = self.image_normal


        else:

            if self.selected:

                self.is_hover = False
                self.image = self.image_selected

            else:

                # change state to normal

                self.is_hover = False

                self.image = self.image_normal

    def check_selected(self):

        if self.selected:
            self.image = self.image_selected

        elif self.is_hover:
            self.image = self.image_selected

        else:
            self.image = self.image_normal

    def sound(self):
        s = randint(0, 1)

        if s == 0:
            return self.select1
        elif s == 1:
            return self.select2
        else:
            return self.select1

# The checkbox class, used in the game options
class Checkbox:



    def __init__(self, pos):

        # The checkbox class takes 4 images
        # Images does not change dynamically, so there is no need to put it in argument
        
            # Unselected in the "Off" position
        self.image_0_normal = pygame.image.load("Assets/GUI/CheckBox1.png")

            # Selected in the "Off" position
        self.image_0_hover = pygame.image.load("Assets/GUI/CheckBox1Hover.png")

            # Unselected in the "On" position
        self.image_1_normal = pygame.image.load("Assets/GUI/CheckBox2.png")

            # Selected in the "On" position
        self.image_1_hover = pygame.image.load("Assets/GUI/CheckBox2Hover.png")

        # The default image is Off position, unselected
        self.image = self.image_0_normal
        self.rect = self.image.get_rect()

        # The position of the element
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # The state of the button, defined at start on "OFF"
        # The state will be changed by the game save loading
        self.state = False
        self.is_hover = False

        # The sounds of the element
        self.select1 = pygame.mixer.Sound("Assets/Sound/select1.ogg")
        self.select2 = pygame.mixer.Sound("Assets/Sound/select2.ogg")

    # That functions decides what to do is mous is on the button
    def check_mouse(self, mousepos):
        
        # If the player's mouse x pos is between button x pos and button x pos + button width
        if mousepos[0] > self.rect.x and mousepos[0] < self.rect.x + self.rect.width:
            # If the player's mouse y pos is between button y pos and button y pos + button height
            if mousepos[1] > self.rect.y and mousepos[1] < self.rect.y + self.rect.height:
                # Change state to hover
                self.is_hover = True

                # If checkbox isn't active
                # Change image to inactive_hover
                if self.state == False:
                    self.image = self.image_0_hover
                
                # If checkbox is active
                # Change image to active_hover
                elif self.state == True:
                    self.image = self.image_1_hover

            else:
                # Change state to normal
                self.is_hover = False

        # Same process here
        else:
            self.is_hover = False

    # Update image without mouse pos
    def update_image(self):

        if self.state == True:
            if self.is_hover:
                self.image = self.image_1_hover
            else:
                self.image = self.image_1_normal
        elif self.state == False:
            if self.is_hover:
                self.image = self.image_0_hover
            else:
                self.image = self.image_0_normal

    # Happens if checkbox is clicked
    def change_state(self):

        # If inactive
        # Set to active
        if self.state == False:
            self.state = True


        # If active
        # Set to inactive
        elif self.state == True:
            self.state = False

    # Don't forget to play the sound :)
    def play_sound(self):

        # Create a random int between 0 and 1
        s = randint(0, 1)

        # If it's 0
        # Return select1 sound to main game
        if s == 0:
            return self.select1

        # If it's 1
        # Return select2 sound to the main game
        elif s == 1:
            return self.select2

        # Another case... Can happen ?
        # Return select1 sound to the main game
        else:
            return self.select1

# The value button
# A changer-button as seen in othger games like Mincecraft

class ValueButton:

    # Arguments :
    # Images for state1, state2, state3 (facultative), etc (extend as you wish) --> lists or tuples containing normal and hover images (path with extension)
    # Position --> list or tuple containg x and y position int values
    # Index Range of possibles states for this button --> tuple with 2 elements

    def __init__(self, state1, state2, state3, position, index_range, initpos):

        self.states = {

            "state1": {"normal": state1[0], "hover": state1[1]},
            "state2": {"normal": state2[0], "hover": state2[1]},
            "state3": {"normal": state3[0], "hover": state3[1]},

            # ...
            # Extend as you wish
        }


        # Extend as you wish here too

        # The position variable
        self.position = initpos
        self.active_state = self.states["state" + str(self.position)]
        self.range_min = index_range[0]
        self.range_max = index_range[1]

        # The image by default is normal image of state 1
        self.image = pygame.image.load(self.active_state["normal"])

        # The rect and the position defined in arguments
        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

        # Hover state
        self.hover = False

        # The sounds of the element
        self.select1 = pygame.mixer.Sound("Assets/Sound/select1.ogg")
        self.select2 = pygame.mixer.Sound("Assets/Sound/select2.ogg")

    def check_hover(self, mousepos):

        if mousepos[0] > self.rect.x and mousepos[0] < self.rect.x + self.rect.width:
            if mousepos[1] > self.rect.y and mousepos[1] < self.rect.y + self.rect.height:

                # Change hover state to true
                self.hover = True

                # Change image to hover
                self.image = pygame.image.load(self.active_state["hover"])
            
            else:

                # Change hover state to false
                self.hover = False

                # Change image to normal
                self.image = pygame.image.load(self.active_state["normal"])

        else:

            # Same process here
            self.hover = False
            self.image = pygame.image.load(self.active_state["normal"])


    def on_click(self):

        if self.position >= self.range_min and self.position < self.range_max:

            self.position += 1
        
        elif self.position == self.range_max:

            self.position = self.range_min

        # Update active state
        self.active_state = self.states["state" + str(self.position)]

        # Update Image
        if self.hover:
            self.image = pygame.image.load(self.active_state["hover"])
        
        else:
            self.image = pygame.image.load(self.active_state["normal"])


    def sound(self):

        # Create a random int between 0 and 1
        s = randint(0, 1)

        # If it's 0
        # Return select1 sound to main game
        if s == 0:
            return self.select1

        # If it's 1
        # Return select2 sound to the main game
        elif s == 1:
            return self.select2

        # Another case... Can happen ?
        # Return select1 sound to the main game
        else:
            return self.select1

