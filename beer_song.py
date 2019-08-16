import time
beers = 99

for x in range (beers):
	print (str(beers) + " bottles of beer on the wall, " + str(beers) + " bottles of beers.")
	beers -= 1
	print ("Take one down, pass it around, " + str(beers) + " bottles of beer on the wall\n")
	time.sleep(2)
