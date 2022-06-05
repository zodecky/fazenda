"""Tarefa 06."""

from random import randint
from random import shuffle
import turtle


proibidas = ["e", "o", "a", "ante", "após", "até", "com", "contra", "de",
             "desde", "em", "entre", "para", "perante", "por", "sem", "sob",
             "sobre", "trás", "lá", "no", "que", "de", "tão", "é", "quando",
             "não", "há", "ir", "me"]


class GabTurtle(turtle.Turtle):
    """turtle_gabriel."""

    def __init__(self, *args, **kwargs):
        """Fiz classe para aprender a usar."""
        super().__init__(*args, **kwargs)

    def anda(self, random=False):
        """Anda tamanho fixo 40."""
        self.up()
        if not random:
            self.fd(40)
        else:
            self.fd(randint(10, 100))
        self.down()

    def retangulo(self, altura, cor, texto):
        """Desenha os retangulos do histograma."""
        # Vai
        self.penup()
        self.back(15)  # metade da do que anda
        self.rt(90)
        self.fd(10)

        # Escreve
        self.color(cor)
        self.write(texto, align="center", font=("Arial", 9, "bold"))
        self.color("black")

        # Volta
        self.back(10)
        self.lt(90)
        self.fd(15)  # metade da do que anda
        self.pendown()
        self.fillcolor(cor)
        self.begin_fill()
        for _ in range(2):
            self.left(90)
            self.fd(altura * 10)
            self.left(90)
            self.fd(30)
        self.end_fill()

    def eixos(self):
        """Desenha os eixos."""
        self.fd(400)
        self.back(400)
        self.lt(90)
        self.fd(250)
        self.back(250)
        self.rt(90)

    def stripes(self, altura):
        """Desenha as linhas pontilhadas."""
        self.penup()
        self.color("black")
        self.fillcolor("black")
        self.goto(0, altura)
        self.pendown()
        self.write(altura // 10, align="right", font=("Arial", 12, "normal"))
        for _ in range(20):
            self.fd(10)
            self.penup()
            self.fd(10)
            self.pendown()

    def histograma(self, lista):
        """Faz o histograma."""

        lista_cores = ["#832e8e", "#e92626", "#fe4dcc", "#610f2a", "#ff6a0a",
                       "#4695de", "#72cb00", "#6f6f6f", "#000000", "#66e4cd"]
        lista_altura = []  # Lista vazia
        shuffle(lista_cores)
        for i_cor in range(10):
            altura = lista[i_cor][1]
            texto = lista[i_cor][0]
            self.retangulo(altura, lista_cores[i_cor], texto)
            self.anda()
            lista_altura.append(altura)

        lista_altura = list(set(lista_altura))  # Limpa duplicados
        for _, _alturas in enumerate(lista_altura):
            print(_alturas)
            self.stripes(_alturas * 10)

    def desenha_palavra(self, texto, tamanho, cor, i_palavra):
        self.color(cor)
        self.lt(90)
        self.penup()
        i_palavra += 1
        print(i_palavra)
        if (i_palavra == 3 or i_palavra == 4
                or i_palavra == 7 or i_palavra == 8):
            texto = texto[::-1]
            print(texto)
        for letra in texto:
            self.write(letra,
                       align="center",
                       font=("calibri", tamanho * 5, "bold"))
            self.fd(tamanho * 5)
        self.pendown()

    def nuvem(self, lista):
        lista_cores = ['red', 'green', 'blue', 'yellow',
                       'magenta', 'cyan', 'pink', 'gray', 'black', 'brown']
        shuffle(lista_cores)
        for i_cor in range(10):
            altura = lista[(i_cor + 1) * -1][1]
            texto = lista[(i_cor + 1) * -1][0]
            cor = lista_cores[i_cor]

            self.desenha_palavra(texto, altura, cor, i_palavra=i_cor)
            self.anda(random=True)

# ************************* Funções turtle *******************************


def Histograma(histo_lista):
    """Cria a turtle que desenha o histograma."""
    turt = GabTurtle()
    turt.speed(0)
    turt.eixos()
    turt.anda()
    turt.histograma(histo_lista)


def Nuvem(histo_lista):
    """Cria a turtle que desenha a nuvem."""
    turt = GabTurtle()
    turt.speed(1)
    turt.lt(180)
    for _ in range(7):
        turt.anda()
    turt.nuvem(histo_lista)

# ************************* Funções turtle *******************************
# --------------------------------------------------------------------------
# ************************* Funções lógica *******************************


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

# ************************* Funções lógica *******************************


with open("alvorada.txt") as arquivo:
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
    Histograma(histolista)
    Nuvem(histolista)
