import math
class Circle:
    __slots__ = ['__center', '__radius']
    
    def __init__(self,center,radius):
        self.__center = center
        self.__radius = radius
    
    def __str__(self):
        return "Center: (" + str((list(self.__center))[0])+','+ str((list(self.__center))[1]) + ")  radius: " + str(self.__radius)
    def __repr__(self):
        return "Center: (" + str((list(self.__center))[0])+','+ str((list(self.__center))[1]) + ")  radius: " + str(self.__radius)    
    def __eq__(self,other):
        if type(self) != type(other):
            return False
        if self.__radius == other.__radius:
            return True
        return False

    def __lt__(self,other):
        if type(self) != type(other):
            return False
        return self.__radius < other.__radius
    def __le__(self,other):
        if type(self) != type(other):
            return False
        return self.__radius <= other.__radius
    def __gt__(self,other):
        if type(self) != type(other):
            return False
        return self.__radius > other.__radius
    def __ge__(self,other):
        if type(self) != type(other):
            return False
        return self.__radius >= other.__radius

    def intersect(self,other):
        dist = math.sqrt(((list(self.__center))[0]-(list(other.__center))[0])**2 + ((list(self.__center))[1]-(list(other.__center))[1])**2)
        return dist <= self.__radius + other.__radius

def main():
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect:", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect:", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect:", circle2.intersect(circle3)) # True

main()           
    
