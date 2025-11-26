import numpy as np

class Vector: 
    def __str__(self):
        s = str(self.data)
        return '(' + s[1:-1] + ')'
    
    def __init__(self,data):
        self.data = data

    def __getitem__(self,index):
        return self.data[index]

    def __len__(self):
        return len(self.data)
    
    def copy(self):
        return Vector(self.data[:]
                      )
    def __add__(self,other):
        return Vector([a + b for a,b in zip(self,other)])

    def __sub__(self,other):
        return Vector([a - b for a,b in zip(self,other)])

    def __mul__(self,other):
        return Vector([other*a for a in self])

    __rmul__ = __mul__

    def __truediv__(self,other):
        return Vector([a / other for a in self])

    def norm(x,p=2):
        return sum([abs(i)**p for i in x])**(1/p)

    def dot(x,y):
        return sum([x[a] * y[a] for a in range(len(x))])

    def cross(x,y):
        if len(x) != 3 or len(y) != 3:
            raise ValueError("Only defined for 3 dimensions")
        cross = [u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2],  u[0]*v[1] - u[1]*v[0]]
        return cross

    def proj(x,y):
        proj_factor = ((dot(x,y) / (norm(y)**2) ))
        return [proj_factor * i for i in y]


    def angle(x,y):
        return acos(dot(x,y) / (norm(x) * norm(y))) * (180/np.pi)
