# Challenge day 2 - Calculator

def calculator  (number1, number2, operator):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == 'x' or operator == '*':
        result = number1 * number2
    elif operator == '/':
        if number2 == 0:
            result = "0 is not divisible"
        else: 
            result = int(number1 / number2)
    else:
        raise ValueError("the operator inputed is not valid")
        
    return print(number1, operator, number2, "->", result)
    

number1 = int(input('Input the first number: '))
operator = str(input('Input the operator among +, -, x, * or / : '))   
number2 = int(input('Input the second number: '))

calculator(number1, number2, operator)
