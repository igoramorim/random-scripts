string1 = raw_input("")
print "String: " + string1

#if string.endswith("r"):
#	print "ok"
#else:
#	print "fail"

#get the last letter
#output = string[-1]

#remove the last letter
#string = string [:-1]

print "Last letter: " + string1[-1]

string2 = raw_input("")

if string2.startswith(string1[-1]):
	print "ok"
else:
	print "fail"