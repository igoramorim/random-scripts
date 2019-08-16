import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Pen()
t.speed("fastest")
t.hideturtle()

step = 10
angle = 60

def X(n):
	if n > 0:
		L("X+YF++YF-FX--FXFX-YF+", n, "orange")

def Y(n):
	if n > 0:
		L("-FX+YFYF++YF+FX--FX-Y", n, "green")
		
def L(string, n, color):
	print(n)
	t.pencolor(color)
	for letter in string:
		if letter == "-":
			t.left(angle)
		elif letter == "+":
			t.right(angle)
		elif letter == "F":
			t.forward(step)
		elif letter == "X":
			X(n-1)
		elif letter == "Y":
			Y(n-1)
			
t.penup()
t.goto(80, 280)
t.pendown()

X(4)