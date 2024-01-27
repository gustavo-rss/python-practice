# Challenge day 6 - Unit of measure converter

def converter  (option, number):
    if option == '1':
        conversion = number * 0.621371
        phrase = "Kilometers to Miles"
    elif option == '2':
        conversion = number * 1.60934
        phrase = "Miles to Kilometers"
    elif option == '3':
        conversion = number * 3.28084
        phrase = "Meters to Feets"
    elif option == '4':
        conversion = number * 0.3048
        phrase = "Feets to Meters"
    elif option == '5':
        conversion = number * 9/5 + 32
        phrase = "Celcius to Fahrenheit"
    elif option == '6':
        conversion =  (number - 32) * 5/9
        phrase = "Fahrenheit to Celcius"
    else:
        raise ValueError("the option inputed is not valid")
        
    return print("Converted", number, phrase, "-> Result:", conversion)
    

option = str(input('1 - Kilometers to Miles \n2 - Miles to Kilometers \n3 - Meters to Feets \n4 - Feets to Meters \n5 - Celcius to Fahrenheit \n6 - Fahrenheit to Celcius \nInput the option of the desired operator: '))   
number = int(input('Input the number to be converted: '))

converter(option, number)