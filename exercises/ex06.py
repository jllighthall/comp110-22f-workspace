
# make use of f-strings

# use random library 
from random import random

# make liberal use of emojis 
green_emoji: str = "\U0001F7E9"
yellow_emoji: str = "\U0001F7E8" 
white_emoji: str = "\U00002B1C"  
clown_emoji: str = "\U0001F921"
won_emoji: str = "\U0001F973"
points: int = 0
player = player_name

def main() -> None:
    """Entrance to Game"""
    secret: list[int] = [guessing_list]
    greet()
    #number of turns allowed = 6 
    n = 0
    won = False
    while n <= 10 and won is False:
        print(f"=== Turn {n}/10 === ")
        user_input: int = players_list(input)
        print(game_emojified(guessing_list, user_input))
        print(players_points)
        if guessing_list == players_list: 
            print(f"You won {player} " + won_emoji + " !!!")
            won = True 
    if n > 10:
        print(f"X/10 - Sorry {player} you are a" + clown_emoji+ "maybe try again tomorrow?! ")
# Improve the docstring 
# Intodruce a "game loop"


def greet() -> None:
    """Welcome statement."""
    # dont understand why this isnt working properly 
    global player_name
    player_name: str = input("Hello! Welcome to the List Integer Game, where you test your luck at guessing a series of integers. What is your name? ")
    
    #want_enter_game: str = input("Hello, would you like to play a game? \n press 1 for YES and 2 for NO. ")
    #a: int = int(want_enter_game)

    #while a != 1 or 2:
      #  want_enter_game = input("Im sorry your answer wasn't clear ): would you like to play a game? \n press 1 for YES and 2 for NO. ")
     #   a = int(want_enter_game)
    #else:
        #if a == 2:
           # print("Are you sure? I would really like for you to play my game.")
          #  want_enter_game == 1
         #   print("Sorry you have no choice ):")
        #if a == 1:
    #print(f"Hello {player} welcome to the List Integer Guessing Game! \n The game will produce a list of random integers, \n positive or negative from -100 to 100. \n The game will then prompt you to guess a number.")
    #print("You will be granted" +  +"if the integer is in the correct position \n a" + + "if the number is within the list but in the incorrect position \n and a" + + "if the integer is not present within the game's random generated list"   )
    #print(green_emoji + "= 7 points \n" + yellow_emoji + " = 3 points \n" + white_emoji + " = 0 points")
    return player


def game_emojified(list_of_game: list[int], list_of_player:list[int]) -> str:
    """Checks random list for users input, assigning emojis along the way."""
    emoji: str = ""
    i: int = 0
    while len(list_of_player) > i:
        #if the first index at the games list = the first index at the players list GREEN EMOJI
        if list_of_game[i] == list_of_player[i]:
            emoji += green_emoji
        #other wise we will be assigning a yellow or white emoji 
        else:
            j: int = 0
            is_in: bool = False
            while j < len(list_of_game) and is_in == False:
                if list_of_game[i] ==list_of_player[j]:
                    is_in = True
                else:
                    j += 1
            if is_in:
                emoji += yellow_emoji
            else: 
                emoji += white_emoji
    i += 1
    return emoji


def players_points() -> int: 
    """Assigns players points based on emojis."""
    i = 0
    while len(game_emojified) > i:
        if game_emojified[i] == green_emoji:
            points += 7
        if game_emojified[i] == yellow_emoji:
            points += 3
        if game_emojified[i] == yellow_emoji:
            points += 0
        i += 1
    return points


def players_list(a:int) -> list[int]:
    """Gets input from player to create a list to compare with random list."""
    number_in_sequence: int = 0
    appended_players_list: list[int] = []
    while number_in_sequence <= 5:
        a = input(f"What is the number at index {number_in_sequence} in the sequence?")
        while len(a) == 0:
            a = input(f"What is the number at index {number_in_sequence} in the sequence?")
        number_in_sequence += 1
        appended_players_list.append(a)
    return appended_players_list


def guessing_list() -> list[int]:
    """Given random integers produces a list appending that integer along with the number half its value."""
    game_list: list[int] = []
    a: int = random.randint(-10, 10)
    game_list.append(a)
    a = a%2
    game_list.append(a)
    b: int = random.randint(-10, 10)
    game_list.append(b)
    b = b%2
    game_list.append(b)
    c: int = random.randint(-10, 10)
    game_list.append(c)
    c = c%2
    game_list.append(c)
    
    return game_list


if __name__ == "__main__":
    main()

