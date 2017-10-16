from Jude_Assignment.Cylinder_Circle.Circle import Circle


class Cylinder(Circle):
    def __init__(self, height,radius,color):
        self.__height = height
        self.__radius = radius
        self.__color = color
        Circle.__init__(self, self.__radius, self.__color)

    def getHeight(self):
        return self.__height

    def setHeight(self, amt):
        self.__height = amt

    def toString(self):
        return 'Cylinder[radius= {0}, height= {1}, color= {2}]'.format(self.__height, Circle.getRadius(),
                                                                       Circle.getColor())

    def getVolume(self):
        return Circle.getArea(self)* self.__height
