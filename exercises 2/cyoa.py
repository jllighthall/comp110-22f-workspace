"EX06 - Create Your Own Adventure."
__author__ = "730571564"

#needed global variables
from random import randint, random


player: str = ""
points: int = 0
game_mode: str = ""
#emojis 
green_emoji: str = "\U0001F7E9"
yellow_emoji: str = "\U0001F7E8" 
white_emoji: str = "\U00002B1C"  
clown_emoji: str = "\U0001F921"
won_emoji: str = "\U0001F973"
sad_emoji: str = "\U0001F972"

#Questions to ask
# How can I get lines 31 & 32 to run correctly? 

def main() -> None:
    """Entrypoint of the game."""
    greet()
    global round_number
    round_number = 0
    while round_number <= 10:
        print(f"=== Turn {round_number}/10 ===")
        player_guess: str = int(input(f"Hi {player} what is your guess? "))
        points += (player_points(player_guess))
        points += adjust_points(points)
        print(points)
        round_number += 1


#def the_players_input(input_str: str) -> int:
    #"""Evaluates players input to an integer value from a string. """
    #player_guess: str = input(f"Hi {player} what is your guess?")
    #int(player_guess)



def greet() -> None:
    """Welcoming statment and introductions."""
    global game_mode
    print("Hello and welcome to the integer guessing game, a game that tests your ability to guess integers.")
    player = input("To begin enter your name. ")
    yes_or_no: str = input(f"Nice to meet you {player}! Would you like me to explain the guidelines of the game? \n Type YES for yes I would like to play the game or \n NO for I would not like to play the game. ")
    if yes_or_no == "YES":
        game_mode = input("Great! There are two modes to this game: EASY and HARD. Which would you like to play?")
        if game_mode == "EASY":
            print("The game will produce an integer 1-100. Each time you guess an integer the game will give your feedback \n HIGHER = the number is high than the number you guessed \n LOWER = the number is lower than the number you guessed.")
        if game_mode == "HARD":
            print("The game will produce an integer 1-100. You will be given no hints to whether the number is higher or lower.")
        while game_mode != "EASY" and game_mode != "HARD":
            game_mode = (f"Im sorry {player} was that EASY or HARD? ")
    if yes_or_no == "NO":
        print(f"Oh no, I though we were friends {player}" + sad_emoji + "!!")
        yes_or_no = input("Are you sure? Would you like to play my game?")
        print(points)
    while yes_or_no != "YES" and yes_or_no != "NO":
        yes_or_no = input(f"Im sorry {player} your answer was unclear" + sad_emoji + "could you please answer the question again? \n Would you like me to explain the guidelines of the game? \n Type YES for yes I would like to play the game or \n NO for I would not like to play the game.")


def player_points(z:int) -> None:
    """Assigns the players points."""
    #if game_mode == "HARD":
    #   points += 5
    #  print("Bonus points for HARD mode, you need it!")
    global game_mode
    random_integer: int = randint(1,100)
    
    if game_mode == "HARD" and round_number >= 10:
        if z == random_integer:
            print(f"Congratulations {player}!!!" + won_emoji + "You won!!!")
            points += 100
        else: 
            print(f"Sorry {player}" + sad_emoji + "your answer was not correct.")
    if game_mode == "EASY" and round_number >= 10:
        if z == random_integer:
            print(f"Congratulations {player}!!!" + won_emoji + "You won!!!")
            points += 100
        else:
            if random_integer > z:
                print(f"Sorry {player}" + sad_emoji + "your answer was not correct, guess HIGHER next round!")
            if random_integer < z:
                print(f"Sorry {player}" + sad_emoji + "your answer was not correct, guess LOWER next turn!")

    

def adjust_points(a:int) -> int:
    """Adjusts the players points."""
    heads_or_tails: str = input(f"Hi {player}, for extra points guess HEADS or TAILS. If you guess correctly you'll gain 1-10 bonus points.")
    answer: str = ""
    random_number: int = randint(0,100)
    if 50 >= random_number >= 0:
        answer += "HEADS"
    if 100 >= random_number >= 51:
        answer += "TAILS"
    bonus_points: int = randint(1,10)
    if heads_or_tails == "HEADS" and answer == "HEADS":
        print(f"Great job {player} you just won {bonus_points} bonus points!")
        a += bonus_points
    if heads_or_tails == "TAILS" and answer == "TAILS":
        print(f"Great job {player} you just won {bonus_points} bonus points!")
        a += bonus_points
    if heads_or_tails == "HEADS" and answer != "HEADS":
        a += 0
        print(f"Sorry {player} the answer was {answer}" + sad_emoji)
    if heads_or_tails == "TAILS" and answer != "TAILS":
        a += 0
        print(f"Sorry {player} the answer was {answer}" + sad_emoji)
    return a


if __name__ == "__main__":
    main()