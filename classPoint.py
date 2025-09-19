import math
from typing import Self

class Point:
    def __init__(self, x= 0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __str__(self) :
        return f"Point : ({self.__x}, {self.__y})"

    def distancecoordonnees(self, x : float, y : float) :
        d : float = math.sqrt((self.__x - x)*(self.__x - x) + (self.__y - y)*(self.__y - y))

        return d
    def distancePoint(self, p : Self):
        d : float = math.sqrt((self.__x - p.__x)*(self.__x - p.__x) + (self.__y - p.__y)*(self.__y - p.__y))
        return d

class Point :
    def __ini__(self, x:float=0.0, y:float=0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self)->float :
        return self.__x

    @x.setter
    def x(self, x:float):
        self.__x=x

        if __name__ =="__main__":
            p1 : Point(3,5)
            print(p1.x)
            p1.x = 12
            print(p1.x)
            #print(p1.y)-->erreur
            #print(p1.__y)--erreur