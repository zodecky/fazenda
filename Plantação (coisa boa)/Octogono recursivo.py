import turtle

t = turtle.Turtle()


def octogono_r(t, lado):
    if lado > 5:
        for i in range(8):
            t.fd(lado)
            t.right(45)
        t.right(67.5)
        t.up()
        t.fd(27)
        t.down()
        t.left(67.5)
        octogono_r(t, lado - 20)
    return


octogono_r(t, 120)
t.done()
t.exitonclick()
