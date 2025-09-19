class Point:
    def __init__(self, x=0.0, y=0.0):
        """Constructeur du point. Par défaut à l'origine, ou spécifique."""
        self.x = x
        self.y = y

    def distanceCoord(self, a, b):
        """Calcule la distance avec un autre point donné par ses coordonnées."""
        return ((self.x - a)**2 + (self.y - b)**2)**0.5

    def distancePoint(self, autre_point):
        """Calcule la distance avec un autre point (instance Point)."""
        return ((self.x - autre_point.x)**2 + (self.y - autre_point.y)**2)**0.5

p1 = Point(1, 2)
p2 = Point(4, 6)
print("Point 1 :", p1.x, p1.y)
print("Point 2 :", p2.x, p2.y)
print("Distance entre points :", p1.distancePoint(p2))