import sys
import math

# check argument count
if len(sys.argv) != 2:
    print("Usage: python program.py <diameter>")
    sys.exit()

# get diameter from command line
diameter = int(sys.argv[1])

# calculate radius
radius = diameter / 2

# calculate area
area = math.pi * radius * radius

# print with 2 decimal precision
print(f"{area:.2f}")
