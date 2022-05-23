def lista_aprovados(nome):
    arq = open("Galinheiro/arquivo.txt", "r")

    for linha in arq:
        p1 = linha.find(",")
        nome = linha[:p1]

        p2 = linha.find(",", p1 + 1)
        n1 = float(linha[p1 + 1:p2])
        n2 = float(linha[p2 + 1:])

        if (n1 + n2) / 2 >= 5.0:
            print(nome)
    arq.close()
