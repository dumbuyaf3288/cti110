# P1T1
# Area of a rectangle
# Fatmata Dumbuya
# 23rd June, 2018

# Get the dimension of rectangle 1
lenght1 = int(input("enter the lenght of rectangle 1: "))
width1 = int(input("enter the width of rectangle 1: "))

# Get dimension of rectangle 2
lenght2 = int (input("enter the length of rectangle 2: "))
width2 = int(input("enter the width of rectangle 2: "))

# Calculate the areas of the rectangles
area1 = lenght1 * width1
area2 = lenght2 * width2

# Determine which has the greater area
if area1 > area2:
    print("rectangle 1 has the greater area.")
elif area2 > area1:
     print("rectangle 2 has the greater area.")
else:
     print("both has the same area.")
