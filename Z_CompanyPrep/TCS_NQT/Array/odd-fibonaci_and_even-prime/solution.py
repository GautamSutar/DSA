def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        return 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime(n):
    count = 0
    num = 1

    while True:
        num += 1
        if is_prime(num):
            count += 1
            if count == n:
                return num



n = int(input())

if n % 2 == 1:
    pos = (n // 2) + 1
    print(fibonacci(pos))
else:
    pos = n // 2
    print(prime(pos))
