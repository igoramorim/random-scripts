def histogram(*args):
	for i in args:
		for x in range(i):
			print "*",
		print "\n"

histogram(3,2,5,7,10)