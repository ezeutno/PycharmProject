import pygame
from settings import Settings
from pygame.sprite import Group
import game_fuction as gf

def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Stars')
    stars = Group()
    gf.create_multilayer_star(ai_settings, screen, stars)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, stars)

main()