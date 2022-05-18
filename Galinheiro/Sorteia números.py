import random


def teste_intervalo_0_15(lista):
    for i in range(len(lista)):
        estado = "está no intervalo [0, 15]" if 0 <= lista[i] <= 15 else "não está no intervalo [0, 15]"
        print(f"O valor {lista[i]} {estado}")
    return


# Principal:
qt_numeros = 7

lista = [random.randint(0, 100) for _ in range(qt_numeros)]
teste_intervalo_0_15(lista)
