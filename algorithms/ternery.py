x = int(input("Give an Integer Value:"))
ternary = []
neg = False

if x==0:
    print("zero")

if x < 0:
    x=abs(x)
    neg = True

while x>0:
    remainder = x % 3
    ternary.append(str(remainder))
    x = x//3

    num = "".join(reversed(ternary))

    if neg == True:
        num = "-" + num

    print(num)

