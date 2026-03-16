import sys
import math

if len(sys.argv) != 3:
    sys.exit()

n = int(sys.argv[1])
m = int(sys.argv[2])

h = math.sqrt(n**n + m**m)
print(f"{h:.2f}")
