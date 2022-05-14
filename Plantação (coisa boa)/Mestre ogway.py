import turtle
import math

tort = turtle.Turtle()


def poligono(n, rotacaoInicial):
    tort.left(rotacaoInicial)
    for i in range(n):
        tort.fd(100 / n * 5)
        tort.left(360 / n)


def poligod(n):
    for i in range(n):
        poligono(0, i + 2)


def policirculo(r):
    for i in range(100):
        tort.fd(r)
        tort.left(360 / 100)


def polisenox(n, tamanho):
    for i in range(n):
        tort.goto(i * tamanho + c, math.sin(i) * tamanho)


def polisenoy(n, tamanho):
    for i in range(n):
        tort.goto(math.sin(i) * tamanho + c, i * tamanho)


def parabola(a, b, c, distancia, tamanho):
    bonustort = turtle.Turtle()
    for i in range(distancia):
        tort.goto(i * tamanho, a * (i**2) + b * i + c)
        bonustort.goto(-i * tamanho, a * (i**2) + b * i + c)


def elipse(x, y, a, b):
    for i in range(100):
        tort.goto((a * math.sqrt(b**2 - y**2)) / b, (b * math.sqrt(a**2 - x ** 2))/a)
        return


parabola(10, 4, 0, 100, 100)
