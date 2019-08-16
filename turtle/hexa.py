import turtle

t = turtle.Turtle()
#t.hideturtle()

def hexa():
    for x in range(6):
        t.forward(50)
        t.right(60)

for x in range(6):
    hexa()
    t.left(60)
