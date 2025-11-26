n = int(input("Enter a nonnegative integer:"))
k = int(input("Enter a nonnegative integer:"))
t = n-k

if( n or k) < 0 :
    print("You entered a negative number")

fac_n = fac_k = fac_t = 1
if k <= n :
    for i in range(1,n+1):
        fac_n*=i
    for m in range(1,k+1):
        fac_k*=m
    for o in range(1,t+1):
        fac_t*=o

    print( fac_n / (fac_k * fac_t) )

else :
    print("k cannot be larger than n")

