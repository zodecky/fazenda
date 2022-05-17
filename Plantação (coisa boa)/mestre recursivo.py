# Calcular fatorial recursivo
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


# Calcular numero e recursivo
def calcula_euler(n):
    if n == 1:
        return 1
    return 1 / fatorial(n - 1) + calcula_euler(n - 1)


# Mdc recursivo
def mdc(x, y):
    if x % y == 0:
        return y
    return mdc(y, x % y)


# Sequencia de fribonacci recursivo
def frib(n):
    if n == 1:
        return 1
    return (n - 1) * frib()
