import turtle
#from colorsys import hsv_to_rgb

screen = turtle.Screen()
screen.bgcolor("black")
#screen.colormode(1.0)

t = turtle.Pen()
t.speed("fastest")

step = 10
angle = 90


def X(n):
	if n > 0:
		L("X+YF+", n, "lime")
		
def Y(n):
	if n > 0:
		L("-FX-Y", n, "springgreen")
		
def L(string, n, color):
	t.pencolor(color)
	
	for letter in string:
		if letter == "-":
			t.left(angle)
		elif letter == "+":
			t.right(angle)
		elif letter == "X":
			X(n-1)
		elif letter == "Y":
			Y(n-1)
		elif letter == "F":
			t.forward(step)
	

t.penup()
t.goto(-200, 0)
t.pendown()	
	
t.left(angle)	
X(11)