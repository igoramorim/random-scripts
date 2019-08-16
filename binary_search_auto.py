import matplotlib.pyplot as plt

def bs(li):
    li_numbers = []
    li_guesses = []
    n = 0
    while n < len(li):
        n_min = li[0]
        n_max = li[-1]
        middle = len(li)/2
        target = li[n]
        guesses = 0
        while n_min <= n_max:
            guesses = guesses + 1
            middle = (n_min + n_max)//2

            if target == middle:
                print('\nNumber: ' + str(target) + '\tGuesses: ' + str(guesses))
                li_numbers.append(target)
                li_guesses.append(guesses)
                break
            elif target < middle:
                n_max = middle - 1
            elif target > middle:
                n_min = middle + 1
            else:
                print('Not found.')
                break
        n += 1

    plt.hist(li_guesses, bins=20)
    plt.show()


li = list(range(0, 101))
bs(li)
