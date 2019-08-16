import turtle
from PIL import ImageGrab
import os

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Pen()
t.speed("fastest")
t.hideturtle()

imgName = 0
boxCrop = (360, 140, 1000, 690)
step = 8
angle = 90
#filepath = "C:\Users\Igor\Documents\coding\python\fractal\hilbert_curve\print\name.jpg"


def A(n):
	if n > 0:
		L("-BF+AFA+FB-", n, "deeppink")

def B(n):
	if n > 0:
		L("+AF-BFB-FA+", n, "aqua")
		
def L(string, n, color):
	t.pencolor(color)
	for letter in string:
		if letter == "-":
			t.left(angle)
		elif letter == "+":
			t.right(angle)
		elif letter == "F":
			t.forward(step)
		elif letter == "A":
			A(n-1)
		elif letter == "B":
			B(n-1)
		
	#savePrint()	
		
#def savePrint():
	#ImageGrab.grab(boxCrop).save("C:\Users\Igor\Documents\coding\python\pil\screen_capture.jpg", "JPEG")
	#imgName += 1
	#print imgName
	
t.penup()
t.goto(-330, -275)
t.pendown()

A(6)