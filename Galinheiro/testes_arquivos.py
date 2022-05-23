arq = open("Galinheiro/arquivo.txt", "r")

for linha in arq:
    print(linha, end="")
arq.close()
