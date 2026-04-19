n = int(input())

if n % 2 == 1:
    # odd position → powers of 2
    pos = (n // 2) + 1
    print(2 ** (pos - 1))
else:
    # even position → powers of 3
    pos = n // 2
    print(3 ** (pos - 1))
