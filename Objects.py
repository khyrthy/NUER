
# Imports
import pygame
from random import randint

pygame.mixer.init()


# Crates and Pieces class files

class Crate(pygame.sprite.Sprite):
	def __init__(self, game, texture, speed):
		super().__init__()

		# The crates will interact with the main game
		self.game = game

		self.authorized = False
		self.game.do_spawn_crates = False
		self.can_goleft = True

		# The texture is gived by an argument (see Game Class File) and loaded by the crate object
		self.image = pygame.image.load(texture)
		self.rect = self.image.get_rect()

		# Will place the crate on the ground, just at the screen hedge
		# Crates will move left during the game to make illusion that the player is moving
		self.rect.x = self.game.screen_width
		self.rect.y = self.game.ground_level - self.rect.height

		self.speed = speed

	# Function to move left the crate
	def go_left(self):

		# Better check if crates are allowed to move left (see Game Class File)
		if self.can_goleft:

			# Moves at 2px/s, like the background scrolling speed
			self.rect.x -= self.speed

			if self.rect.x + self.rect.width < self.game.screen_width and not self.authorized:
				self.game.do_spawn_crates = True
				self.authorized = True

			# If the crates if behind the left hedge of the screen
			# The game will simply remove it
			if self.rect.x + self.rect.width < 0:
				self.remove()

			# Crates needs to check where is the player
			# Then it will allow the main file to consider player is on a box
			self.check_player_place()

	# We need a remove function that simply removes the current object
	def remove(self):
		self.game.crates.remove(self)

	# (PHYSICS) Checks where is the player on the screen
	def check_player_place(self):

		# Checks if the player is in the box and on the ground
		if self.game.player.rect.x + self.game.player.rect.width > self.rect.x and self.game.player.rect.x < self.rect.x + self.rect.width:

			# The will die if he touches the box
			if self.game.player.rect.y + self.game.player.rect.height > self.rect.y and self.game.player.is_onground:

				# Here it's the case : Game Over
				self.game._signal_player_dead()

			# If the player is jumping/falling and is not on the ground
			elif self.game.player.rect.y + self.game.player.rect.height >= self.rect.y and not self.game.player.is_onground:

				# Will return to the main game that the player is on the current box
				self.game.player.is_onbox = True

				self.game.player.is_fall = False
				self.game.player.is_run = True

				# Force double-jump enabling at landing
				self.game.player.doublejump = False

				# ...and will place him on the box (When Glitching)
				self.game.player.rect.y = self.rect.y - self.game.player.rect.height

				# It is important to reset the fall counter to 0 (else the fall speed will be great
				self.game.player.fall_count = 0

			else:
				pass

		# If the player is on the ground and does not touches the crate
		elif self.game.player.is_onground:
			pass

		# If the player is at another place
		# Will simply make it fall
		else:
			self.game._signal_player_nowhere()

class Piece(pygame.sprite.Sprite):

	def __init__(self, game, y, speed, sounds):
		super().__init__()

		self.game = game

		self.sounds = sounds
		self.sound = None

		self.image = pygame.image.load("Assets/Piece/normal.png")
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = self.game.screen_width

		# All the animation frames are prealoded when Game starts, to prevent lagging
		# when loading and reloading image at every frame
		self.animation = [pygame.image.load("Assets/Piece/animation_0.png"),
		pygame.image.load("Assets/Piece/animation_1.png"),
		pygame.image.load("Assets/Piece/animation_2.png"),
		pygame.image.load("Assets/Piece/animation_3.png"),
		pygame.image.load("Assets/Piece/animation_4.png"),
		pygame.image.load("Assets/Piece/animation_5.png"),
		pygame.image.load("Assets/Piece/animation_6.png"),
		pygame.image.load("Assets/Piece/animation_7.png"),
		pygame.image.load("Assets/Piece/animation_8.png"),]

		self.animation_index = 0

		self.frame_skip_max = 2
		self.frame_skip = 0

		# The authorization to move is contained in this piece
		self.cangoleft = True

		# To prevent generating loads of pieces in a same place, piece generation is disabled
		# when a piece is generated
		# While piece is at screen border (object x position + object width > screen width)
		# The game can't generate other pieces
		self.game.do_generate_pieces = False

		# This variable sets to True at the first time the piece authorizes game to restart generating
		# Pieces, to prevent infinite authorizations, and loads of pieces at the same place
		self.authorized = False

		# Sets to true when piece is gathered
		# Allows piece to animate
		self.do_animate = False

		# To prevent giving the player a lot of score with only one piece, the piece sets this variable to True
		# Just once it gived a point.
		self.got_point = False

		# Obviously, speed variable
		self.speed = speed

	def go_left(self):

		if self.cangoleft:
			self.rect.x -= self.speed

			if self.rect.x + self.rect.width < self.game.screen_width and not self.authorized:
				self.game.do_generate_pieces = True
				self.authorized = True

			if self.rect.x + self.rect.width < 0:
				self.remove()

			self.check_player_place()

	def remove(self):
		self.game.pieces.remove(self)

	def check_player_place(self):

		if self.game.player.rect.center[0] > self.rect.x and self.game.player.rect.center[0] < self.rect.x + self.rect.width:
			if self.game.player.rect.center[1] > self.rect.y and self.game.player.rect.center[1] < self.rect.y + self.rect.height:

				if not self.got_point:
					self.got_point = True
					self.do_animate = True
					self.game.score += 1

					if self.game.options["play_sfx"] is True:
						self.PlaySound().play()


	# When piece is got, it makes animation
	def animate(self):

		# The animation will play only one time
		# After the animation finish, the piece will be removed
		if self.do_animate:
			if self.animation_index < 9:

				# The animation is too fast to be at 60FPS
				# The skip counter limits animation to play at 66% Lower
				# The same process is used for player animations
				if self.frame_skip == self.frame_skip_max:
					# Next frame in animation list
					self.image = self.animation[self.animation_index]

					# Increase animation index
					self.animation_index += 1

					# Reset frame skip counter to 0
					self.frame_skip = 0
				else:
					self.frame_skip += 1

				# Move up 10 pixels
				self.rect.y -= 10

			else:
				self.remove()

	def PlaySound(self):

		self.sound = pygame.mixer.Sound(self.sounds[randint(0, (len(self.sounds)-1))])

		return self.sound



# Code ends here
