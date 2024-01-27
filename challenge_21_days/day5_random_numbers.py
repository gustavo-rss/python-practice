# Challenge day 5 - Random numbers
from random import randint

numbers = []
while len(numbers) < 6:
    randomNumber = randint(1, 60)
    while randomNumber not in numbers:
        numbers.append(randomNumber)

print(numbers)        
 