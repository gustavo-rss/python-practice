# Challenge day 13 - E-mail validator
import  os
import  re

os.system('clear')

email = str(input('Input the e-mail to be validated: '))
regex = re.compile(r'^(?:[A-Za-z0-9]+)+(?:[A-Za-z0-9]+(?:[.-_]?[A-Za-z0-9]+)*)+\@(?:[A-Za-z0-9]+(?:[.-]?[A-Za-z0-9]+)*\.)+[A-Z|a-z]{2,}$')

if re.fullmatch(regex, email):
    print('Inputed e-mail:', email,'\nExpected result: Valid e-mail')
else:
    print('Inputed e-mail:', email,'\nExpected result: Invalid e-mail')
    
    