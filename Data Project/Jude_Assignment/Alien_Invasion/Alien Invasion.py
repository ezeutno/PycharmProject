import sys
import pygame
from Setting import Setting
from Ship import Ship

def run_game():
    #pyGame initiations
    pygame.init()
    #setting base on OOP << back to Setting Class
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    ship = Ship(screen)
    #display in windows bar
    pygame.display.set_caption("Alien_game")

    while True:
        #check every event
        for event in pygame.event.get():
            #to quit via x mark
            if event.type == pygame.QUIT:
                sys.exit()
        #to fill the screen with color
        screen.fill(setting.bg_color)
        ship.blitme()
        #for renewing your screen
        pygame.display.flip()

run_game()
