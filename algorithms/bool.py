l = [0.1 , 0.2 , 0.3, 0.4, 0.5]

dec = False

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        dec = True
    
    else:
        dec = False

if dec == True:
    print("This is is an DECREASING list of floats")
else:
    print("This is an INCREASING list of floats")

