s = "apple banana date pear dragonfruit"

fruits_list = s.split()

fruit_with_d = []

for fruit in fruits_list:
    if 'd' in fruit:
        fruit_with_d.append(fruit)

print(fruit_with_d)

s = s.replace("." , "")

fruits_list = s.split()

fruit_order = { }
counter = 1

for fruit in fruits_list:
    fruit_order[fruit] = counter
    counter+=1

print(fruit_order)

