print('\nHi, I am the computer. Think a number between 0 and 100 and I will guess it!\n')

n_min = 0
n_max = 100
middle = 50
guesses = 0

while n_min <= n_max:
    guesses = guesses + 1
    middle = (n_min + n_max)//2

    answer = input('Is your number ' + str(middle) + '?\n1 - Yes\n2 - Too high\n3 - Too low\n')

    if answer == '1':
        print('\nGotcha!\nTotal guesses: ', guesses)
        break
    elif answer == '2':
        n_max = middle - 1
    elif answer == '3':
        n_min = middle + 1
    else:
        print('Try again.')



    # if target == middle:
    #     print(middle)
    #     break
    #
    # if target < middle:
    #     n_max = middle - 1
    # else:
    #     n_min = middle + 1
