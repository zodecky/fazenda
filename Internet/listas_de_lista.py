signos = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi",
          "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]
aniversario = [["Patinhas", "22/01/1945"], ["Donald", "12/09/1968"],
               ["Margarida", "02/10/1975"], ["Lalá", "15/05/2010"]]


def exibeSigno(lista, lista_signo):
    for mini_lista in lista:
        indice = int(mini_lista[1][6:]) % 12
        print(f"Nome: {mini_lista[0]}\nSigno: {lista_signo[indice]}\nAniversário: {mini_lista[1]}")


exibeSigno(aniversario, signos)
