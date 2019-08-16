def reverse(string):
	rString = ""
	for c in range(len(string)-1, -1, -1):
		rString += string[c]
		#print (string[c] + " " + str(c))
	return rString


def is_palindrome(string):
	if string == reverse(string):
		print (string + " is a palindrome")
	else:
		print (string + " is NOT a palindrome")

input = raw_input("Digite algo: ")

is_palindrome(input)