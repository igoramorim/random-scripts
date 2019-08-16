# def check_game(game):
#     print('Hor', check_hor(game[0], game[1], game[2]))
#     print('---')
#     print('Vert', check_vert(game[0], game[1], game[2]))
#     print('---')
#     print('Diag', check_diag(game[0], game[1], game[2]))
#
#
# def check_hor(l1, l2, l3):
#     if 0 not in l1 or 0 not in l2 or 0 not in l3:
#         if l1[0] == l1[1] and l1[0] == l1[2]:
#             return l1[0]
#         elif l2[0] == l2[1] and l2[0] == l2[2]:
#             return l2[0]
#         elif l3[0] == l3[1] and l3[0] == l3[2]:
#             return l3[0]
#         else:
#             return False
#     return False
#
#
# def check_vert(l1, l2, l3):
#     if 0 not in l1 or 0 not in l2 or 0 not in l3:
#         if l1[0] == l2[0] and l1[0] == l3[0]:
#             return l1[0]
#         elif l1[1] == l2[1] and l1[1] == l3[1]:
#             return l1[1]
#         elif l1[2] == l2[2] and l1[2] == l3[2]:
#             return l1[2]
#         else:
#             return False
#     return False
#
#
# def check_diag(l1, l2, l3):
#     if 0 not in l1 or 0 not in l2 or 0 not in l3:
#         if l1[0] == l2[1] and l1[0] == l3[2]:
#             return l1[0]
#         elif l1[2] == l2[1] and l1[2] == l3[0]:
#             return l1[2]
#         else:
#             return False
#     return False


def checkGrid(grid):
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


game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_11 = [[0, 2, 0],
	[2, 1, 0],
	[1, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


gameX = [['', '', ''],
	['', '', ''],
	['', '', '']]

print(gameX)
print(checkGrid(gameX))
