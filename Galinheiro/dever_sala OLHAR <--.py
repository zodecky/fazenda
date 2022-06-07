banana = [i * 3 for i in range(20)]
banana.extend([i * 2 for i in range(13)])
banana[5] = [3, 5, 10, 3, [], []]

luisa = ["oi", "banana", 3, [3, 4, 5, 7, [8, 2, "hehehehe"], "ahajdhj"]]


def extrai_no_intervalo(lista, ini, fim):  # ini < fim
    lista_retorno = []
    for elemento in lista:
        if isinstance(elemento, int):
            if ini <= elemento <= fim:
                lista_retorno.append(elemento)
        else:
            lista_filho = extrai_no_intervalo(elemento, ini, fim)
            lista_retorno.extend(lista_filho)
    return lista_retorno


def string_para_int(lista):
    for i, elemento in enumerate(lista):
        if isinstance(elemento, str):
            lista[i] = len(elemento)
        elif isinstance(elemento, list):
            string_para_int(elemento)


def remove_impares(lista):
    """Somente inteiros sao pares ou impares."""
    i = 0
    while len(lista) > i:
        if isinstance(lista[i], int):
            if lista[i] % 2 != 0:
                lista.pop(i)
            else:
                i += 1
        elif isinstance(lista[i], list):
            if len(lista[i]) == 0:
                lista.pop(i)
            else:
                remove_impares(lista[i])
                i += 1
        else:
            i += 1


def busca(tabela, letra):
    for i, elemento in enumerate(tabela):
        if letra == elemento[0]:
            return i + 1
    return 0


def sequencia_caracteres(txt):
    txt = txt.replace(" ", "")
    tabela = []
    for letra in txt:
        i_busca = busca(tabela, letra)
        if i_busca:
            tabela[i_busca - 1][1] += 1
        else:
            tabela.append([letra, 1])
    # tabela.sort()
    print(tabela)


# print(extrai_no_intervalo(banana, 2, 20))
# string_para_int(luisa)
# print(luisa)
# remove_impares(banana)
# print(banana)
sequencia_caracteres("oi ooopessoal tudo bem aaaaaa hgsdjhgasj qwh iqwi uqwyhofwie jhief")
