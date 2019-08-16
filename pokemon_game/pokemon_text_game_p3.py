import os

pokedex = []

filepath = os.path.dirname(os.path.abspath(__file__)) + "\pokedex.txt"
dir = os.path.dirname(filepath)

if not os.path.exists(dir):
        os.makedirs(dir)

with open(filepath) as f:
	for line in f:
		# line[:-1] retira a "\n" que fica apos ler a linha do txt > abra\n > abra
		pokedex.append(line[:-1].lower())

f.closed

pokemon1 = input("Pokemon: ").lower()

# remove o pokemon digitado da lista
pokedex.remove(pokemon1)

# mostra ao jogador a ultima letra do pokemon digitado
print("Ultima letra: " + pokemon1[-1])

# enquanto a lista pokedex estiver com algum pokemon o jogo continua
while pokedex:
	print("\n")

	pokemon2 = input("Pokemon: ").lower()

	# se o pokemon2 comecar com a ultima letra do pokemon1 e estiver dentro da lista pokedex
	if pokemon2.startswith(pokemon1[-1]) and pokedex.count(pokemon2) == 1:

		# mostra que o jogador acertou, remove o pokemon2 da lista pokedex e atualiza o pokemon1
		print("Certinho! Continua...")
		pokedex.remove(pokemon2)
		pokemon1 = pokemon2

		# esse for e necessario para contar quantos pokemons estao disponiveis da lista pokedex iniciando com a letra da rodada
		initial_letter_counter = 0
		for p in pokedex:
			if p.startswith(pokemon1[-1]):
				initial_letter_counter += 1

		# se nao houver pokemon disponivel, significa fim de jogo
		if initial_letter_counter == 0:
			print("Fim de jogo. Nao ha pokemons disponiveis com essa letra.")
			break
		else:
			# se houver pokemons disponiveis com a letra da rodada, mostra ao jogador essa quantidade
			print("Ultima letra: " + pokemon1[-1] + " | Pokemons disponiveis com essa letra: " + str(initial_letter_counter))
	else:
		# se o jogador erra o nome do pokemon ou digita um pokemon que ja foi usado, ou seja, fora da lista, pede para o jogador sair da brincadeira e o proximo continua
		print("Errou! Pokemon fora da lista! Saia da brincadeira!")
		print("Ultima letra: " + pokemon1[-1])

		