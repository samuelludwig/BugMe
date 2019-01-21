import traceback
from sys import exc_info
from time import sleep

from pygame import mixer


def play_alert(sound_file):
    """To be triggered by watch when overdue task encountered
    
    Plays the selected sound file (for 10 seconds) if it is of proper format (.mp3), else should return
    an error.
    """
    try:
        mixer.init()
        mixer.music.load(sound_file)
        mixer.music.play()
        sleep(10)
        mixer.music.stop()
    except:
        print(exc_info())
