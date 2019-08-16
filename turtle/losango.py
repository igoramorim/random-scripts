import turtle

t = turtle.Turtle()


def losango():
    t.forward(60)
    t.right(30)
    t.forward(60)
    t.right(150)
    t.forward(60)
    t.right(30)
    t.forward(60)


for x in range(12):
    losango()
