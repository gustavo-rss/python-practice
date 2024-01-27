# Challenge day 10 - Guessing game
import  os
import  random

os.system('clear')
exit = False
score = 0
secretNumber = random.randint(1, 100)
chances = 7

while exit == False:   
    print('\nGuess what is the number secret number')
    answer = int(input('1-Take a guess\n2-Show score\n3-Reset score\n4-Exit program\nAnswer: '))
    
   
    if answer == 1:
        guess = int(input('\nYour guess: '))
        if guess == secretNumber:
            chances -= 1
            print('Correct! It took you', 7 - chances,'chances')
            score += 1
            chances = 7
        elif guess != secretNumber:
            chances -= 1
            if chances == 0:
                print('Your chances are over! You lost the game! The secret number was:', secretNumber)
                exit = True
            if guess > secretNumber:
                print('Your guess', guess, 'is higher than the secret number\nYou got', chances,'chances left')
            elif guess < secretNumber:
                print('Your guess', guess, 'is lower than the secret number\nYou got', chances,'chances left')
    elif answer == 2:
        print('\nYour score:', score)
    elif answer == 3:
        score = 0
        print('\nYour new reset score is:', score)
    elif answer == 4:
        exit = True
    else:
        print("\nThe option inputed is not valid")
