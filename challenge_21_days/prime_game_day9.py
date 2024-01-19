# Challenge day 09 - Prime Number Game
import  os
import  random

os.system('clear')
exit = False
score = 0

while exit == False:
    randomNumber = random.randint(2, 100)
   
    print('\nIs the number', randomNumber, 'a prime number?')
    answer = int(input('1-True\n2-False\n3-Show score\n4-Exit program\nAnswer: '))

    isPrime =  all(randomNumber % i != 0 for i in range(2, int(randomNumber**0.5) + 1))
   
    if isPrime and answer == 1 or isPrime == False and answer == 2:
        print('Correct!')
        score += 1
    elif isPrime and answer == 2 or isPrime == False and answer == 1:
        print('Incorrect! You lost the game!')
        exit = True
    elif answer == 3:
        print('\nYour score:', score)
    elif answer == 4:
        exit = True
    else:
        raise ValueError("the option inputed is not valid")
