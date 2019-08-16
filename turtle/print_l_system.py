axiom = "A"

def L(string, n):
	if n > 0:
		new = ""
		for letter in string:
			if letter == "A":
				new += "AB"
			elif letter == "B":
				new += "A"
		print(new + "\n")
		L(new, n-1)

	
L("A", 10)