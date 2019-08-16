import os

#pokedex = ["p1", "p1", "p2", "p3", "p4"]
#print pokedex.count("p1")
pokedex = []

print pokedex
#pokedex.remove("p2")
print pokedex

filepath = "C:/Users/Igor/Downloads/python/pokemon_game/test.txt"
dir = os.path.dirname(filepath)


#print "Diretorio do test.txt ANTES: " + dir

if not os.path.exists(dir):
        os.makedirs(dir)
        
with open(filepath) as f:
        #print (f.read())
        for line in f:
                #print line
				pokedex.append(line[:-1].lower())

f.closed                
print pokedex

