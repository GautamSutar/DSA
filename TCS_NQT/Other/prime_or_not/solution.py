import sys
import math

# check argument
if len(sys.argv) != 2:
    print("Usage: python program.py <number>")
    sys.exit()

n = int(sys.argv[1])

# prime check
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

# output
if is_prime:
    print(f"{math.sqrt(n):.2f}")
else:
    print("0.00")
