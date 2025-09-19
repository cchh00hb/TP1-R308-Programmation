import math
from point import Point


class Cercle:
    def __init__(self, rayon, centre=None):
        """Créer un cercle à l'origine ou avec un centre donné."""
        self.centre = centre if centre else Point()
        self.rayon = rayon

    def diametre(self):
        return 2 * self.rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def surface(self):
        return math.pi * self.rayon**2

    def intersection(self, autre_cercle):
        """Vrai si ce cercle croise l’autre."""
        distance = self.centre.distancePoint(autre_cercle.centre)
        return distance < (self.rayon + autre_cercle.rayon)

    def contientPoint(self, point):
        """Vrai si un point donné est dans le cercle."""
        return self.centre.distancePoint(point) <= self.rayon

c1 = Cercle(5)
c2 = Cercle(3, Point(3, 4))
print("Cercle 1 : centre={}, rayon={}".format((c1.centre.x, c1.centre.y), c1.rayon))
print("Cercle 2 : centre={}, rayon={}".format((c2.centre.x, c2.centre.y), c2.rayon))
print("Diamètre Cercle 1 :", c1.diametre())
print("Périmètre Cercle 1 :", c1.perimetre())
print("Surface Cercle 1 :", c1.surface())
print("Cercle 1 intersecte Cercle 2 :", c1.intersection(c2))
print("Le centre du cercle 2 est dans le cercle 1 :", c1.contientPoint(c2.centre))