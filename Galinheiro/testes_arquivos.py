with open("Galinheiro/arquivo.txt", "r") as arq:
    total = 0
    for linha in arq:
        total += linha.count("eu")
print(total)