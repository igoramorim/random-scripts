#Isso e um comentario. Toda linha iniciada com "#" nao e lida como comando pelo computador. Usamos comentarios para explicar o codigo.
#Atividade feita com o intuito de mostrar pequenos jogos feitos em python para os alunos da SuperGeeks Alphaville.
#O codigo nao esta otimizado, pois acredito que dificultaria o entendimento inicial.
#Sinta-se livre para modifica-lo e estuda-lo.
#Agradecimento especial ao aluno Caua Kencis por ter me ajudado com a lista de pokemons do arquivo pokedex.txt :D
#E possivel adaptar o tema do jogo facilmente, simplesmente trocando o conteudo do arquivo txt. Por exemplo, com nomes de animais.

#Para funcionar corretamente, o arquivo pokedex.txt deve estar na mesma pasta desse arquivo.

#Divirta-se! -Igor Amorim :D~


#import necessario para ler o arquivo txt com os pokemons
import os

#lista onde ira ficar os pokemons do txt
pokedex = []

#variaveis relacionadas a leitura do txt
filepath = os.path.dirname(os.path.abspath(__file__)) + "\pokedex.txt"
dir = os.path.dirname(filepath)

if not os.path.exists(dir):
        os.makedirs(dir)

#abre o txt e passa todos os pokemons para a lista pokedex[]        
with open(filepath) as f:
        for line in f:
				#line[:-1] retira a "\n" que fica apos ler a linha do txt > abra\n > abra
				pokedex.append(line[:-1].lower())

f.closed                
#pede para o jogador digitar o primeiro pokemon
pokemon1 = raw_input("Pokemon: ").lower()
#remove o pokemon digitado da lista
pokedex.remove(pokemon1)
#mostra ao jogador a ultima letra do pokemon digitado
print "Ultima letra: " + pokemon1[-1]
#enquanto a lista pokedex estiver com algum pokemon o jogo continua
while pokedex:
	#print "\n" para pular uma linha
	print "\n"
	#pede para o jogador digitar o segundo pokemon
	pokemon2 = raw_input("Pokemon: ").lower()
	#se o pokemon2 comecar com a ultima letra do pokemon1 e estiver dentro da lista pokedex
	if pokemon2.startswith(pokemon1[-1]) and pokedex.count(pokemon2) == 1:
		#mostra que o jogador acertou, remove o pokemon2 da lista pokedex e atualiza o pokemon1
		print "Certinho! Continua..."
		pokedex.remove(pokemon2)
		pokemon1 = pokemon2
		#esse for e necessario para contar quantos pokemons estao disponiveis da lista pokedex iniciando com a letra da rodada
		initial_letter_counter = 0
		for p in pokedex:
			if p.startswith(pokemon1[-1]):
				initial_letter_counter += 1
		#se nao houver pokemon disponivel, significa fim de jogo
		if initial_letter_counter == 0:
			print "Fim de jogo. Nao ha pokemons disponiveis com essa letra."
			#comando break para a execucao do loop while
			break
		else:
			#se houver pokemons disponiveis com a letra da rodada, mostra ao jogador essa quantidade
			print "Ultima letra: " + pokemon1[-1] + " | Pokemons disponiveis com essa letra: " + str(initial_letter_counter)
	else:
		#se o jogador erra o nome do pokemon ou digita um pokemon que ja foi usado, ou seja, fora da lista, pede para o jogador sair da brincadeira e o proximo continua
		print "Errou! Pokemon fora da lista! Saia da brincadeira!"
		print "Ultima letra: " + pokemon1[-1]

		