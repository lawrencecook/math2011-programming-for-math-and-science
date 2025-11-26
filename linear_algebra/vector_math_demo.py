#1 Compute x+y , x-y , and 2x - (1/3)y

# a) x = (1,1) & y = (2,3) ... x+y = (3,4) ... x-y = (-1,-2) ... 2x - (1/3)y = (4/3, 1)
# b) x = (2,-2) & y = (0,3) ... x+y = (2,1) ... x-y = (2,-5) ... 2x - (1/3)y = (4,-5)
# c) x = (1,2,-1) & y = (2,2,2) ... x+y = (3,4,1) ... x-y = (-1,0,-3) ... 2x - (1/3)y = (4/3,10/3,-8/3)
# d) x = (0,1,0,1) & y = (6,0,4,1) ... x+y = (6,1,4,2) ... x-y = (-6,1,-4,0) ... 2x - (1/3)y = (-2,2,-4/3, 5/3)

#2 Complete Vector Class
from collections import UserList

class Vector(UserList):
    def __str__(self):
        s = str(self.data)
        return '(' + s[1:-1] + ')'

    def __add__(self,other):
        return Vector([a + b for a, b in zip(self,other)])
    
    def __sub__(self,other):
        return Vector([a - b for a,b in zip(self,other)])
    
    def __mul__(self,other):
        return Vector([other*a for a in self])
    __rmul__ = __mul__

    def __truediv__(self,other):
        return Vector([other/a for a in self])
v1 = Vector([1,1])
v2 = Vector([2,3])
print(v1 + v2)
print(v1 - v2)
print(2*v1 - (1/3)*v2)
v1 = Vector([2,-2])
v2 = Vector([0,3])
print(v1 + v2)
print(v1 - v2)
print(2*v1 - (1/3)*v2)
v1 = Vector([1,2,-1])
v2 = Vector([2,2,2])
print(v1 + v2)
print(v1 - v2)
print(2*v1 - (1/3)*v2)
v1 = Vector([0,1,0,1])
v2 = Vector([6,0,4,1])
print(v1 + v2)
print(v1 - v2)
print(2*v1 - (1/3)*v2)


