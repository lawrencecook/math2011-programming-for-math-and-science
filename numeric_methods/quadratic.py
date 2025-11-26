a = 1e-20

pos = (-1 + (1 + 4*a)**0.5)/(2*a)

print(pos)

#The ahove code gives the answer for the positive root to be 0. This is because the term of 4*a is so small   that it's practially negligible. So it ends up being -1 + 1 in the denominator or 0.

#Below is code to fix it and make it more precise. By taking the conjugate and making an expression that stopstwo very close numbers subtracting it removes 0 in the denominator.

alt = 2/(1+(1+4*a)**0.5)
print(alt)

