import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Pen()
t.speed("fastest")
t.hideturtle()

step = 8
angle = 90

def X(n):
	if n > 0:
		L("XFYFX+F+YFXFY-F-XFYFX", n, "purple")

def Y(n):
	if n > 0:
		L("YFXFY-F-XFYFX+F+YFXFY", n, "gold")
		
def L(string, n, color):
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
t.goto(-325, 270)
t.pendown()

X(5)