import sys
import math

if len(sys.argv) != 2:
    sys.exit()

n = int(sys.argv[1])
r = int(math.sqrt(n))

if r * r == n:
    print("yes")
else:
    print("no")
