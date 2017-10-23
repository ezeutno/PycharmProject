class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.high_score = int(open('Data_base\\data.txt', 'r').read())
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.level = 1

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0

    def update_highscore(self):
        open('Data_base\\data.txt', 'w').write(str(self.high_score))