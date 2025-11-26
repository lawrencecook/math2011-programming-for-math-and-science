n = int(input("How many rows do you want?:"))

triangle = []

for num in range(n):
    row = [1]
    if triangle:
        last = triangle[-1]

        row += [last[i] + last[i+1] for i in range(len(last) - 1)]

        row.append(1)
    triangle.append(row)
print(triangle) 

