


secret: str = "python"

green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
white_box: str = "\U00002B1C"

# want user to put in an input 
wordle_word: str = input("What is your 6-letter guess? ")
i: int = 0
guess: str = ""


while len(wordle_word) != len(secret):
    wordle_word = input("That was not 6 letters! Try again:")   

while i < len(wordle_word):
    if wordle_word[i] == secret[i]:
        guess += green_box
    else:
        j: int = 0
        is_in: bool = False
        while j < len(wordle_word) and is_in == False:
            if wordle_word[i] == secret[j]:
                is_in = True
            else: 
                j += 1
        if is_in:
            guess += yellow_box
        else:
            guess += white_box
    i += 1
print(guess)
if wordle_word == secret:
    print("Woo! You got it!")     
else: 
    print("Not quite. Play again soon!")
