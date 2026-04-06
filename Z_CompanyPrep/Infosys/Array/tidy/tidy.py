def tidy(n):
    while n > 9:
        last = n % 10
        n //= 10
        secondLast = n % 10
        if last < secondLast:
            return "not tidy"
    
    return "tidy"

n = int(input())

print(tidy(n))
