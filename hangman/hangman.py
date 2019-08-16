import random

def get_new_word():
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def show_spaces(spaces):
    print(' '.join(spaces))


def get_input():
    return input('\nGuess your letter: ')


def store_letter(letter, li):
    if letter not in li:
        li.append(letter)


def update_spaces(letter, word, spaces):
    for i in range(len(word)):
        if letter == word[i]:
            spaces[i] = word[i]


def check_win(spaces, word):
    spaces = ''.join(spaces)
    if spaces == word:
        return True


def print_hang(n):
    gal = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        gal[2] = ['|  o ']
    if n < 5:
        gal[3] = ['| /  ']
    if n < 4:
        gal[3] = ['| / \\']
    if n < 3:
        gal[3] = ['| /|\\']
    if n < 2:
        gal[4] = ['| /  ']
    if n < 1:
        gal[4] = ['| / \\']
    for i in gal:
        print(''.join(i))


def start_game():
    print('\nWelcome to Hangman!')

    word = get_new_word()
    corrects = []
    fails = []
    spaces = ['_'] * len(word)
    word_guessed = False
    guesses = 6

    show_spaces(spaces)

    # print(word)

    while not word_guessed and guesses > 0:
        letter = get_input().upper()
        if letter not in word and letter not in fails:
            print('Incorrect!\n')
            guesses -= 1
            store_letter(letter, fails)
            print_hang(guesses)
        elif letter in corrects or letter in fails:
            print('\nLetter already typed. Try another one!\n')
        else:
            print('Correct!\n')
            update_spaces(letter, word, spaces)
            store_letter(letter, corrects)

        if check_win(spaces, word):
            print('\nYou Win!')
            word_guessed = True

        show_spaces(spaces)
        # print('\nCorrects: ', corrects)
        # print('Fails: ', fails)

    if input('Play again? y / n') == 'y':
        start_game()
    else:
        pass


start_game()
