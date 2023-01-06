import math
class x:
    @staticmethod
    def kolo(r):
        return round((math.pi*(r**2)),2)
    @staticmethod
    def trojkat(a,h):
        return round((1/2)*a*h)
    @staticmethod
    def prostokat(a,b):
        return (a*b)


print(x.kolo(3))
print(x.trojkat(6,2))
print(x.prostokat(4,7))