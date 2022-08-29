"""An example of conditional (if-else) statement."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Great job! Have a wonderful day!")
else: 
    print("Sorry, you guessed incorrectly :(")
    print("You suck.")
 
 
print("Game over.")