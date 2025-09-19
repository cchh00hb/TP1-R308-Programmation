from point import Point

class Rectangle:
    def __init__(self, bas_gauche=None, longueur=1.0, hauteur=1.0, haut_droit=None):
        if haut_droit:
            self.bas_gauche = bas_gauche
            self.longueur = haut_droit.x - bas_gauche.x
            self.hauteur = haut_droit.y - bas_gauche.y
        else:
            self.bas_gauche = bas_gauche if bas_gauche else Point()
            self.longueur = longueur
            self.hauteur = hauteur

    def surface(self):
        return self.longueur * self.hauteur

    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    def position_bas_droite(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y)

    def position_haut_gauche(self):
        return Point(self.bas_gauche.x, self.bas_gauche.y + self.hauteur)

    def position_haut_droite(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y + self.hauteur)

    def contientPoint(self, point):
        return (self.bas_gauche.x <= point.x <= self.bas_gauche.x + self.longueur) and \
               (self.bas_gauche.y <= point.y <= self.bas_gauche.y + self.hauteur)


r1 = Rectangle(Point(0,0), 3, 2)
print("Rectangle : bas_gauche=({}, {}), longueur={}, hauteur={}".format(r1.bas_gauche.x, r1.bas_gauche.y, r1.longueur, r1.hauteur))
print("Surface du rectangle :", r1.surface())
print("Périmètre du rectangle :", r1.perimetre())
print("Le point (2,1) est dans le rectangle :", r1.contientPoint(Point(2, 1)))