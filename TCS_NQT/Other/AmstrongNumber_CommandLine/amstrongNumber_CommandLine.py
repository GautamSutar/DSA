import sys

if len(sys.argv) != 2:
    sys.exit()

n = int(sys.argv[1])
temp = n
s = 0
while temp > 0:
    digit = temp % 10
    s += digit**3
    temp //= 10

if s == n:
    print("Yes")
else:
    print("No")
