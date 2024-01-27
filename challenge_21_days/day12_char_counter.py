# Challenge day 12 - Char counter
import  os


os.system('clear')

count_list = {}

phrase = str(input('Input the phrase to count the words: ')).lower()

for char in phrase:
    if char.isalpha():
        count_list[char] = count_list.get(char, 0) + 1

for char, count in count_list.items():
        print(f'Char {char} appears {count} times')
    
