import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            print(str(event.type))
            return str(event.type)


def update_screen(ai_settings, screen, thing):
    screen.fill(ai_settings.bg_color)
    for i in thing:
        i.blitme()
    pygame.display.flip()