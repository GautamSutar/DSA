n = int(input())

if n % 2 == 1:
    # odd position → even numbers
    pos = n // 2
    print(2 * pos)
else:
    # even position → previous / 2
    pos = (n // 2) - 1
    print(pos)
