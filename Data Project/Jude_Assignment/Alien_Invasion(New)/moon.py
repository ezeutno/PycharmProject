import pygame

class Moon():
    def __init__ (self,ai_setting,screen):
        self.screen = screen
        self.ai_setting = ai_setting
        x = self.ai_setting
        self.image = pygame.image.load('Data_base\\moon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = (x.moon_x,x.moon_y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)