import math
from typing import Self
from Point import Point

class Cercle :
    def __init__(self,rayon:float,centre: Point = none):
        self.__rayon = rayon
        if centre is not None:
            self.__centre = centre
        else :
            self.__centre = Point(0.0)

    @property
    def rayon(self) -> float :
        return self.__rayon

    @rayon.setter
    def rayon (self, rayon : float):
        self.__rayon = rayon,

    @property
    def centre (self) -> Point :
        return self.__centre

    @centre.setter
    def centre(self,centre:Point):
        self.__centre=centre

    def perimetre (self)->float:
        return self.__rayon*2

    def perimetre(self)-> float:
        return self.__rayon*2*math.py