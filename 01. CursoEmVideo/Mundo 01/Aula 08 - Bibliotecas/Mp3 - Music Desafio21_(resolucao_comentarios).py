import emoji
from pygame import *

mixer.init()
mixer.music.load('desafio21_music.ogg')
mixer.music.play()

print(emoji.emojize("Music is playing.... :musical_note:",use_aliases=True))
while mixer.music.get_busy():
    time.Clock().tick(10)