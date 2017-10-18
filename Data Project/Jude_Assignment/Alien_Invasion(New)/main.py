import pygame
from pygame.sprite import Group
#from pygame.locals import *
from Setting import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from Ship import Ship
from moon import Moon
from earth import Earth
from button import Button
import game_function as gf

def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#,RESIZABLE)
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    moon = Moon(ai_settings,screen)
    earth = Earth(ai_settings,screen)
    stars = Group()
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    gf.create_multilayer_star(ai_settings, screen, stars)

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats, sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb, screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,stars,sb,[moon,earth],[ship],play_button,aliens,bullets)

main()