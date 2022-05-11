import turtle

t = turtle.Turtle(shape="turtle")

t.lt(90)

lv = 7
tarugo = 120
angulo = 30


t.bk(tarugo)
t.fd(tarugo)

def draw_tree(tarugo, level):

    tarugo = 0.8 * tarugo

    t.lt(angulo/2)
    t.fd(tarugo)

    if level < lv:
        draw_tree(tarugo, level + tarugo)

        
    t.bk(tarugo)
    t.rt(angulo)
    t.fd(tarugo)

    if level < lv:
        draw_tree(tarugo, level + tarugo)

        
    t.bk(tarugo)
    t.lt(angulo/2)
    return

t.speed("fastest")

draw_tree(tarugo, 2)

turtle.done()
