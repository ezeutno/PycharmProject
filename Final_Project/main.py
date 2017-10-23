import pygame
import game_fuction as gf
from settings import Settings as ai_settings

def main():
    pygame.init()
    set = ai_settings()
    screen = pygame.display.set_mode((set.screen_width,set.screen_height))
    pygame.display.set_caption(set.caption)
    while True:
        gf.check_event()
        gf.update_screen(screen,set)

main()