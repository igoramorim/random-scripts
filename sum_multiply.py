def sum(list):
	sum = 0
	for number in list:
		sum += number
	print ("Numeros: " + str(list) + " Soma: " + str(sum))

def multiply(list):
	total = 1
	for number in list:
		total *= number
	print ("Numeros: " + str(list) + " Multiplicacao: " + str(total))
	
sum([1, 2, 3, 4])
multiply([1, 2, 3, 4])
