number = 25

running = True

while running:
    guess = int(input('Enter an integer: '))

    if guess == number:

        print('You guessed it right! ')
        running = False

    elif guess < number:
        print('No it is a little higher than that. ')

    else:
        print('No it is a little lower than that. ')

else:
    print('The while loop is over')

