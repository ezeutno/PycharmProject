import random
class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 700
        self.screen_height = 300
        self.bg_color = (21,41,55)

        #Ship Settings
        self.ship_speed_factor = 1.5

        #moon Settings
        self.moon_location_times = 0.85

        #Bullets Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3