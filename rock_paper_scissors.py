import sys
import getpass

def selectNames():
	global player1, player2
	
	player1 = raw_input("\nWhat's your name, Player 1?\n")
	player2 = raw_input("\nWhat's your name, Player 2?\n")
	newGame()

def newGame():
	p1Points = 0
	p2Points = 0
	
	print "\nLet's start!"
	print "\nUse R[ock] P[aper] or S[cissors] to play"
	
	inputs = ["r", "p", "s"]
	
	while True:
	
		p1Choice = getpass.getpass(prompt = "\n" + player1 + " , it is your turn: ", stream = None)
		if p1Choice not in inputs:
			print "Invalid key. Try again!\n"
			continue
			
		p2Choice = getpass.getpass(prompt = "\n" + player2 + " , it is your turn: ", stream = None)
		if p2Choice not in inputs:
			print "Invalid key. Try again!\n"
			continue
		else:
			if p1Choice == p2Choice:
				print "\nDRAW!"
				menu()
			elif p1Choice == "r" and p2Choice == "s":
				p1Points += 1
				print "\n" + player1 + " wins!\n"
			elif p1Choice == "p" and p2Choice == "r":
				p1Points += 1
				print "\n" + player1 + " wins!\n"
			elif p1Choice == "s" and p2Choice == "p":
				p1Points += 1
				print "\n" + player1 + " wins!\n"
			else:
				p2Points += 1
				print "\n" + player2 + " wins!\n"
			
			print player1 + ": " + str(p1Points) + " | " + player2 + ": " + str(p2Points)
			print "\n-------------------------------------------"

selectNames()