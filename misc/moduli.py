# By hand I got mod(1/i) = 1 & mod(1/2+3i) = sqrt(13)/13 =  .277350

x = 1/1j
z = 1/(2+3j)

modX =( x * x.conjugate())**0.5
print(f"The modulus of 1/i is {modX}")
modZ = (z * z.conjugate())**0.5
print(f"The modulus of 1/(2+3i) is {modZ}")

