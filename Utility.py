import pygame, time, pickle
# Additional stuff

# Logfile, printed at exit in the latest log file
# It is simply a list
logfile =  []

# The "Video" Class :
# Following of images called with a number (from anything to anything) and placed in the same folder
# The folder also needs an audio file, a .ogg containing sound of the video (leave False if no audio)

# If the video is too slow or fast, adapt with frame skipping (already implemented) and fps using
# pygame.time.Clock() Class and its tick() method
class Video:

    def __init__(self, folder, range_min, range_max, skip, prefix, audio):

        # The folder where the video is placed
        self.folder = folder

        # The name (without file extension) of the first image (SHOULD BE A NUBER)
        try:
            self.min = int(range_min)
            self.max = int(range_max)
        except TypeError:
            CrashLog("FATAL ERROR WHILE LOADING VIDEO FRAMES \n Min and Max should be integers numbers, got type", type(range_min), "and", type(range_max))

        # Prefix, if filenames contains prefixes like "video_" or "img-".
        # Leave blank ("") if there's no prefix
        self.prefix = prefix

        # The current image that will be pasted on the screen with blit() method
        self.image = pygame.image.load(self.folder + self.prefix + str(self.min) + ".jpg")

        # The audio file that should be here
        if audio is False:
            self.audio = None
        else:
            try:
                self.audio = pygame.mixer.Sound(audio)
            except:
                CrashLog("FATAL ERROR\n Missing Video Sound not told. Please consider using False if no audio")

        # The number of animation frames that would be skipped
        self.skip = skip

        # The current frame, that is defined by the min of the range at the start
        self.current_frame = self.min

        # Times video played in the execution
        self.playedtimes = 0

        # Skip counter, counts how frames would be skipped
        self.skip_counter = 0

        self.play = False
        self.finished = False

    # At each frame in the main game
    def next_frame(self):

        if self.play:
            self.finished = False
            if self.current_frame <= self.max:
                if self.current_frame >= self.min:

                    if self.skip_counter == self.skip:

                        self.image = pygame.image.load(self.folder + self.prefix + str(self.current_frame) + ".jpg")

                        self.current_frame += 1

                        self.skip_counter = 0

                    else:
                        self.skip_counter += 1

            else:
                self.play = False
                self.playedtimes += 1
                self.finished = True
                self.current_frame = self.min

# Imports settings from a specific text file
"""def ImportSettings(file):

    # Starts by opening a specific file in read mode
    # And creating a local options dict object
    open_file = open(file, "r")
    options = {}

    # For every line in the file
    for line in open_file:

        l = line.split("=")

        # Will cut the line at the "=" symbol
        options[l[0]] = l[1]
        # Then we have the value before "=" that is the key in the dict
        # And the value after that is the value assigned to the key

        # If there is a line-return character
        # It will be erased
        # (Can Cause problems)

        if options[l[0]][-1] == "\n":
            options[l[0]] = options[l[0]][:-1]

    # Don't forget to close the file (Save memory)
    open_file.close()

    print(options)

    # And returns the options
    return options
"""
# Creates crashlog and saves the error cause
def CrashLog(message):

    # Filename creating
    date = time.localtime()

    # Filename will appear like "CRASHLOG_2020_16_08_20:43:57.txt"
    filename = "CRASHLOG_" + str(date.tm_year) + "_" + str(date.tm_mon) + "_" + str(date.tm_mday) + "_" + str(date.tm_hour) + ":" + str(date.tm_min) + ":" + str(date.tm_sec) + ".txt"

    # File creating
    file = open(filename, "w+")

    # File content
    genericmessage = "CrashLog is'nt log of everything. Just description of the error that made the game crash. \n \n"

    file.write(genericmessage + message)

    # Close file and deletes everything
    file.close()
    del date, filename, file, genericmessage

    # Quits the game
    quit()

def Save(data, filename):

    file = open(filename, "wb")

    pickle.dump(data, file)

    file.close()

def Load(filename):

    file = open(filename, "rb")

    data = pickle.load(file)

    file.close()

    return data


def LogMessage(message, messagetype):

    # To know exactly what happened in a log, time is printed

    log_time_structure = time.localtime()
    log_time = str(log_time_structure.tm_mon) + "." + str(log_time_structure.tm_mday) + "." + str(log_time_structure.tm_year) + " " + str(log_time_structure.tm_hour) + ":" + str(log_time_structure.tm_min) + ":" + str(log_time_structure.tm_sec)

    # Delete the struct_time object
    del log_time_structure

    log_message = "[" + log_time + "] " + messagetype + " | " + message

    # Add the message to the log list
    logfile.append(log_message)

    # Print the message in the terminal (if open)
    print(log_message)



