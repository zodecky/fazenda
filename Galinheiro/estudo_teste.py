import random

n = random.randint(1, 10)
guarda_n = n
acrescimo = random.randint(1, 10)

somador = 1
qt_multiplo = 0

print("Valores:")

while n > 0:
    somador += acrescimo

    if somador % 3 == 0:
        qt_multiplo += 1

    print(somador)
    n -= 1

media = somador / guarda_n

print(f"\nValor de n: {guarda_n}")
print(f"Valor de acrescimo: {acrescimo}")
print(f"Média: {round(media, 2)}")
print(f"Quantidade de valores múltiplos de 3: {qt_multiplo}")
