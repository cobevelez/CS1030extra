import random

start_game = True
#computer chooses 1-10
#ran_num = random.randint(1,10)
#guess = int(input('The computer has selected a number between 1-10. Guess what the number is:'))

while start_game:
    ran_num = random.randint(1,10)

    guess_num = 0
    win = False

    while not win:
        try:
            guess = int(input('The computer has selected a number between 1-10. Guess what the number is: '))

        except ValueError:
            print('Invalid number')
            continue

        guess_num += 1
#if statement
        if guess == ran_num:
            print('You got it! The number was ', ran_num)
            print('You guessed the number in ', guess_num,' attepmts.')

            win = True

        elif guess > ran_num:
            print('too high')

        else:
         print('too low')
#allow user to replay
    play_again = input('Play again? (yes or no) ')
    if play_again != 'yes':
        start_game = False

    print('Game over')













#print(ran_num)