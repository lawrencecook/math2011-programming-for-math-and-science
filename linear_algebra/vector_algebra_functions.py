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

from math import acos
import numpy as np
def angle(x,y):
    return acos(dot(x,y) / (norm(x) * norm(y))) * (180/np.pi)

x1 = [2,5] 
x2 = [-5,2]
print(dot(x1,x2))
print(angle(x1,x2))
print(proj(x1,x2))

x1 = [2,1]
x2 = [-1,1]
print(dot(x1,x2))
print(angle(x1,x2))
print(proj(x1,x2))

x1 = [1,4,-3]
x2 = [5,1,3]
print(dot(x1,x2))
print(angle(x1,x2))
print(proj(x1,x2))

x1 = [1,1,1,1]
x2 = [1,-3,-1,5]
print(dot(x1,x2))
print(angle(x1,x2))
print(proj(x1,x2))
