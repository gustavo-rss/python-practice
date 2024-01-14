# Challenge day 4 - Word counter

phrase = str(input('Input the phrase to count the words: '))

phrase_split = phrase.split()

print(phrase, "-> the phrase contains", len(phrase_split), "words.")