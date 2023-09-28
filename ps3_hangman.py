import string
import random

def loadWords():
    with open('words.txt', 'r') as file:
        words = file.read().split()
    return words

def chooseWord(wordList):
    return random.choice(wordList)

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_'
    return guessedWord

def getAvailableLetters(lettersGuessed):
    alphabet = string.ascii_lowercase
    availableLetters = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters

def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    
    lettersGuessed = []
    mistakesMade = 0
    maxMistakes = 8
    
    while True:
        print("-------------")
        print("You have {} guesses left.".format(maxMistakes - mistakesMade))
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters: {}".format(availableLetters))
        
        guess = input("Please guess a letter: ").lower()
        
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed.append(guess)
            mistakesMade += 1
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won! The word was {}.".format(secretWord))
            break
        
        if mistakesMade == maxMistakes:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
            break

if __name__ == "__main__":
    wordList = loadWords()
    secretWord = chooseWord(wordList).lower()
    hangman(secretWord)
