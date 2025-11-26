num = 0
max_length = 0

for n in range (2,1001):
    new_n = n
    length = 1
    
    while new_n != 1:
        if new_n % 2 == 1:
            new_n= 3*new_n+1
            length+=1
            
        else:
            new_n=new_n//2
            length+=1
            
    if length > max_length:
        max_length =length
        num = n
print(f"The number between 2 and 1000 with the longest Hailstone sequence is {num} with a sequence length of {max_length}")

