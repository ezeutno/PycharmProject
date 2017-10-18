import sys
import pygame
from star import Star
from random import randint

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, stars):
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()


def create_star(ai_settings, screen, stars):
    star = Star(ai_settings,screen)
    star.rect.x = randint(0,ai_settings.screen_width)
    star.rect.y = randint(0,ai_settings.screen_height)
    stars.add(star)

def create_multilayer_star(ai_setting, screen, stars):
    number_star = randint(25,50)
    for star_number in range(number_star):
        create_star(ai_setting,screen,stars)
