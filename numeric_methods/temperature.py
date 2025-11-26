v1 = v2 = 3/4
t1 = 50
t2 = 100
counter = 1
i=1
while abs(t1-t2) > 1:
    
    if i%2 == 1:
        v1 = (1-v2)
        t1 = t1*v1 + v2*t2
        i+=1
    else:
        v2 = (1-v1)
        t2 = t1*v1 + v2*t2
        i+=1

    counter+=1

print(t1)
print(t2)
print(counter)

