#range(x, y, z)
# x = start	y = final	z = step

def reverse(string):
	rString = ""
	for c in range(len(string)-1, -1, -1):
		rString += string[c]
		print (string[c] + " " + str(c))
	return rString

input = raw_input("Digite algo: ")

print ("len(" + input + ") => " + str(len(input)))
print ("len(" + input + ")-1 => " + str(len(input)-1) + "\n")

print (reverse(input))