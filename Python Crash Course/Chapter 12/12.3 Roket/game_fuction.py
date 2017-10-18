import sys
import pygame

def check_keydown_event(event,rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True


def check_keyup_event(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_event(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,rocket)

def update_screen(ai_settings, screen, thing):
    screen.fill(ai_settings.bg_color)
    for i in thing:
        i.blitme()
    pygame.display.flip()