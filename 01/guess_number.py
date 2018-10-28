print('Welcome!')
guess = 0
while guess != 5:
    user_guess = input('Guess a number: ')
    guess = int(user_guess)
    if guess == 5:
        print('You win!')
    else:
        if guess > 5:
            print('Too high')
        else:
            print('Too low')
print('Game over')
