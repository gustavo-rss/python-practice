# Challenge day 8 - List
import  os

exit = False
user_list = []


while exit == False:
    option = str(input('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n1 - Add an item to the list \n2 - Remove an item from the list\n3 - Print the list\n4- Exit the list program\nInput the option of the desired operator: '))
    os.system('clear')
    
    if option == '1':
        os.system('clear')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        user_list.append(input('Input the item to be added: '))
        
    elif option == '2':
        os.system('clear')  
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        remove_item = int(input('Input the item to be removed: '))
        
        if  remove_item >= len(user_list):
            print('this item is not in the list')
        else:
            print(user_list[remove_item], 'is removed')
            user_list.pop(remove_item)
            
    elif option == '3':
        os.system('clear')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        
        if user_list == []:
            print('the list is empty')
        else:
            print(list(enumerate(user_list)))
            
    elif option == '4':
        exit = True
    else:
        raise ValueError("the option inputed is not valid")


