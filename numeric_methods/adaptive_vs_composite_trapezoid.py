#part 1

global_list = []
def trapz(y, x=None, tol = 1e-7):
    global global_list

    if callable(y):
        a,b = x
        m = (a + b) / 2
        ya, yb, ym = y(a) , y(b), y(m)

        global_list.append(a)
        global_list.append(b)

        if abs(ya + yb - 2*ym) < 4 * tol:
            return trapz([ya,yb] , [a,b])

        else:
            return trapz(y,[a,m],tol) + trapz(y, [m,b],tol)


    elif x is None:
        area = 0
        for i in range(len(y)-1):
            area += (y[i] + y[i + 1])/2
        return area

    else:
        area2 = 0

        c = sorted(zip(x,y))
        x,y = zip(*c)

        for i in range(len(y)-1):
            area2 += (x[i+1] - x[i]) * (y[i+1] +y[i]) / 2
        return area2

x2 = [0,1,2,3]
y2 = [0,1,2,3]

area = trapz(y2)
print("Compositite Trapezoidal Rule (Unit Spacing):", area)

area2 = trapz(y2,x2)
print("Compositite Trapezoidal Rule(Custom x):", area2)

def semicircle(x):
    global global_list
    global_list.append(x)
    return (1-x**2)**0.5

area3 = trapz(semicircle , [-1,1], tol= 1e-7)
print("Adapative Trapezoidal Rule (1-x**2)**0.5 over [-1,1]:",area3)

#part 2
import numpy as np
import matplotlib.pyplot as plt

global_list.clear()

a , b = -1,1
tol = 1e-7

adaptive_integral = trapz(semicircle, [a,b], tol)
adaptive_points = sorted(set(global_list))

n_values = [10,20,40,80,160,320,640]
composite_results = []

for n in n_values:
    x_vals = [a+ i * (b-a) / n for i in range(n+1)]
    y_vals = [semicircle(x) for x in x_vals]
    integral = trapz(y_vals, x_vals)
    composite_results.append((n,integral))


closest_n , closest_integral = min(composite_results, key=lambda x:abs(x[1] - adaptive_integral))

# Plotting
x_plot = [a + i * (b - a) / 1000 for i in range(1001)]
y_plot = [semicircle(x) for x in x_plot]

plt.figure(figsize=(12, 6))

# Composite Trapezoidal Rule Plot
plt.subplot(1, 2, 1)
plt.plot(x_plot, y_plot, label=r'$y = \sqrt{1 - x^2}$', color='blue')
plt.scatter(x_vals, [semicircle(x) for x in x_vals], color='red', label="Composite Trapezoid Points")
plt.fill_between(x_vals, [0] * len(x_vals), [semicircle(x) for x in x_vals], color='red', alpha=0.3, step='mid')
plt.title(f"Composite Trapezoidal Rule (n={closest_n})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Adaptive Trapezoidal Rule Plot
plt.subplot(1, 2, 2)
plt.plot(x_plot, y_plot, label=r'$y = \sqrt{1 - x^2}$', color='blue')
plt.scatter(adaptive_points, [semicircle(x) for x in adaptive_points], color='green', label="Adaptive Trapezoid Points")
plt.fill_between(adaptive_points, [0] * len(adaptive_points), [semicircle(x) for x in adaptive_points], color='green', alpha=0.3, step='mid')
plt.title(f"Adaptive Trapezoidal Rule (Evaluations={len(adaptive_points)})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.tight_layout()
plt.show()

#Plotting Trapezoids
for i in range(len(x_vals)-1):
    x0,x1 = x_vals[i] , x_vals[i+1]
    y0,y1 = semicircle(x0) , semicircle(x1)

    plt.plot([x0,x0] , [0,y0] ,color="black")
    plt.plot([x1,x1] , [0,y1] ,color="black")
    plt.plot([x0,x1] , [y0,y1] ,color="black")
    plt.plot([x0,x1] , [0,0] ,color="black")


# Print final comparison
print(f"Adaptive Trapezoidal Rule used {len(adaptive_points)} evaluations.")
print(f"To achieve similar accuracy, Composite Trapezoidal Rule required n = {closest_n}.")
print(f"Adaptive Integral: {adaptive_integral}")
print(f"Closest Composite Integral (n={closest_n}): {closest_integral}")

#This shows us that compositite is much more efficient than adaptive

