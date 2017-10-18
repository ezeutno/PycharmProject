import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, bg_obj,fr_obj,bullets):
    screen.fill(ai_settings.bg_color)
    for i in bg_obj:
        i.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for i in fr_obj:
        i.blitme()
    pygame.display.flip()

def update_bullets(bullets,screen_rect):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)