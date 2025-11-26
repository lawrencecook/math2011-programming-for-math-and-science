fruits = ['apple', 'banana', 'date', 'pear', 'dragonfruit']

order = [4 , 2 , 1 , 3 , 5]

place = list(zip(order, fruits))

sort = sorted(place)

fruits_sorted = [fruit for _, fruit in sort]

print(fruits_sorted)

