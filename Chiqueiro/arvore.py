import turtle

t = turtle.Turtle()


def galhos(t, distancia, angulo, fator, lvl, i):
    distancia *= fator
    t.right(angulo)
    t.fd(distancia)

    if i < lvl:
        galhos(t, distancia, angulo, fator, lvl, i + 1)
    t.bk(distancia)
    t.left(angulo)
    t.fd(distancia)
    if i < lvl:
        galhos(t, distancia, angulo, fator, lvl, i + 1)
        i += 1
    t.bk(distancia)
    t.right(angulo / 2)


def arvore(t, distancia, angulo, fator, lvl):
    t.left(90)
    t.back(distancia)
    t.fd(distancia)
    galhos(t, distancia, angulo, fator, lvl, 0)


arvore(t, 100, 30, 0.8, 7)
