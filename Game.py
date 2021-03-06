from pygame import sprite
from Character import Character
import Utility
import random, time
from Objects import Crate, Piece

# This file contains the GAME class, for every Game Controlling Stuff

class Game:
	def __init__(self):

		# Game options
		self.options = {
			"play_music": True,
			"play_sfx": True,
			"show_fps": False,
			"difficulty": "normal",
			"max_FPS": 60,
		}


		self.can_pause = True


		self.score = 0
		self.highscore = 0

		# Ground Level, just at the bottom of player's image.
		self.ground_level = 495

		# There is 3 Characters in the Game. Every character has a path for it.
		# During Pre-Alpha, only the "Dude Monster" will be available, because there is not any menu in the game.
		self.current_character_path = "Assets/Heroes/Dude_Monster/"
		self.current_character = "Dude_Monster.png"
		# Defines the player, attribute object of Game
		self.player = Character(self)

		self.piece_sounds = [
			"Assets/Sound/coin1.ogg", "Assets/Sound/coin2.ogg",
			"Assets/Sound/coin3.ogg", "Assets/Sound/coin4.ogg",
			"Assets/Sound/coin5.ogg", "Assets/Sound/coin6.ogg",
			"Assets/Sound/coin7.ogg", "Assets/Sound/coin8.ogg",
			"Assets/Sound/coin9.ogg", "Assets/Sound/coin10.ogg"
		]

		self.speed = 2

		# Imports the screen width settings from "options.txt"
		# Will be useful later
		self.screen_width = 928



		# GameOver checking stuff
		self.game = True
		self.do_spawn_crates = True
		self.do_generate_pieces = True

		# Defines crates group, and paths to every textures available for the crates.
		# Textures can be customized, and crates can be modded. More data in Crates.py file
		self.crates = sprite.Group()
		self.crates_textures = [
			"Assets/Boxes/Box1.png", "Assets/Boxes/Box2.png", "Assets/Boxes/Box3.png",
			"Assets/Boxes/Box4.png", "Assets/Boxes/Box5.png", "Assets/Boxes/Box6.png",
			"Assets/Boxes/Box7.png", "Assets/Boxes/Box8.png"
			]
		self.pieces = sprite.Group()

		# Defining difficulty
		# Diffiulty is a value that can be changed in the "options.txt" file
		# That changes crates spawn rate.
		# Every frame a random number between 0 and 50, 100 or 150 (that depends on difficulty)
		# If this random number = 0, a crate will be spawned

		

		if self.options["difficulty"] == "easy":
			self.crate_spawn_value = 150
			self.piece_spawn_value = 200

		elif self.options["difficulty"] == "normal":
			self.crate_spawn_value = 100
			self.piece_spawn_value = 300

		elif self.options["difficulty"] == "hard":
			self.crate_spawn_value = 50
			self.piece_spawn_value = 400

		else:
			self.crate_spawn_value = 100
			self.piece_spawn_value = 300



		self.save_data = []
		self.load_data = []
		self.Load()

	def Save(self):

		Utility.LogMessage("Saving Game...", "INFO")
		self.save_data = [self.current_character, self.current_character_path, self.highscore, self.options]
		Utility.Save(self.save_data, "savegame.dat")

	def Load(self):

		Utility.LogMessage("Loading Save...", "INFO")
		self.load_data = Utility.Load("savegame.dat")

		self.current_character = self.load_data[0]
		self.current_character_path = self.load_data[1]
		self.highscore = self.load_data[2]
		self.options = self.load_data[3]

		# Reload difficulty

		if self.options["difficulty"] == "easy":
			self.crate_spawn_value = 150
			self.piece_spawn_value = 200

		elif self.options["difficulty"] == "normal":
			self.crate_spawn_value = 100
			self.piece_spawn_value = 300

		elif self.options["difficulty"] == "hard":
			self.crate_spawn_value = 50
			self.piece_spawn_value = 400

		else:
			self.crate_spawn_value = 100
			self.piece_spawn_value = 300

		Utility.LogMessage("Save Loaded", "INFO")

	def reload_difficulty(self):

		if self.options["difficulty"] == "easy":
			self.crate_spawn_value = 150
			self.piece_spawn_value = 200

		elif self.options["difficulty"] == "normal":
			self.crate_spawn_value = 100
			self.piece_spawn_value = 300

		elif self.options["difficulty"] == "hard":
			self.crate_spawn_value = 50
			self.piece_spawn_value = 400

		else:
			self.crate_spawn_value = 100
			self.piece_spawn_value = 300

	# Here is a function to try generating a crate.
	def try_generate_crate(self):
		# Checks if crates are allowed to be spawned
		if self.do_spawn_crates:

			if random.randint(0, self.crate_spawn_value) == 0:

				# Spawn a crate
				index = random.randint(0, (len(self.crates_textures) - 1))
				self.crates.add(Crate(self, self.crates_textures[index], self.speed))

	# Same thing with pieces
	def try_generate_piece(self):

		if self.do_generate_pieces:

			if random.randint(0, self.crate_spawn_value) == 0:

				self.pieces.add(Piece(self, 400, self.speed, self.piece_sounds))

	# The death signal, to prepare Game Over
	def _signal_player_dead(self):

		# Disables every Physics phase
		self.player.is_onbox = False
		self.player.is_fall = False
		self.player.is_jump = False
		self.player.is_run = False
		self.player.is_onground = False

		# Disables piece spawing and deletes every piece
		self.do_generate_pieces = False

		for piece in self.pieces:
			piece.cangoleft = False

		if self.score > self.highscore:
			self.highscore = self.score



		# Disables crates spawing and deletes every crate
		self.do_spawn_crates = False
		for crate in self.crates:

			# Disables crates movement
			crate.can_goleft = False






		# And prevents the Game that the player is dead
		self.player.is_dead = True


	# When the player is not on a crate, jumping or on the ground (ERROR Case)
	def _signal_player_nowhere(self):

		# Will simply make the Player fall
		self.player.is_onbox = False
		self.player.is_onground = False
		self.player.is_fall = True

	# player.is_dead sends a signal to the Player to make it play death animation
	# this signal with initialize loading screen
	def _signal_player_finished_deathanimation(self):

		# Removes every crate in the game
		for crate in self.crates:
			crate.remove()

		for piece in self.pieces:
			piece.remove()

		# Wait 2 seconds
		time.sleep(2)

		# Finally stops the game
		self.player.is_onground = True
		self.game = False

	def choose_music(self, musics):

		c = random.randint(0, len(musics)-1)
		return musics[c]

# Code ends here
