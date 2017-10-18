import pygame
import game_fuction as gf
from setting import Settings
from event_print import Display_print as Dp

def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Display Key')

    while True:
        Display = Dp(Settings(),screen,gf.check_event())
        Display.prep_text()
        Display.show_event()

main()