class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self,other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

# print(point1 == point2)
# print(point1 == point3)

###
p1=Point(1,2)
p2=Point(1,4)
if p1==p2:
    print('Odległość wynosi 0')
else:
    print(round(((((p2.x-p1.x)**2)+((p2.y-p1.y)**2))**(1/2)),2))