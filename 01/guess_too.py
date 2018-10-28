from random import randint


secret = randint(1, 10)
print('Welcome!')
guess = 0
while guess != secret:
    user_guess = input('Guess the number: ')
    guess = int(user_guess)
    if guess == secret:
        print('You win!')
    else:
        if guess > secret:
            print('Too high')
        else:
            print('Too low')
print('Game over')
    
