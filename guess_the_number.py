import random

name = raw_input("Hello! What is your name?\n")

print "\nWell, " + name + ", I am thinking of a number between 1 and 20"

number = random.randint(1, 20)
guesses = 0

print number

while True:
	guess = int(raw_input("\nTake a guess\n"))

	if guess < number:
		print "Your guess is too low"
		guesses += 1
	elif guess > number:
		print "Your guess is too high"
		guesses += 1
	elif guess == number:
		guesses += 1
		print "Good job, " + name + " You guessed my number in " + str(guesses) + " guesses!"
		break