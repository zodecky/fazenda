def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def calcula_euler(n):
    if n == 1:
        return 1
    return 1 / fatorial(n - 1) + calcula_euler(n - 1)


def quadradoRecursivo(lado, t):
    if lado < 10:
        return
    t.fd(lado)
    t.left(90)
    return quadradoRecursivo(lado - 10, t)


def mdc(x, y):
    if x % y == 0:
        return y
    return mdc(y, x % y)


def frib(n):
    if n == 1:
        return 1
    return (n - 1) * frib()
