import math
class Circle:
    def __init__(self,radius,color):
        self.__radius = int(radius)
        self.__color = str(color)

    def getRadius(self):
        return self.__radius
    def setRadius(self, amt):
        self.__radius = amt
    def getColor(self):
        return self.__color
    def setColor(self, clr):
        self.__color = clr
    def toString(self):
        return "Circle[radius= {0}, color= {1}]".format(self.__radius,self.__color)
    def getArea(self):
        return math.pi*(Circle(self.__radius,self.__color).getRadius()** 2)