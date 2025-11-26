import math
from linear_algebra.Vector_Class import Vector
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#1) beginning city positions
A = Vector([0,2])
B = Vector([4,3])
C = Vector([2,0])
D = Vector([5,0])

#2) gradient function
def grad(x):
    P1 = Vector([x[0],x[1]])
    P2 = Vector([x[2],x[3]])

    v1a = (P1 - A)/(P1 - A).norm()
    v1b = (P1 - B)/(P1 - B).norm()
    v12 = (P1 - P2)/(P1 - P2).norm()

    v2c = (P2 - C)/(P2 - C).norm()
    v2d = (P2 - D)/(P2 - D).norm()
    v21 = (P2 - P1)/(P2 - P1).norm()

    g1 = v1a + v1b + v12
    g2 = v2c + v2d + v21

    return Vector([g1[0],g1[1],g2[0],g2[1]]) 

#3) time stepping
dt = 0.01
maxstep = 500

x = Vector([2,1.5,3,-0.5]) #inital guess 
history = [x.copy()]

for i in range(maxstep):
    g = grad(x)
    x = x - g * dt 
    history.append(x.copy())

#4) Animation
fig = plt.figure()
ax =  fig.add_subplot(111)
ax.set_aspect('equal','box')
ax.set_xlim(-1,6)
ax.set_ylim(-2,6)


line1, = ax.plot([],[],'-o',lw=1)
line2, = ax.plot([],[],'-o',lw=1)
line3, = ax.plot([],[],'-o',lw=1)

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    return line1,line2,line3

def update(f):
    x = history[f]
    P1 = Vector([x[0],x[1]])
    P2 = Vector([x[2],x[3]])

    line1.set_data([A[0],P1[0],B[0]],[A[1],P1[1],B[1]])
    line2.set_data([P1[0],P2[0]],[P1[1],P2[1]])
    line3.set_data([C[0],P2[0],D[0]],[C[1],P2[1],D[1]])

    return line1,line2,line3

ani = animation.FuncAnimation(fig,update,frames=len(history),init_func=init,blit=True,interval=30)

plt.show()

def angle(u, v):
    return math.degrees(math.acos(Vector.dot(u, v) / (u.norm() * v.norm())))

final = history[-1]
P1f   = Vector([final[0], final[1]])
P2f   = Vector([final[2], final[3]])

# around P1: to A, to B, to P2
uPA   = A   - P1f
uPB   = B   - P1f
uP12  = P2f - P1f

# around P2: to C, to D, to P1
uPC   = C   - P2f
uPD   = D   - P2f
uP21  = P1f - P2f

print("Angles at P1:", angle(uPA, uPB), angle(uPA, uP12), angle(uPB, uP12))

print("Angles at P2:", angle(uPC, uPD), angle(uPC, uP21), angle(uPD, uP21))
