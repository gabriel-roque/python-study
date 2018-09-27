from pygame import mixer
mixer.init()
mixer.music.load('desafio21_music.mp3')
mixer.music.set_volume(0.1)
mixer.music.play()