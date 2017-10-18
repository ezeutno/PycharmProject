import pygame
from setting import Settings
import rocket
import game_fuction as gf

def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Rocket Moving')
    Rocket = rocket.Rocket(ai_settings,screen)

    while True:
        gf.check_event(Rocket)
        Rocket.update()
        gf.update_screen(ai_settings,screen,[Rocket])

main()

