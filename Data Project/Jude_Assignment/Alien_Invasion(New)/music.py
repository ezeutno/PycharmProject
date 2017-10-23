import pygame

class Music():
    def __init__(self,music_path,vol,str):
        self.music_path = music_path
        self.vol = vol
        self.str = str

    def effect(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(self.vol)
        pygame.mixer.music.play(loops=0, start=self.str)

