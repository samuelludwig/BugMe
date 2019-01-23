import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import traceback
from time import sleep

from pygame import mixer


def play_alert(sound_file):
    """To be triggered by watch when overdue task encountered
    
    Plays the selected sound file (for 10 seconds) if it is of proper format (.mp3), else should return
    an error.
    """
    try:
        mixer.init()
        mixer.music.load(sound_file)    # <- ISSUE SOURCE
        mixer.music.play()
        sleep(10)
        mixer.music.stop()
    except:
        print(sys.exc_info())

"""NOTE: What I'm guessing is that spawning of the process in controller makes an interpreter that 
    for some reason cant find the sound file due to the relative pathing, will test it later when I find the time.
"""