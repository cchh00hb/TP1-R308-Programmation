import math
from typing import Self


class Cercle :
    def __init__(self,rayon:float,centre: Point = none):
        self.__rayon = rayon
        if centre is not None:
            self.__centre = centre
        else :
            self.__centre = Point(0.0)
