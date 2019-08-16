import os

initial_letter_counter = 0
pokedex = []

filepath = "C:/Users/Igor/Downloads/python/pokemon_game/test.txt"
dir = os.path.dirname(filepath)

if not os.path.exists(dir):
        os.makedirs(dir)
        
with open(filepath) as f:
        #print (f.read())
        for line in f:
                #print line
				pokedex.append(line[:-1].lower())

f.closed

print pokedex

pokemon1 = raw_input("Pokemon: ").lower()
pokedex.remove(pokemon1)
print "Ultima letra: " + pokemon1[-1]

for p in pokedex:
	if p.startswith(pokemon1[-1]):
		initial_letter_counter += 1
		
print initial_letter_counter