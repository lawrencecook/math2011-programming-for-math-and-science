
#8
from time import time, sleep
import random

n = 1000
a = [random.random() for r in range(n+1)]
x = 2

start = time()
#Schoolbook
s = 0
for i in range(n+1):
    s += a[i] * x**i
end = time()
print("Schoolbook method time:", end - start, "second")

sleep(1)

start = time()
#Horner's Method
s = 0
for i in range(n,-1,-1):
    s = s*x + a[i]
end = time()
print("Horner's method time:", end - start, "seconds")

sleep(1)

start = time()
#Example 6.8
for i in range(1, n+1):

    i_min = i 
    for j in range(i+1 , n+1):
        if a[j] < a[i_min]:
            i_min = j

    a[i], a[i_min] = a[i_min] , a[i]

end = time()
print("Selecteion sort time:", end - start, "seconds")

sleep(1)

start = time()
repeat = 10000
#Example 6.9 - Log Linear Method
max_sum = 0
for r in range(repeat):
    
    for i in range(i, n+1):
        s = 0
        for j in range(i,n+1):
            s += a[j]
            if s > max_sum:
                max_sum = s
end = time()
print("Log Linear Method:", end - start, "seconds")

sleep(1)

start = time()
#Example 6.9 - Brute Force Method
for k in range(repeat):
    max_c = max_g = a[0]
    for x in a[1:]:
        max_c = max(x, max_c  + x)
        max_g = max(max_g,max_c)
end = time()
print("Brute Force Method:", end - start, "seconds")

#10
def relative_error(x_i , x_star):
    return abs(x_i - x_star) / abs(x_star)

def t(n):
    return 1.2907 * n - 2.07138

def root_finding_algorithm(n , x_star, x_0, tolerance=1e-10,max_iterations=1000):
    x_i = x_0

    for i in range(max_iterations):
        f = x_i**3 - x_star**3
        f_prime = 3 * x_i**2
        x_i = x_i - f / f_prime

        e_i = relative_error(x_i , x_star)

        if i + 1 >= int(t(n)) and e_i < 10**(-n):
            print("n=", n, ": Iterations i=", i+1, ",Relative error e_i", round(e_i,10), ",t(n) =", round(t(n),2))
            return i + 1
    print("maximum iterations reached without acheiving the desired relative error.")
    return max_iterations

x_star = 2.347
x_0 = 2.0

n = int(input("Enter the value of n:"))

iterations_needed = root_finding_algorithm(n, x_star, x_0)

if iterations_needed >= t(n):
    print("The number of iterations i=",iterations_needed,"is greated than or equal to t(n) =", round(t(n),2))
else:
    print("The number of iterations i=", iterations_needed,"is less than t(n) =", round(t(n),2))

#11
a = 50
b = 100

e_i = abs(a-b)/75
avg = (a+b)/2
upper_bound = avg * (1+e_i)

print("Relative error e_i=", e_i)
print("Upper bound for t(n) =", upper_bound)

#12
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 1000

target = Fraction(1, 10**1000)
x = Fraction(2,1)

iteration = 0 
while x*x - 2 > target:
    iteration += 1 
    x = Fraction(x + Fraction(2,x),2)

print("Rational approx of sprt(2):")
approx = Decimal(x.numerator) /Decimal(x.denominator)
print(approx)
