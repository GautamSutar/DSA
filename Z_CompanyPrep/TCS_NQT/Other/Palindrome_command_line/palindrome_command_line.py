import sys

if len(sys.argv) != 2:
    sys.exit()

n = sys.argv[1]

if n == n[::-1]:
    print("yes")
else:
    print("no")

