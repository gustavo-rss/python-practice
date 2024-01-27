# Challenge day 14 - Password Generator
import random
import string
import  os


os.system('clear')

defined_lenght = 0
contains_numbers = 0
contains_upper = 0
contains_lower = 0
contains_special = 0

def passwordGenerator  (defined_lenght, contains_numbers, contains_upper, contains_lower, contains_special):
    print('------ PASSWORD GENERATOR -----')
    password = ''
    
    defined_lenght = int(input('Input the desired lenght: '))   
    while defined_lenght <= 0:
        print('Input a lenght higher than 0')
        defined_lenght = int(input('Input the desired lenght: '))   
    if defined_lenght > 0:
            if defined_lenght > len(password):  contains_numbers = int(input('Want it to contain numbers? 1- YES 2- NO :  '))
            while contains_numbers != 1 and contains_numbers != 2:
                print("the option inputed is not valid")
                contains_numbers = int(input('Want it to contain numbers? 1- YES 2- NO :  '))
            if contains_numbers == 1:   password+= random.choice(string.digits)
            
            if defined_lenght > len(password): contains_upper = int(input('Want it to contain upper case? 1- YES 2- NO :  '))
            while contains_upper != 1 and contains_upper != 2:
                print("the option inputed is not valid")
                contains_upper = int(input('Want it to contain upper case? 1- YES 2- NO :  '))
            if contains_upper == 1: password+= random.choice(string.ascii_uppercase)    
                
            if defined_lenght > len(password):  contains_lower = int(input('Want it to contain lower case? 1- YES 2- NO :  '))
            while contains_lower != 1 and contains_lower != 2:
                print("the option inputed is not valid")
                contains_lower = int(input('Want it to contain lower case? 1- YES 2- NO :  '))
            if contains_lower == 1: password+= random.choice(string.ascii_lowercase)
            
            if defined_lenght > len(password):  contains_special = int(input('Want it to contain special characters? 1- YES 2- NO :  '))
            while contains_special != 1 and contains_special != 2:
                print("the option inputed is not valid")
                contains_special = int(input('Want it to contain special characters? 1- YES 2- NO :  '))
            if contains_special == 1:   password+= random.choice(string.punctuation)

            while defined_lenght > len(password):
                if contains_numbers == 1:  password+= random.choice(string.digits)
                if defined_lenght > len(password):  
                    if contains_upper == 1: password+= random.choice(string.ascii_uppercase)
                if defined_lenght > len(password):
                    if contains_lower == 1: password+= random.choice(string.ascii_lowercase)
                if defined_lenght > len(password):
                    if contains_special == 1:   password+= random.choice(string.punctuation)        
    return print('Generated password:', password, 'has the lenght of', len(password))
    

passwordGenerator(defined_lenght, contains_numbers, contains_upper, contains_lower, contains_special)



 