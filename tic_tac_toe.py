def check_grid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0


def draw_board(game):
    print('\n  1    2    3')
    for i in range(3):
        print(' --- ' * 3)
        print('| ' + str(game[i][0]) + ' || ' + str(game[i][1]) + ' || ' + str(game[i][2]) + ' | ' + str(i+1))
    print(' --- ' * 3)


def get_input():
    choice = input("\nEscolha a posicao da peca.\nLinha e coluna. Separadas por ,\nEx: 3,1\n\n")
    pos = choice.split(',')
    pos = list(map(int, pos))
    if check_input(pos):
        return pos
    else:
        get_input()


def check_input(pos):
    # TODO: verify string inputs,  out of range indexes and already used grids
    for i in pos:
        if type(i) is int:
            return True
        else:
            return False


def update_game(pos, piece):
    game[pos[0]-1][pos[1]-1] = piece


game = [[' ', ' ', ' '],
	[' ', ' ', ' '],
	[' ', ' ', ' ']]


is_p1 = True
has_winner = False

draw_board(game)

while not has_winner:
    pos = get_input()

    if is_p1:
        update_game(pos, 'X')
    else:
        update_game(pos, 'O')

    draw_board(game)

    if check_grid(game) != ' ':
        print('\nO vencedor e: ' + check_grid(game))
        has_winner = True

    is_p1 = not is_p1
