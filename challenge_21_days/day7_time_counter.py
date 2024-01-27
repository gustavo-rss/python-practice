# Challenge day 7 - Time counter
import time

def counter  (option, number):
    if option == '1':
        i = 0
        while i < number:
            i+= 1
            time.sleep(1)
            print(i)
    elif option == '2':
        i = 1
        while i <= number:
            print(number)
            number-= i
            time.sleep(1)
    else:
        raise ValueError("the option inputed is not valid")

option = str(input('1 - Progressive counter \n2 - Regressive counter\nInput the option of the desired operator: '))   
number = int(input('Input the count number to be reached: '))

counter(option, number)