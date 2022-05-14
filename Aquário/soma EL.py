def soma_el_r(lista):  # Resolve listas com listas de inteiro dentro
    soma = 0
    for elemento in lista:
        if type(elemento) == int:  # Testa o tipo do elemento
            soma += elemento  # soma o elemento ao somatorio, se for inteiro
        else:
            soma += soma_el_r(elemento)  # passa a LISTA DE DENTRO para a função

    return soma  # saida da função


# - - - - - - - - - - - - - - - PRINCIPAL - - - - - - - - - - - - - - - -#
lista = [1, 4, 6, 6, [4, 6, 2, [245, 25], 5, 6], 3, 5]

print(soma_el_r(lista))
