import turtle
import math


def circulo(r, color):
    t = turtle.Turtle()
    t.up()
    t.right(90)
    t.fd(r)
    t.left(90)
    t.down()

    # INICIO
    t.fillcolor(color)
    t.begin_fill()
    for i in range(360):
        t.fd((2 * math.pi * r) / 360)  # tamanho de cada andada
        t.left(1)
    t.end_fill()
    return


circulo(20, "blue")


def losango(lado):
    t = turtle.Turtle()
    t.up()
    t.right(90)
    t.fd(lado)
    t.left(45)
    t.down()
