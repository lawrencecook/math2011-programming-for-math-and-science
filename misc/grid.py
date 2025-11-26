x = int(input("Row #:")) 
y = int(input("Column #:"))
i = x//2 
j = y//2

# Part a: Give the grid coordinates
grid_coordinates = (i,j)
print(f"Grid Coordinates: {grid_coordinates}")
#Part b: Give the grid numbers (Right to left)
grid_numbers = 16 * j + (15 - i)
print(f"Grid Number: {grid_numbers}")
#part C: Square's color
if (i+j)%2 == 0:
   color = "Black"
else:
   color = "White"
print(f"Color: {color}")

