# Challenge day 3 - Palindrom

phrase = str(input('Input the phrase to check if is a palindrom: ')).lower()

phrase = ''.join(letter for letter in phrase if letter.isalnum())

if phrase[0] == phrase[len(phrase) - 1]:
    result = print(phrase, "-> Its a palindrom")
else:
    result = print(phrase, "-> Its not a palindrom")
