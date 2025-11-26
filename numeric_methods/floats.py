x = float(input("Enter a float greater than zero:"))
b = float(input("Enter a float greater than one:")) 
n = 0 

while x <= b**n:
    n-=1
while x > b**(n+1):
    n+=1

print(f"The number that satifies the conditions b**n<=x<=b**(n+1) is {n}")

while b**(n+1) < x < b**n :
    if b**n>  b**(n+1):
        n-=1
    else:
        n+=1
print(n)
