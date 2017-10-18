import pygame

class Display_print:
    def __init__(self,setting,screen,event):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.event = event

        self.text_color = (50,0,50)
        self.font = pygame.font.SysFont(None,50)

    def prep_text(self):
        self.text_display = self.font.render(self.event,True,self.text_color,self.setting.bg_color)
        self.text_rect = self.text_display.get_rect()
        self.text_rect.center = self.screen_rect.center


    def show_event(self):
        self.screen.blit(self.text_display,self.text_rect)