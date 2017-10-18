import pygame
from pygame.sprite import Group
from Setting import Settings
from Ship import Ship
from moon import Moon
import game_function as gf

def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    moon = Moon(ai_settings,screen)
    bullets = Group()


    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets,screen.get_rect())
        gf.update_screen(ai_settings,screen,[moon],[ship],bullets)

main()