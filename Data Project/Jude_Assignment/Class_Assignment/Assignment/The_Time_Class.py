class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setHour(self, hour):
        self.hour = hour

    def setMinute(self, minute):
        self.minute = minute

    def setSecond(self, second):
        self.second = second

    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def toString(self):
        return "{0}:{1}:{2}".format(self.hour, self.minute, self.hour)

    def nextSecond(self):
        self.second += 1
        return self.second

    def previousSecond(self):
        self.second -= 1
        return self.second
