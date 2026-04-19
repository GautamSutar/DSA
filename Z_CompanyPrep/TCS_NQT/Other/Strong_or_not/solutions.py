import sys
import math

# check argument
if len(sys.argv) != 2:
    sys.exit()

n = int(sys.argv[1])

temp = n
s = 0

while temp > 0:
    digit = temp % 10
    s += math.factorial(digit)
    temp //= 10

if s == n:
    print("YES")
else:
    print("NO")
