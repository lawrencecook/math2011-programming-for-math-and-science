x = [0,1,0,2,0,3]; y = x.copy()
for i in range(len(x)):
    x[i] = (x[i-1] + x[i])/2

y = [(y[i-1] + y[i])/2 for i in range (len(y))]
print(x,y)


# The difference between the two comes from how x and y are positioned. "y" does it's caculations in one go, meaning so previous calculations don't effect the next ones. "x" doesn't do this, "x" is updated each time meaning that previous   calculations change the next ones.



