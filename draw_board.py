def get_integer(help_text):
    return int(input(help_text))


def draw_board(width, height):
    for l in range(height):
        print(' --- ' * width)
        print('|   |' * width)
    print(' --- ' * width)


w = get_integer('Quantas casas o tabuleiro deve ter de largura?')

h = get_integer('Quantas casas o tabuleiro deve ter de altura?')

draw_board(w, h)
