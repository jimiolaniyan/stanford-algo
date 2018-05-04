def exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = exp(x, n / 2)
        return y * y
    else:
        return x * exp(x, n - 1)


def mod(x, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = mod(x, n / 2, m)
        return (y * y) % m
    else:
        return ((x % m) * mod(x, n - 1, m)) % m