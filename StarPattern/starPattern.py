n = 5

for i in range(1, 2 * n):
    if i <= n:
        stars = i - 1
    else:
        stars = 2 * n - i - 1

    # Left stars
    print("* " * stars, end="")

    # Left special
    print("@ ", end="")

    # Middle spaces
    spaces = 2 * (n - stars - 1)
    print("  " * spaces, end="")

    # Right special
    if stars != n - 1:
        print("# ", end="")

    # Right stars
    print("* " * stars)
