def powerOfN(x: float, n: int) -> float:
    def solve(base, exp):
        if exp == 0:
            return 1.0
        half = solve(base, exp // 2)
        if exp % 2 == 0:
            print(half)
            return half * half
        else:
            return half * half * base
    return solve(x, n)

print(powerOfN(2, 10))
