""""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730571564"


number_of_letters_in_wordleword: int = 5
indices_counter: int = 0

wordle_word: str = input("Enter a 5-character word: ")

if len(wordle_word) != number_of_letters_in_wordleword:
    print("Error word must contain 5 letters. ") 
    exit()


"""first letter"""

wordle_word_1: str = input("Enter a single character: ")

letter_entered: int = 1
if len(wordle_word_1) != letter_entered:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + wordle_word_1 + " in " + wordle_word)

if wordle_word_1 == wordle_word [0]:
    print( wordle_word_1 + " found at index 0")
    indices_counter = int(indices_counter + 1)

if wordle_word_1 == wordle_word [1]:
    print( wordle_word_1  + " found at index 1")
    indices_counter = int(indices_counter + 1)

if wordle_word_1 == wordle_word [2]:
    print( wordle_word_1  + " found at index 2")
    indices_counter = int(indices_counter + 1)

if wordle_word_1 == wordle_word [3]:
    print( wordle_word_1  + " found at index 3")
    indices_coutner = int(indices_counter + 1)

if wordle_word_1 == wordle_word [4]:
    print( wordle_word_1  + " found at index 4")
    indices_counter = int(indices_counter + 1)


print(str(indices_counter) + " instance(s) of " + wordle_word_1 + " found in " + wordle_word )

