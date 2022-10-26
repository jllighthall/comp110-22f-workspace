"""Wordle."""

__author__ = "730571564"


def contains_char(searched_through: str, searched_for: str) -> bool:
    """Trying to find parameter 2 in parameter 1, to find indices matches."""
    assert len(searched_for) == 1

    i: int = 0
    while len(searched_through) > i:
        if searched_through[i] == searched_for:
            return True
        i += 1 
    return False
    

def emojified(guess: str, secret: str) -> str:
    """Assigning green, yellow, or white block emojis to assess validity of character."""
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8" 
    white_box: str = "\U00002B1C"  
    i: int = 0
    emoji: str = ""
    assert len(guess) == len(secret)

    while i < len(secret):
        if secret[i] == guess[i]:
            emoji += green_box
        else: 
            if contains_char(secret, guess[i]) is True: 
                emoji += yellow_box
            if contains_char(secret, guess[i]) is False:
                emoji += white_box
        i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Examining the number of letters within a guess and receiving the users input."""
    users_input: str = input(f"Enter a {expected_length} character word: ")
    
    while expected_length != len(users_input):
        users_input = (input(f"That wasn't {expected_length} chars! Try again: "))
    return users_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    n: int = 1
    won = False
    while n <= 6 and won is False:
        print(f"=== Turn {n}/6 === ")
        users_input: str = input_guess(len(secret))
        print(emojified(users_input, secret))
        if users_input == secret:
            print(f"You won in {n}/6 turns!")
            won = True 
        n += 1
    if n > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()