from pygame import mixer
from time import sleep

def play_alert(sound_file):
    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()
    sleep(10)
    mixer.music.stop()
