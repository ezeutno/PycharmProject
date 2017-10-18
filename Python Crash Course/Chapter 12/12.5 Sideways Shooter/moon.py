import pygame

class Moon():
    def __init__ (self,ai_setting,screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('Data_base\\moon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = (int(self.ai_setting.screen_width*ai_setting.moon_location_times),
                            int(self.ai_setting.screen_height*(1-ai_setting.moon_location_times)))

    def blitme(self):
        self.screen.blit(self.image, self.rect)