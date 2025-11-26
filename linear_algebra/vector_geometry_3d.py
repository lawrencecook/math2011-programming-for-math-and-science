
def norm(x,p=2):
    return sum([abs(i)**p for i in x])**(1/p)

def dot(x,y):
    return sum([x[a] * y[a] for a in range(len(x))])

def proj(x,y):
    proj_factor = ((dot(x,y) / (norm(y)**2) ))
    return [proj_factor * i for i in y]

import math
import numpy as np
def angle(x,y):
    return acos(dot(x,y) / (norm(x) * norm(y))) * (180/np.pi)

def unit(x):
    n = norm(x)
    return [i / n for i in x]

def cross(x,y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]

x = [1,2,3]
y = [4,5,6]
z = cross(x,y)

print(dot(x,z))
print(dot(y,z))
print("If both 0, then x and y are orthognal to their cross product (x cross y)")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v_pyramid = [ [0,0,0], [1,0,0], [0,1,0], [1,1,0], [0.5,0.5,1] ]
v_tetrahedron = [ [0,0,0], [1,0,0], [0.5, math.sqrt(3)/2,0], [0.5,math.sqrt(3)/6,math.sqrt(2)/math.sqrt(3)] ]

e_pyramid = [ (0,1), (1,3), (3,2), (2,0), (0,4), (1,4), (2,4), (3,4) ]
e_tetrahedron = [ (0,1), (1,2), (2,0), (0,3), (1,3), (2,3) ] 

def plot_3d_shape(vert,edges,title="Shapes"):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111,projection="3d")

    for i,j in edges:
        x_values = [vert[i][0] , vert[j][0]]
        y_values = [vert[i][1] , vert[j][1]]
        z_values = [vert[i][2] , vert[j][2]]

        ax.plot(x_values,y_values,z_values,'k-')

    for idx, (x,y,z) in enumerate(vert):
        ax.scatter(x,y,z,color='red',s=50)
        ax.text(x,y,z, f"V{idx+1}", fontsize=10)

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("x3")
    ax.set_title(title)
    ax.set_box_aspect([1,1,1])
    plt.tight_layout()
    plt.show()

plot_3d_shape(v_pyramid, e_pyramid,"Pyramid w Square Base")
plot_3d_shape(v_tetrahedron, e_tetrahedron, "Tetrahedron")


