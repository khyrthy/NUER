# Imports
import pygame, sys

# Game Modules Imports
import Utility, GUI
from Game import Game
from Background import Background



# Init pygame cores
pygame.init()

LOADINGWINDOW = pygame.display.set_mode((928, 552))
pygame.display.set_caption("Nao's Universe: Endless Run")
pygame.display.set_icon(pygame.image.load("icon.png"))
LOADINGCLOCK = pygame.time.Clock()

Utility.LogMessage("Starting game loading", "INFO")
Utility.LogMessage("Starting intro video", "INFO")

Loading = True
GameLoaded = False

intro = Utility.Video("Assets/Video/", 1, 222, 0, "", False)

while Loading:

	if not intro.play and intro.playedtimes == 0:

		intro.play = True
		if not intro.audio:
			Utility.LogMessage("Intro video does not have audio", "WARNING")
		else:
			intro.audio.play()

	if intro.finished:
		Loading = False

	intro.next_frame()

	LOADINGWINDOW.fill((0, 0, 0))
	LOADINGWINDOW.blit(intro.image, (0, 0))

	pygame.display.flip()

	# Keep at 22FPS
	LOADINGCLOCK.tick(22)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()

	if not GameLoaded:

		# Game Class
		GAME = Game()

		# Cursor Image
		Utility.LogMessage("Initializing Cursor...", "LOADINGINFO")
		Cursor = pygame.image.load("Assets/cursor.png")
		Cursor_Rect = Cursor.get_rect()
	

		# Font for non-image text
		Utility.LogMessage("Initializing font...", "LOADINGINFO")
		FONT = pygame.font.Font("Assets/font.ttf", 42)

		# Creating refresh-rate clock
		Utility.LogMessage("Initializing clock...", "LOADINGINFO")
		CLOCK = pygame.time.Clock()

		# FPS option in "savegame.dat", please prefer using the refresh rate of your monitor,
		# Default is 60FPS
		Utility.LogMessage("Initializing FPS...", "LOADINGINFO")
		FPS = GAME.options["max_FPS"]



		# This list is necessary for random music chooser
		Utility.LogMessage("Initializing music...", "LOADINGINFO")
		MUSICS = ["Assets/Sound/music1.ogg", "Assets/Sound/music2.ogg", "Assets/Sound/music3.ogg"]

		# The ShowFps option, if needed
		# Displays FPS counter on screen
		Utility.LogMessage("Initializing ShowFPS...", "LOADINGINFO")
		

		# Creating "Game" Object, Class that controls all game objects (Character, crates, etc...)
		# For more info, see the Game.py file
		Utility.LogMessage("Initializing game consts...", "LOADINGINFO")
		GAME = Game()

		# The Game is made with 2 Backgrounds, doing an infinite scrolling to make seems like the player is forwarding
		Utility.LogMessage("Initializing backgrounds...", "LOADINGINFO")
		Background1 = Background("Assets/Background.jpeg", (0, 0), (0, 0), (928, 0), 2)
		Background2 = Background("Assets/Background.jpeg", (298, 0), (928, 0), (928, 0), 2)

		# Credits scrolling image
		Credits = Background("Assets/GUI/Credits.png", (0, 557), (0, 557), (0, 557), 1)

		# The Death screen is just a background that listens for your instruction.
		Background_death = pygame.image.load("Assets/GameOver.png")
		Background_menu = pygame.image.load("Assets/Background.jpeg")

		# Menu stuff
		Utility.LogMessage("Initializing image assets...", "LOADINGINFO")
		Title = pygame.image.load("Assets/GUI/Title.png")

		ScoreIndicatorImage = pygame.image.load("Assets/GUI/score_indicator.png")
		HighScoreIndicatorImage = pygame.image.load("Assets/GUI/highscore_indicator.png")

		Text2 = pygame.image.load("Assets/GUI/Text2.png")

		# Pause menu stuff
		Pause_Title = pygame.image.load("Assets/GUI/PauseMenu/title.png")

		Pause_Button_Resume = GUI.Button("Assets/GUI/PauseMenu/resume_normal.png", "Assets/GUI/PauseMenu/resume_hover.png", (325, 250))
		Pause_Button_Quit = GUI.Button("Assets/GUI/PauseMenu/quit_normal.png", "Assets/GUI/PauseMenu/quit_hover.png", (325, 350))

		# The buttons of the Game
		Utility.LogMessage("Initializing buttons...", "LOADINGINFO")
		Button_Play = GUI.Button("Assets/GUI/PlayButton.png", "Assets/GUI/PlayButtonHover.png", (50, 200))
		Button_Settings = GUI.Button("Assets/GUI/OptionsButton.png", "Assets/GUI/OptionsButtonHover.png", (50, 300))
		Button_Credits = GUI.Button("Assets/GUI/CreditsButton.png", "Assets/GUI/CreditsButtonHover.png", (50, 400))

		
		# GUI of the options-part of the game
		Options_Title = pygame.image.load("Assets/GUI/OptionsTitle.png")
		Button_Options_Back = GUI.Button("Assets/GUI/BackButton.png", "Assets/GUI/BackButtonHover.png", (10, 15))
		Options_Text = pygame.image.load("Assets/GUI/options_text.png")

		# Buttons of Game Over screen
		Gameover_Backmenu = GUI.Button("Assets/GUI/Gameover/Backmenu.png", "Assets/GUI/Gameover/Backmenu_Hover.png", (161, 295))
		Gameover_Tryagain = GUI.Button("Assets/GUI/Gameover/Tryagain.png", "Assets/GUI/Gameover/Tryagain_Hover.png", (489, 295))

		if GAME.options["difficulty"] == "easy":
			tempvar = 1
		elif GAME.options["difficulty"] == "normal":
			tempvar = 2
		elif GAME.options["difficulty"] == "hard":
			tempvar = 3

		Slider_difficulty = GUI.ValueButton(["Assets/GUI/DifficultyButton/easy_normal.png", "Assets/GUI/DifficultyButton/easy_hover.png"], ["Assets/GUI/DifficultyButton/normal_normal.png", "Assets/GUI/DifficultyButton/normal_hover.png"],
		["Assets/GUI/DifficultyButton/hard_normal.png", "Assets/GUI/DifficultyButton/hard_hover.png"], (700, 280), (1, 3), tempvar)

		del tempvar


		# The checkbox of the options-part of the game
		Utility.LogMessage("Initializing checkbox...", "LOADINGINFO")
		Checkbox_Music = GUI.Checkbox((790, 170))
		Checkbox_Sfx = GUI.Checkbox((790, 225))
		Checkbox_Showfps = GUI.Checkbox((790, 345))

		#	... Change their state
		Checkbox_Music.state = GAME.options["play_music"]
		Checkbox_Sfx.state = GAME.options["play_sfx"]
		Checkbox_Showfps.state = GAME.options["show_fps"]



		# Character choosing Menu
		Text1 = pygame.image.load("Assets/GUI/Text1.png")
		Ch_Nao = GUI.Button("Assets/GUI/Heroes/Dude_Monster.png", "Assets/GUI/Heroes/Dude_Monster_Hover.png", (475, 340))
		Ch_Tao = GUI.Button("Assets/GUI/Heroes/Owlet_Monster.png", "Assets/GUI/Heroes/Owlet_Monster_Hover.png", (600, 340))
		Ch_Geo = GUI.Button("Assets/GUI/Heroes/Pink_Monster.png", "Assets/GUI/Heroes/Pink_Monster_Hover.png", (725, 340))

		# Selecting Game Character
		Utility.LogMessage("Initializing character choosing menu...", "LOADINGINFO")
		if GAME.current_character == "Dude_Monster.png":
			Ch_Nao.selected = True
		elif GAME.current_character == "Owlet_Monster.png":
			Ch_Tao.selected = True
		elif GAME.current_character == "Pink_Monster.png":
			Ch_Geo.selected = True
		else:
			Ch_Nao.selected = True

		# The Global loop of the Game, contains every input loop.
		Utility.LogMessage("Initializing main game", "LOADINGINFO")
		Loop_global = True

		# The 2 Sub-loops of the Game, for Play screen and "Game Over" Screen
		Loop_run = False
		Loop_gameover = False
		Loop_menu = True
		Loop_Credits = False
		Loop_Options = False
		Loop_Pause = False
		Loop_PauseOptions = False

		# Stops game Loading to prevent infinite loading loop
		GameLoaded = True

# Deletes loading window
del LOADINGWINDOW
del intro

# Creating Window with possibility to change resolution
Utility.LogMessage("Initializing game window...", "LOADINGINFO")
Main_Window = pygame.display.set_mode((928, 557), pygame.RESIZABLE)
WINDOW = pygame.Surface([928, 557])

# Universal function to resize frame and draw it
def draw():

	# Defines a scale coefficient between the original image and the window size
	coefficient = Main_Window.get_width() / 928

	# If the height of the frame > the height of the window, then it will use the coefficient based on the height
	if round(557 * coefficient) > Main_Window.get_height():
		coefficient = Main_Window.get_height() / 557

	# And scale the window to it
	frame = pygame.transform.scale(WINDOW, (round(928 * coefficient), round(557 * coefficient)))

	# Centers x and y the window
	PosCenterX = Main_Window.get_width() / 2 - round(928 * coefficient) / 2
	PosCenterY = Main_Window.get_height() / 2 - round(557 * coefficient) / 2

	# And finally draws the window
	Main_Window.blit(frame, (PosCenterX, PosCenterY))
	CLOCK.tick(FPS)
	pygame.display.flip()

# The Window will be named like this :
pygame.display.set_caption("Nao's Universe: Endless Run")
# Importing and setting window icon : "icon.png"
pygame.display.set_icon(pygame.image.load("icon.png"))

# Start menu music
if GAME.options["play_music"] is True:
	Utility.LogMessage("Starting music...", "LOADINGINFO")
	pygame.mixer_music.load("Assets/Sound/menu.ogg")
	pygame.mixer_music.play(loops=-1)
else:
	Utility.LogMessage("Music is disabled, ignoring.", "LOADINGINFO")

Utility.LogMessage("Loading Complete", "INFO")

# Hide the Mouse cursor
pygame.mouse.set_visible(False)

# The game starts Here
while Loop_global:


	# The loop for the menu screen
	while Loop_menu:
	
	
		Ch_Nao.check_selected()
		Ch_Tao.check_selected()
		Ch_Geo.check_selected()

		# Clear the screen before doing anything
		WINDOW.fill((0, 0, 0))

		# Paste the background
		WINDOW.blit(Background_menu, (0, 0))

		# Paste the title
		WINDOW.blit(Title, (130, 50))

		# HighScore

		WINDOW.blit(Text2, (452, 200))

		WINDOW.blit(HighScoreIndicatorImage, (460, 255))

		HighScoreIndicator = FONT.render("Record : " + str(GAME.highscore), True, (255, 255, 255))
		WINDOW.blit(HighScoreIndicator, (490, 250))

		# Character choice menu
		WINDOW.blit(Text1, (450, 285))
		WINDOW.blit(Ch_Nao.image, Ch_Nao.rect)
		WINDOW.blit(Ch_Tao.image, Ch_Tao.rect)
		WINDOW.blit(Ch_Geo.image, Ch_Geo.rect)

		# Paste the Buttons
		WINDOW.blit(Button_Play.image, Button_Play.rect)
		WINDOW.blit(Button_Settings.image, Button_Settings.rect)
		WINDOW.blit(Button_Credits.image, Button_Credits.rect)

		# Place the cursor
		WINDOW.blit(Cursor, Cursor_Rect)

		draw()


		for event in pygame.event.get():

			
			# If the player moves his mouse
			if event.type == pygame.MOUSEMOTION:
				Cursor_Rect.x = event.pos[0]
				Cursor_Rect.y = event.pos[1]
				

				Button_Play.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Button_Settings.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Button_Credits.check_mouse([Cursor_Rect.x, Cursor_Rect.y])

				Ch_Nao.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Ch_Tao.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Ch_Geo.check_mouse([Cursor_Rect.x, Cursor_Rect.y])

			

			# If the player clicks on the screen
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:

				if Button_Play.is_hover:

					# Play button sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Button_Play.sound().play()

					# The three characters have pros and cons

					# Nao can jump high, but is slow
					# Tao can double jump
					# Geo is fast, but jumps less

					# If geo is selected :
					# Slide velocity for Backgrounds is set to 3 px/frame (2 when controlling Nao and Tao)
					# Move velocity for objects is set to 3 px/frame (2 when controlling Nao and Tao)
					# Jump modifier is reducted by 10% (the normal value is x0.05)

					if Ch_Geo.selected:

						Background1.slide_velocity = 3
						Background2.slide_velocity = 3
						GAME.speed = 3

						GAME.player.jump_modifier = 0.045

					# If Nao is selected
					# Jump modifier is increased by 10% (the normal value is x0.05)
					elif Ch_Nao.selected:

						# Nao is slower than Geo, and his speed is 2px/frame
						Background1.slide_velocity = 2
						Background2.slide_velocity = 2
						GAME.speed = 2

						GAME.player.jump_modifier = 0.055

					# If Tao is selected
					# The double-jump isn't enabled at this place
					# Tao has a speed of 2px/frame and 100% jump modifier (x0.05)

					else:
						Background1.slide_velocity = 2
						Background2.slide_velocity = 2
						GAME.speed = 2

						GAME.player.jump_modifier = 0.05

					# Replace backgrounds at their origin place
					Background1.return_to_origin()
					Background2.return_to_origin()

					# Re-enable death sound
					GAME.player.played_death_sound = False
					
					# Re-enable Pause
					GAME.can_pause = True

					# Stop music if it was played
					if GAME.options["play_music"] is True:
						pygame.mixer_music.stop()

					# Start game music if music is enabled
					# Chosen randomly
					if GAME.options["play_music"] is True:
						pygame.mixer_music.load(GAME.choose_music(MUSICS))
						pygame.mixer_music.play(loops=-1)

					# Reload Character animation
					GAME.player.reload_frames()

					# Start the Game
					Loop_menu = False
					Loop_run = True

				if Button_Settings.is_hover:

					# Play button sound if sfx is enabled in game options
					if GAME.options["play_sfx"] is True:
						Button_Settings.sound().play()

					Loop_menu = False
					Loop_Options = True


				elif Button_Credits.is_hover:

					# Play button sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Button_Credits.sound().play()

					# Stop menu loop
					Loop_menu = False
					Loop_Credits = True

					# Enable credits scrolling
					Credits.return_to_origin()
					Credits.do_slide = True

					# Stop current music
					pygame.mixer_music.stop()

					# Choose a game music and play it if music is active
					if GAME.options["play_music"] is True:
						pygame.mixer_music.load(GAME.choose_music(MUSICS))
						pygame.mixer_music.play(loops=-1)

				# Character selection menu input

				# If Nao character is chosen
				elif Ch_Nao.is_hover:

					# Play select sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Ch_Nao.sound().play()

					# Select Nao
					# Unselect Tao or Geo
					Ch_Tao.selected = False
					Ch_Geo.selected = False
					Ch_Nao.selected = True

					# Set the current character to Owlet_Monster
					# The name is the filename to the default image

					# This image is loaded if other frames can't be loaded
					GAME.current_character = "Dude_Monster.png"

					# This is the path to the character images folder
					GAME.current_character_path = "Assets/Heroes/Dude_Monster/"

				# Exactly same thing with Tao
				elif Ch_Tao.is_hover:

					# Play select sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Ch_Tao.sound().play()

					# Select Tao
					# Unselect Nao or Geo
					Ch_Nao.selected = False
					Ch_Geo.selected = False
					Ch_Tao.selected = True

					# Set the current character to Owlet_Monster
					GAME.current_character = "Owlet_Monster.png"
					GAME.current_character_path = "Assets/Heroes/Owlet_Monster/"

				elif Ch_Geo.is_hover:

					# Same process for Geo choice here

					if GAME.options["play_sfx"] is True:
						Ch_Geo.sound().play()

					Ch_Nao.selected = False
					Ch_Tao.selected = False
					Ch_Geo.selected = True

					GAME.current_character = "Pink_Monster.png"
					GAME.current_character_path = "Assets/Heroes/Pink_Monster/"

			# If the player needs to quit the game
			elif event.type == pygame.QUIT:

				# Save Progress
				GAME.Save()

				Loop_menu = False
				Loop_global = False
				pygame.quit()

				sys.exit()


	# When Options are activated
	while Loop_Options:


		Checkbox_Music.update_image()
		Checkbox_Sfx.update_image()
		Checkbox_Showfps.update_image()


		WINDOW.fill((0, 0, 0))

		WINDOW.blit(Background_menu, (0, 0))

		WINDOW.blit(Button_Options_Back.image, Button_Options_Back.rect)
		WINDOW.blit(Options_Title, (75, 15))

		WINDOW.blit(Options_Text, (0, 0))

		WINDOW.blit(Checkbox_Music.image, Checkbox_Music.rect)
		WINDOW.blit(Checkbox_Sfx.image, Checkbox_Sfx.rect)
		WINDOW.blit(Checkbox_Showfps.image, Checkbox_Showfps.rect)

		WINDOW.blit(Slider_difficulty.image, Slider_difficulty.rect)

		# Place the cursor
		WINDOW.blit(Cursor, Cursor_Rect)


		draw()



		for event in pygame.event.get():

			if event.type == pygame.MOUSEMOTION:
				Cursor_Rect.x = event.pos[0]
				Cursor_Rect.y = event.pos[1]


				Button_Options_Back.check_mouse([Cursor_Rect.x, Cursor_Rect.y])

				Checkbox_Music.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Checkbox_Sfx.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Checkbox_Showfps.check_mouse([Cursor_Rect.x, Cursor_Rect.y])

				Slider_difficulty.check_hover([Cursor_Rect.x, Cursor_Rect.y])


			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:

				if Slider_difficulty.hover:

					Slider_difficulty.on_click()

					# Play button sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Button_Options_Back.sound().play()

					# Button Function
					if Slider_difficulty.position == 1:
						GAME.options["difficulty"] = "easy"

					elif Slider_difficulty.position == 2:
						GAME.options["difficulty"] = "normal"

					elif Slider_difficulty.position == 3:
						GAME.options["difficulty"] = "hard"

					GAME.reload_difficulty()
					Utility.LogMessage("Changed difficulty to " + GAME.options["difficulty"], "INFO")

				if Button_Options_Back.is_hover:

					# Play button sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Button_Options_Back.sound().play()

					Loop_Options = False
					Loop_menu = True

				elif Checkbox_Music.is_hover:

					# Change state (see in class for details)
					Checkbox_Music.change_state()

					# Play a sound is sfx is enabled
					if GAME.options["play_sfx"] is True:
						Checkbox_Music.play_sound().play()
				
					# Action related to Music
					if Checkbox_Music.state is True:
						GAME.options["play_music"] = True
						Utility.LogMessage("Enabled Music", "INFO")

						# Restart the music
						Utility.LogMessage("Restarting music...", "INFO")
						pygame.mixer_music.load("Assets/Sound/menu.ogg")
						pygame.mixer_music.play(loops=-1)


					else:
						GAME.options["play_music"] = False
						Utility.LogMessage("Disabled Music", "INFO")

						# Stop the music
						Utility.LogMessage("Stopping Music...", "INFO")
						pygame.mixer_music.stop()

				elif Checkbox_Sfx.is_hover:

					Checkbox_Sfx.change_state()

					if GAME.options["play_sfx"] is True:
						Checkbox_Sfx.play_sound().play()

					# Action related to this checkbox
					if Checkbox_Sfx.state is True:
						GAME.options["play_sfx"] = True
						Utility.LogMessage("Enabled SFX", "INFO")


					else:
						GAME.options["play_sfx"] = False
						Utility.LogMessage("Disabled SFX", "INFO")

				elif Checkbox_Showfps.is_hover:

					Checkbox_Showfps.change_state()

					if GAME.options["play_sfx"] is True:
						Checkbox_Showfps.play_sound().play()

					# Action related to this checkbox
					if Checkbox_Showfps.state is True:
						GAME.options["show_fps"] = True
						Utility.LogMessage("Enabled ShowFPS", "INFO")


					else:
						GAME.options["show_fps"] = False
						Utility.LogMessage("Disabled ShowFPS", "INFO")


			elif event.type == pygame.QUIT:
				GAME.Save()

				Loop_Options = False
				Loop_global = False

				pygame.quit()
				sys.exit()

	# When Credits are activated
	while Loop_Credits:


		# Fill window with black color
		WINDOW.fill((0, 0, 0))

		# Paste background image
		WINDOW.blit(Background_menu, (0, 0))

		# Move credits image
		Credits.slide_vertical()

		# Paste credits image
		WINDOW.blit(Credits.background, Credits.rect)

		# Optimization stuff
		draw()

		# Event stuff
		for event in pygame.event.get():

			# If the player presses any key
			if event.type == pygame.KEYDOWN:

				# Get back to menu
				Loop_Credits = False
				Loop_menu = True

				# Play select sound if sfx is enabled
				if GAME.options["play_sfx"] is True:
					pygame.mixer.Sound("Assets/Sound/select1.ogg")

				# Stop current music (if music has played)
				if GAME.options["play_music"] is True:
					pygame.mixer_music.stop()

				# Load and play menu music if music is enabled
				if GAME.options["play_music"] is True:
					pygame.mixer_music.load("Assets/Sound/menu.ogg")
					pygame.mixer_music.play(loops=-1)

			# If player closes the window
			elif event.type == pygame.QUIT:

				# Save progress
				GAME.Save()

				# Stop every active loop of the game
				Loop_Credits = False
				Loop_global = False

				# Unload pygame librairies
				pygame.quit()
				sys.exit()

	# Main loop of the game
	while Loop_run:

		# Blits the surface

		while Loop_Pause:

			# Blits the surface

			# Fills the window with Black color every frame
			WINDOW.fill((0, 0, 0))

			# Place the background image
			WINDOW.	blit(Background1.background, Background1.rect)
			WINDOW.blit(Background2.background, Background2.rect)

			# Paste score indicators
			WINDOW.blit(ScoreIndicatorImage, (5, 10))

			ScoreIndicator = FONT.render(str(GAME.score), True, (255, 255, 255))
			WINDOW.blit(ScoreIndicator, (35, 5))

			# Paste title
			WINDOW.blit(Pause_Title, (214, 75))

			# Paste buttons
			WINDOW.blit(Pause_Button_Quit.image, Pause_Button_Quit.rect)
			WINDOW.blit(Pause_Button_Resume.image, Pause_Button_Resume.rect)

			# Place the cursor
			WINDOW.blit(Cursor, Cursor_Rect)

			# Scaling and refreshing
			draw()


			# Events
			for event in pygame.event.get():

				# If the player attemps to quit the Game
				if event.type == pygame.QUIT:

					# Save Progress
					GAME.Save()

					# Stops all the loops in the Game
					Loop_run = False
					Loop_global = False
					# Unloads pygame libraries.
					pygame.quit()
					sys.exit()

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

					# Exit Pause Loop and get back to main game
					Loop_Pause = False

					# Play button sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Pause_Button_Quit.sound().play()

				elif event.type == pygame.MOUSEMOTION:
					Cursor_Rect.x = event.pos[0]
					Cursor_Rect.y = event.pos[1]

					Pause_Button_Quit.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
					Pause_Button_Resume.check_mouse([Cursor_Rect.x, Cursor_Rect.y])

				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:

					if Pause_Button_Quit.is_hover:

						# Play button sound if sfx is enabled
						if GAME.options["play_sfx"] is True:
							Pause_Button_Quit.sound().play()

						# Play menu music if music is enabled in options
						if GAME.options["play_music"] is True:
							pygame.mixer_music.load("Assets/Sound/menu.ogg")
							pygame.mixer_music.play(loops=-1)

						
						# Make backgrounds slide
						Background1.do_slide = True
						Background2.do_slide = True

						# Delete every object
						for piece in GAME.pieces:
							piece.can_goleft = False
							piece.remove()

						for crate in GAME.crates:
							crate.can_goleft = False
							crate.remove()

						# If score > highscore, then create a new highscore
						if GAME.score > GAME.highscore:
							GAME.highscore = GAME.score
						
						# Erase the score
						GAME.score = 0

						Loop_run = False
						Loop_Pause = False
						Loop_menu = True

					elif Pause_Button_Resume.is_hover:

						# Play button sound if sfx is enabled
						if GAME.options["play_sfx"] is True:
							Button_Play.sound().play()

						# Exit pause loop and get back to game run
						Loop_Pause = False


		# Fills the Windows with Black every frame
		WINDOW.fill((0, 0, 0))

		# Check if the player is dead
		# If true, it will stop background scrolling
		if GAME.player.is_dead:
			Background1.do_slide = False
			Background2.do_slide = False

			GAME.can_pause = False

			# Stop music if it was played
			if GAME.options["play_music"] is True:
				pygame.mixer_music.stop()

			# If the death sound hasn't played yet and sfx is enabled
			if GAME.player.played_death_sound is False and GAME.options["play_sfx"] is True:


				# Play death sound (obviously)
				GAME.player.death_sound.play()

				# Disable death sound
				GAME.player.played_death_sound = True

				

			

		# Background scrolling stuff
		Background1.slide_horizontal()
		Background2.slide_horizontal()
		# Crates are generated when a random number, generated every frame, comes to a certain position
		GAME.try_generate_crate()
		GAME.try_generate_piece()

		# Player animation is Manual. The Game will import image at every frame and apply it to player's Image.
		GAME.player.next_frame()

		# Simply pastes Backgrounds images on the screen
		WINDOW.	blit(Background1.background, Background1.rect)
		WINDOW.blit(Background2.background, Background2.rect)

		WINDOW.blit(ScoreIndicatorImage, (5, 10))

		ScoreIndicator = FONT.render(str(GAME.score), True, (255, 255, 255))
		WINDOW.blit(ScoreIndicator, (35, 5))

		if GAME.options["show_fps"] is True:
			FPS_IMG = FONT.render(str(round(CLOCK.get_fps(), 1)), True, (255, 255, 255))
			WINDOW.blit(FPS_IMG, (820, 5))

		# Action to do for every crate in the game
		for crate in GAME.crates:
			# Make crates go left on the screen at 2px/s speed
			crate.go_left()

		# Draws every crate present on the screen
		GAME.crates.draw(WINDOW)

		# Same thing for pieces
		for piece in GAME.pieces:
			piece.go_left()
			piece.animate()

		GAME.pieces.draw(WINDOW)

		# Pastes player's image on the screen
		WINDOW.blit(GAME.player.image, GAME.player.rect)

		# Optimization stuff, regulates FPS
		draw()

		# Event listening stuff
		for event in pygame.event.get():

			# If the player attemps to quit the Game
			if event.type == pygame.QUIT:

				# Save Progress
				GAME.Save()

				# Stops all the loops in the Game
				Loop_run = False
				Loop_global = False
				# Unloads pygame libraries.
				pygame.quit()
				sys.exit()

			# If the player hits "ESC" key
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

				# If player can pause
				if GAME.can_pause:

				# Play button sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						Pause_Button_Quit.sound().play()

					# Enter the pause loop
					Loop_Pause = True

			# If the player press "SPACE" key
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
				# (PHYSICS) If the player is running
				if GAME.player.is_run:
					# (PHYSICS) Re-initialises Jump
					GAME.player.jump_count = 12
					
					# Play jump sound if sfx is enabled
					if GAME.options["play_sfx"] is True:
						GAME.player.jump_sound.play()

					# (PHYSICS) Prepares for jumping
					GAME.player.is_jump = True
					GAME.player.is_onground = False
					GAME.player.is_onbox = False
					GAME.player.is_run = False

				# The doublejump phase, enabled only if Tao is selected and if it hasn't executed yet
				elif GAME.player.is_jump or GAME.player.is_fall:
					if Ch_Tao.selected is True and GAME.player.doublejump is False:

						# Disable doublejump while the player hasn't landed
						GAME.player.doublejump = True

						# Re-initialize jump
						GAME.player.jump_count = 12
						GAME.player.fall_count = 0

						# replay jump sound if sfx is enabled
						if GAME.options["play_sfx"] is True:
							GAME.player.jump_sound.play()

						# Refresh player state
						GAME.player.is_jump = True
						GAME.player.is_onground = False
						GAME.player.is_onbox = False
						GAME.player.is_run = False

		# (PHYSICS) If the player is jumping
		if GAME.player.is_jump:

			GAME.play_step_sound = False

			# If the jump count, that decreases from 12 isn't at 0
			if GAME.player.jump_count >= 0:

				# Moves the player and decreases the Jump count (-0.5)
				GAME.player.rect.y -= (GAME.player.jump_count * abs(GAME.player.jump_count)) * GAME.player.jump_modifier
				GAME.player.jump_count -= 0.5

			# If the player's jump count is at 0
			else:
				# Initialising falling phase
				GAME.player.is_jump = False
				GAME.player.is_fall = True

		# If the player is falling
		elif GAME.player.is_fall:

			GAME.play_step_sound = False

			# If the player is on a surface (falling phase ending)
			if GAME.player.is_onbox or GAME.player.is_onground:
				# Resets Fall count value
				GAME.player.fall_count = 0

				# Player will now do the running animation
				GAME.player.is_fall = False
				GAME.player.is_run = True

				GAME.player.doublejump = False

				# Play the sound if sfx is enabled
				if GAME.options["play_sfx"] is True:
					GAME.player.Ground_Sound("groundsound").play()

			# If the player is still falling
			else:
				GAME.player.rect.y += (GAME.player.fall_count * abs(GAME.player.fall_count)) * 0.05
				GAME.player.fall_count += 0.5

				# If player's feets Y pos are under the ground level
				if GAME.player.rect.y + GAME.player.rect.height >= GAME.ground_level:
					# Will automaticly make the player on the ground
					GAME.player.is_onground = True
					# And replace it at the ground level
					GAME.player.rect.y = GAME.ground_level - GAME.player.rect.height
					# Ground sound

		# If the game ended (Game Over case)
		if not GAME.game:
			Loop_run = False
			Loop_gameover = True

			# Start game over screen music if enabled
			if GAME.options["play_music"] is True:
				pygame.mixer_music.load("Assets/Sound/music_gameover.ogg")
				pygame.mixer_music.play(loops=-1)


	# The loop for game over screen
	while Loop_gameover:

		# Clears all the window
		WINDOW.fill((0, 0, 0))

		# Pastes Background image on the screen
		WINDOW.blit(Background_death, (0, 0))



		# Score Indicator
		ScoreIndicator = FONT.render(str(GAME.score), True, (255, 255, 255))
		WINDOW.blit(ScoreIndicator, (207, 517))

		# Buttons
		WINDOW.blit(Gameover_Backmenu.image, Gameover_Backmenu.rect)
		WINDOW.blit(Gameover_Tryagain.image, Gameover_Tryagain.rect)

		# Paste the cursor image on the screen
		WINDOW.blit(Cursor, Cursor_Rect)

		# Optimization stuff, FPS regulating stuff
		draw()

		# Input listening stuff
		for event in pygame.event.get():

			# If the player attemps to quit the game
			if event.type == pygame.QUIT:

				# Save progress
				GAME.Save()

				# Will stop every loop of the game
				# And unload pygame library
				Loop_gameover = False
				Loop_global = False
				pygame.quit()
				sys.exit()

			# If the player moves his mouse

			elif event.type == pygame.MOUSEMOTION:

				Cursor_Rect.x = event.pos[0]
				Cursor_Rect.y = event.pos[1]

				Gameover_Backmenu.check_mouse([Cursor_Rect.x, Cursor_Rect.y])
				Gameover_Tryagain.check_mouse([Cursor_Rect.x, Cursor_Rect.y])

			# If the player presses the left button of his mouse
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:

				# If the mouse is pointed on The "Back to Menu" button
				if Gameover_Backmenu.is_hover:

					# Play SFX if sound is enabled
					if GAME.options["play_sfx"] is True:
						Gameover_Backmenu.sound().play()
	
					# Re-initialize game, with Background scrolling stuff, Physics, and Animation utility stuff
					Background1.do_slide = True
					Background2.do_slide = True



					GAME.score = 0

					GAME.player.is_dead = False
					GAME.player.is_run = True
					GAME.player.max_frame_skip = 3
					GAME.player.current_death_frame = 0
					GAME.game = True
					GAME.do_spawn_crates = True
					GAME.do_generate_pieces = True

	

					# Play menu music if music is enabled in options
					if GAME.options["play_music"] is True:
						pygame.mixer_music.load("Assets/Sound/menu.ogg")
						pygame.mixer_music.play(loops=-1)

					# Go to menu
					Loop_gameover = False
					Loop_menu = True

				# Else, if the mouse is pointed on the "Try Again" button
				elif Gameover_Tryagain.is_hover:

					# Play button sfx if enabled
					if GAME.options["play_sfx"] is True:
						Gameover_Tryagain.sound().play()

					# Re-initialize game, with Background scrolling stuff, Physics, and Animation utility stuff
					Background1.do_slide = True
					Background2.do_slide = True

					GAME.score = 0

					GAME.player.is_dead = False
					GAME.player.is_run = True
					GAME.player.max_frame_skip = 3
					GAME.player.current_death_frame = 0
					GAME.game = True
					GAME.do_spawn_crates = True
					GAME.do_generate_pieces = True

					# Replace background to origin
					Background1.return_to_origin()
					Background2.return_to_origin()

					# Re-enable death sound
					GAME.player.played_death_sound = False

					# Re-enable pause menu
					GAME.can_pause = True

					# Restart music if music is enabled in options
					if GAME.options["play_music"] is True:
						pygame.mixer_music.load(GAME.choose_music(MUSICS))
						pygame.mixer_music.play(loops=-1)

					# Restart game
					Loop_gameover = False
					Loop_run = True



					


# Code ends here
