proibidas = ["a", "ante", "após", "até", "com", "contra", "de", "desde",
             "em", "entre", "para", "perante", "por", "sem", "sob", "sobre",
             "trás"]

with open("/Users/Gabriel/Documents/GitHub/fazenda/Chiqueiro/alvorada.txt") as arquivo:
    histolista = []  # Lista que tem o que vai ser usado no histograma
    master_lista = []  # Todas as palavras

    # Cria a master_lista
    for linha in arquivo:
        linha = linha.lower()  # deixa tudo minúsculo
        mini_lista = linha.split()  # transforma em uma lista
        for i, palavra in enumerate(mini_lista):
            master_lista.append(mini_lista[i])

    while True:
        try:
            # Contador
            palavra_contada = master_lista[0]
            quantos = master_lista.count(palavra_contada)

            # Cria histolista
            histolista.append([palavra_contada, quantos])
            # Remove palavra da lista grande
            while True:
                try:
                    master_lista.remove(palavra_contada)
                except ValueError:
                    break
        except IndexError:
            break

    print(histolista)

print("Banan,nanana,".replace(",", ""))
