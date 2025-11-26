from cmath import *
import matplotlib.pyplot as plt

n = 5
s = 2


z = [exp((2 * pi * 1j *k)/n) for k in range(n)]

x = [t.real for t in z]
y = [t.imag for t in z]

star_x = [x[k * s %n] for k in range(n)]
star_y = [y[k * s%n] for k in range(n)]

plt.plot(star_x +[star_x[0]],star_y+[star_y[0]], 'r--')
plt.show()
#######################################################################################################################
n = 7 
s = 3
z = [exp((2 * pi * 1j *k)/n) for k in range(n)]

x = [t.real for t in z]
y = [t.imag for t in z]

star_x = [x[k * s %n] for k in range(n)]
star_y = [y[k * s%n] for k in range(n)]

plt.plot(star_x +[star_x[0]],star_y+[star_y[0]], 'r--')
plt.show( )
