import pygame
class Ship:
    def __init__(self, screen):
        self.screen = screen

        #load the ship image
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Now we want to create the ship on the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    #This fuction is used to draw the ship
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # this blit fuction is used to draw the image on the screen
