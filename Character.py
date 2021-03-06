import pygame
import random

# Player control class file

class Character(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        # Player class will interact with the game.
        self.game = game
        # Simply loads no-animation image (ERROR Case)
        self.image = pygame.image.load(self.game.current_character_path + self.game.current_character)

        # Defines player's rect
        self.rect = self.image.get_rect()

        self.doublejump = False

        # Putting Player at the ground level
        self.rect.x = 200
        self.rect.y = self.game.ground_level - self.rect.height

        # Enables running Physics phase
        self.is_run = True
        self.is_jump = False
        self.is_fall = False
        self.is_dead = False

        # Every sound related to the player
        self.ground1 = pygame.mixer.Sound("Assets/Sound/ground1.ogg")
        self.ground2 = pygame.mixer.Sound("Assets/Sound/ground2.ogg")
        self.ground3 = pygame.mixer.Sound("Assets/Sound/ground3.ogg")

        self.boxstep1 = pygame.mixer.Sound("Assets/Sound/boxstep1.ogg")
        self.boxstep2 = pygame.mixer.Sound("Assets/Sound/boxstep2.ogg")
        self.boxstep3 = pygame.mixer.Sound("Assets/Sound/boxstep3.ogg")
        self.boxstep4 = pygame.mixer.Sound("Assets/Sound/boxstep4.ogg")

        self.jump_sound = pygame.mixer.Sound("Assets/Sound/jump1.ogg")

        self.death_sound = pygame.mixer.Sound("Assets/Sound/loss1.ogg")
        self.played_death_sound = False

        # Player is falling
        self.is_onbox = False
        self.is_onground = True

        # Jump modifier
        self.jump_modifier = 0.05

        # Counts decreases when falling or jumping
        # That makes a smooth jumping and falling animation
        self.jump_count = 15
        self.fall_count = 0

        # Animation stuff
        self.current_run_frame = 0
        self.current_jump_frame = 0
        self.current_death_frame = 0

        self.run_frames = [pygame.image.load(self.game.current_character_path + "Run1.png"),
                           pygame.image.load(self.game.current_character_path + "Run2.png"),
                           pygame.image.load(self.game.current_character_path + "Run3.png"),
                           pygame.image.load(self.game.current_character_path + "Run4.png"),
                           pygame.image.load(self.game.current_character_path + "Run5.png"),
                           pygame.image.load(self.game.current_character_path + "Run6.png")]


        self.jump_frames = [pygame.image.load(self.game.current_character_path + "Jump1.png"),
                            pygame.image.load(self.game.current_character_path + "Jump2.png"),
                            pygame.image.load(self.game.current_character_path + "Jump3.png"),
                            pygame.image.load(self.game.current_character_path + "Jump4.png"),
                            pygame.image.load(self.game.current_character_path + "Jump5.png"),
                            pygame.image.load(self.game.current_character_path + "Jump6.png"),
                            pygame.image.load(self.game.current_character_path + "Jump7.png"),
                            pygame.image.load(self.game.current_character_path + "Jump8.png")]

        self.death_frames = [pygame.image.load(self.game.current_character_path + "Death1.png"),
                             pygame.image.load(self.game.current_character_path + "Death2.png"),
                             pygame.image.load(self.game.current_character_path + "Death3.png"),
                             pygame.image.load(self.game.current_character_path + "Death4.png"),
                             pygame.image.load(self.game.current_character_path + "Death5.png"),
                             pygame.image.load(self.game.current_character_path + "Death6.png"),
                             pygame.image.load(self.game.current_character_path + "Death7.png"),
                             pygame.image.load(self.game.current_character_path + "Death8.png"),
                             pygame.image.load(self.game.current_character_path + "Death9.png")]

        # Animations works with loops, and 3 frames will be skipped at every animation
        self.frame_counter = 0
        self.max_frame_skip = 3
        self.jump_frame_loop = 0
        self.death_frame_loop = 0

    def reload_frames(self):

        # Simply loads no-animation image (ERROR Case)
        self.image = pygame.image.load(self.game.current_character_path + self.game.current_character)

        # Defines player's rect
        self.rect = self.image.get_rect()

        self.rect.x = 200
        self.rect.y = self.game.ground_level - self.rect.height


        self.run_frames = [pygame.image.load(self.game.current_character_path + "Run1.png"),
                           pygame.image.load(self.game.current_character_path + "Run2.png"),
                           pygame.image.load(self.game.current_character_path + "Run3.png"),
                           pygame.image.load(self.game.current_character_path + "Run4.png"),
                           pygame.image.load(self.game.current_character_path + "Run5.png"),
                           pygame.image.load(self.game.current_character_path + "Run6.png")]

        self.jump_frames = [pygame.image.load(self.game.current_character_path + "Jump1.png"),
                            pygame.image.load(self.game.current_character_path + "Jump2.png"),
                            pygame.image.load(self.game.current_character_path + "Jump3.png"),
                            pygame.image.load(self.game.current_character_path + "Jump4.png"),
                            pygame.image.load(self.game.current_character_path + "Jump5.png"),
                            pygame.image.load(self.game.current_character_path + "Jump6.png"),
                            pygame.image.load(self.game.current_character_path + "Jump7.png"),
                            pygame.image.load(self.game.current_character_path + "Jump8.png")]

        self.death_frames = [pygame.image.load(self.game.current_character_path + "Death1.png"),
                             pygame.image.load(self.game.current_character_path + "Death2.png"),
                             pygame.image.load(self.game.current_character_path + "Death3.png"),
                             pygame.image.load(self.game.current_character_path + "Death4.png"),
                             pygame.image.load(self.game.current_character_path + "Death5.png"),
                             pygame.image.load(self.game.current_character_path + "Death6.png"),
                             pygame.image.load(self.game.current_character_path + "Death7.png"),
                             pygame.image.load(self.game.current_character_path + "Death8.png"),
                             pygame.image.load(self.game.current_character_path + "Death9.png")]

    # Next animation frame
    def next_frame(self):

        # Every frame will be applied as image during 3 frame
        self.frame_counter += 1

        # If the frame counter comes to the max_frame_skip (3 by default)
        if self.frame_counter == self.max_frame_skip:

            # Will set as image the next frame for every animation.
            # This is running animation stuff
            if self.is_run:
                if not self.current_run_frame == 6:
                    self.image = self.run_frames[self.current_run_frame]
                    self.current_run_frame += 1
                else:
                    self.current_run_frame = 0

            # This is jumps animation stuff
            elif self.is_jump:
                if self.jump_frame_loop == 0:
                    if not self.current_jump_frame >= 4:
                        self.image = self.jump_frames[self.current_jump_frame]
                        self.current_jump_frame += 1
                    else:
                        self.current_jump_frame = 0
                else:
                    if not self.current_jump_frame >= 5:
                        self.image = self.jump_frames[self.current_jump_frame]
                        self.current_jump_frame += 1
                    else:
                        self.current_jump_frame = 4
                self.jump_frame_loop += 1

            # This is fall animation stuff
            elif self.is_fall:
                if not self.current_jump_frame >= 6:
                    self.image = self.jump_frames[self.current_jump_frame]
                    self.current_jump_frame += 1
                else:
                    self.current_jump_frame = 5

            # This is the death animation stuff
            elif self.is_dead:
                if not self.current_death_frame == 9:
                    self.image = self.death_frames[self.current_death_frame]
                    self.rect.x -= 5
                    self.current_death_frame += 1
                    self.max_frame_skip += 1
                else:
                    self.game._signal_player_finished_deathanimation()

            # Reset the counter to 0 at end.
            self.frame_counter = 0

    def Ground_Sound(self, type):

        if type == "groundsound":
            p = random.randint(0, 2)
            if p == 0:
                return self.ground1
            elif p == 1:
                return self.ground2
            elif p == 2:
                return self.ground3
            return self.ground1

        elif type == "boxstep":
            p = random.randint(0, 3)
            if p == 0:
                return self.boxstep1
            elif p == 1:
                return self.boxstep2
            elif p == 2:
                return self.boxstep3
            elif p == 3:
                return self.boxstep4

            return self.boxstep1


# Code ends here
