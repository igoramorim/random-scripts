vowels = ["a", "e", "i", "o", "u"]

input = raw_input("Digite uma letra: ").lower()

if vowels.count(input) == 1:
	print ("True: vogal")
else:
	print ("False: nao e vogal")