# Converte lista para inteiro
def lista_para_inteiro(lista, base=10):
    n = 0
    for elemento in lista:
        n = base * n + elemento
    return n


def paraBaseN_r(numero, base, it=0):
    if numero == 0:
        return ""
    retorno = str(paraBaseN_r(numero // base, base, it + 1)) + str(numero % base)
    return retorno if it == 0 else int(retorno)


def paraBase10_r(numero, base, it=0):
    if numero == 0:
        return 0
    return ((numero % 10) * base**it) + paraBase10_r(numero // 10, base, it + 1)


def paraBaseN_i(numero, base):
    i = 0  # Indice para adicionar na lista
    resto = []
    while numero != 0:
        resto.append(numero % base)  # Resto
        numero = numero // base  # Divisão
        i += 1
    return lista_para_inteiro(resto[::-1])


def paraBase10_i(numero, base):
    i = 0  # Indice para adicionar na lista
    soma = 0  # Incializa soma
    lista = [int(x) for x in str(numero)]  # Converte número para lista
    lista = lista[::-1]  # Inverte lista

    while True:
        try:
            soma += lista[i] * (base**i)
        except IndexError:
            break
        i += 1

    return soma


print(paraBase10_i(11000, 2))
print(paraBase10_r(11000, 2))
print(paraBaseN_i(24, 2))
print(paraBaseN_r(24, 2))
