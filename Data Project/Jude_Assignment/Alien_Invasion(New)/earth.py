import pygame

class Earth():
    def __init__ (self,ai_setting,screen):
        self.screen = screen
        self.ai_setting = ai_setting
        x = self.ai_setting
        self.image = pygame.image.load('Data_base\\earth.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)