class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (21,41,55)

        #Ship Settings
        self.ship_limit = 5

        #moon Settings
        self.moon_x = int(self.screen_width * 0.25)
        self.moon_y = int(self.screen_height * 0.25)

        #Bullets Settings
        self.bullet_width = 5
        self.bullet_height = 8
        self.bullet_color = (178,34,34)

        #Star Settings
        self.percent_from_top = 1
        self.max_star = int(self.screen_width*2/10)
        self.min_star = int(self.screen_width/10)

        #Alien Settings
        self.fleet_drop_speed = 4

        #Dynamic Speed Settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.bullets_allowed = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullets_allowed = (self.bullets_allowed*1.2)
        self.alien_points = int(self.alien_points*self.score_scale)