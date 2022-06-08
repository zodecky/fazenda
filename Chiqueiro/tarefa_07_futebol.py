"""gabriel zagury 2210912.
   luiza marcondes 2210275

o número de vitórias,
o número de empates,
o número de derrotas,
o total de gols pró e
o total de gols contra
"""

lista_mestre = [['AthleticoPR', 16, 9, 13, 54, 37],
                ['Cruzeiro', 14, 11, 13, 34, 34],
                ['Botafogo', 13, 12, 13, 38, 46],
                ['Santos', 13, 11, 14, 46, 40],
                ['Bahia', 12, 12, 14, 39, 41],
                ['Fluminense', 12, 9, 17, 32, 46],
                ['Corinthians', 11, 11, 16, 34, 35],
                ['Chapecoense', 11, 11, 16, 34, 50],
                ['Ceara', 10, 14, 14, 32, 38],
                ['Vasco', 10, 13, 15, 41, 48],
                ['Sport', 11, 9, 18, 35, 57],
                ['AmericaMG', 10, 10, 18, 30, 47],
                ['Vitoria', 9, 10, 19, 36, 63],
                ['Parana', 4, 11, 23, 18, 57],
                ['Flamengo', 23, 11, 4, 64, 26],
                ['Palmeiras', 21, 9, 8, 59, 29],
                ['Internacional', 19, 12, 7, 51, 29],
                ['Gremio', 18, 12, 8, 48, 27],
                ['SaoPaulo', 16, 15, 7, 46, 34],
                ['AtleticoMG', 17, 8, 13, 56, 43]]


def lista_saldo_de_gols(lista):
    """Retorna lista de saldo."""
    lista_saldo = []
    for i, elemento in enumerate(lista):
        nome = elemento[0]
        gols_pro = elemento[4]
        gols_contra = elemento[5]
        saldo_de_gols = gols_pro - gols_contra
        lista_saldo.append([nome, saldo_de_gols])
    return lista_saldo


def exibe_mais_empates(lista):
    lista.sort(key=lambda x: x[2], reverse=True)
    print("Os 5 primeiros que mais empataram:")
    for i in range(5):
        print(lista[i][0])


def cria_lista_pontuacao(lista):
    lista_pontuacao = []
    for elemento in lista:
        nome = elemento[0]
        pontos = elemento[1] * 3 + elemento[2]
        lista_pontuacao.append([nome, pontos])
    return lista_pontuacao


def exibe_campeao(lista_pt, lista_de_saldos):
    mini_lista = []
    for i, elemento in enumerate(lista_pt):
        mini_lista.append([elemento[0], elemento[1], lista_de_saldos[i][1]])

    mini_lista.sort(key=lambda x: x[1] * 1000 + x[2], reverse=True)

    if mini_lista[0][1] == mini_lista[1][1] and mini_lista[0][2] == mini_lista[1][2]:
        ganhadores = [mini_lista[0][0], mini_lista[1][0]]
        n_1 = 1  # Ignora os já adicionados
        n_2 = 2
        while (
                mini_lista[n_1][1] == mini_lista[n_2][1]
                and mini_lista[n_1][2] == mini_lista[n_2][2]):

            ganhadores.append(mini_lista[n_2][0])
            n_1 += 1
            n_2 += 2

        print(f"Os times {ganhadores} empataram e vão disputar em um campeonato decisivo")
        return
    print(f"{mini_lista[0][0]} foi vencedor!")
    return


# Principal:
lista_pontuacao = cria_lista_pontuacao(lista_mestre)
lista_saldos = lista_saldo_de_gols(lista_mestre)
# Exibe lista:
print(f"Lista de saldos:\n{lista_saldos}\n\n")
exibe_mais_empates(lista_mestre)
print(f"Lista de pontuações:\n{lista_pontuacao}\n\n")
exibe_campeao(lista_pontuacao, lista_saldos)


# Alteradas:
print("- - - - - - - - - - ALTERADAS - - - - - - - - - - ")
lista_mestre[15] = ["Palmeiras", 23, 11, 13, 64, 26]  # empatar palmeiras c Flamengo

lista_pontuacao = cria_lista_pontuacao(lista_mestre)
lista_saldos = lista_saldo_de_gols(lista_mestre)
# Exibe lista:
print(f"Lista de saldos:\n{lista_saldos}\n\n")
exibe_mais_empates(lista_mestre)
print(f"Lista de pontuações:\n{lista_pontuacao}\n\n")
exibe_campeao(lista_pontuacao, lista_saldos)
