proibidas = ["e", "o", "a", "ante", "após", "até", "com", "contra", "de",
             "desde", "em", "entre", "para", "perante", "por", "sem", "sob",
             "sobre", "trás", "lá", "no", "que", "de", "tão", "é", "quando",
             "não", "há", "ir", "me"]


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


def tem_palavra(txt, word, inicio=False):
    if inicio:
        indice = txt.find(" ")
        return txt[0:indice] == word
    return ' ' + word + ' ' in ' ' + txt + ' '


def limpa(txt):
    for palavra_proibida in proibidas:
        if tem_palavra(txt, palavra_proibida, inicio=True):
            txt = txt.replace(palavra_proibida + " ", "", 1)

        elif tem_palavra(txt, palavra_proibida):
            txt = txt.replace(" " + palavra_proibida + " ", " ")

    return txt


with open("Chiqueiro/alvorada.txt") as arquivo:
    histolista = []  # Lista que tem o que vai ter tudo usado no histograma
    master_lista = []  # Todas as palavras

    # Cria a master_lista
    for linha in arquivo:
        linha = linha.lower()  # deixa tudo minúsculo
        linha = linha.replace(",", "")
        linha = limpa(linha)

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
    # Até esse ponto, a histolista tem todos os valores
    # A partir, ela terá só os 10 maiores
    histolista = Sort(histolista)  # Sort do maior para o menor
    histolista = histolista[0:10]
    print(histolista)
