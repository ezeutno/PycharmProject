import sys
import pygame
from star import Star

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, object):
    screen.fill(ai_settings.bg_color)
    object.draw(screen)
    pygame.display.flip()

def get_number_object_x(ai_settings, object_width):
    available_space_x = ai_settings.screen_width - (object_width+10)
    number_aliens_x = int(available_space_x / (object_width+10))
    return number_aliens_x

def get_number_object(ai_settings, object_width):
    available_space_x = ai_settings.screen_width
    number_of_rows = int(available_space_x/(object_width+10))
    return number_of_rows

def get_number_rows(ai_settings, object_height):
    available_space_y = ai_settings.screen_height
    number_of_rows = int(available_space_y/(object_height+10))
    return number_of_rows

def create_object(ai_settings, screen, stars, object_number, row_number):
    star = Star(ai_settings,screen)
    star_width = star.rect.width
    star.x = star_width + (star_width+10)*object_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + (star.rect.height+10)*row_number
    stars.add(star)

def create_multilayer(ai_setting, screen, stars):
    star = Star(ai_setting,screen)
    number_star_x = get_number_object_x(ai_setting,star.rect.width)
    number_rows = get_number_rows(ai_setting,star.rect.height)
    for row_number in range(number_rows):
        for star_number in range(number_star_x):
            create_object(ai_setting,screen,stars,star_number,row_number)
