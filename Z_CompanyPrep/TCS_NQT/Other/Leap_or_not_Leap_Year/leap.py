import sys


if len(sys.argv) != 2:
    print("Usage: python program.py <year>")
    sys.exit()


year = int(sys.argv[1])

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year ")
