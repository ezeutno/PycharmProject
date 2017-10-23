import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen,set):
    screen.fill(set.bg_color)
    pygame.display.flip()
