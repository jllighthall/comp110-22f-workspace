"""ex07 - Dictionary."""

__author__ = "730571564"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    inverted_dictionary: dict[str, str] = dict()

    for key in dictionary:
        for a in inverted_dictionary:
            if a == dictionary[key]:
                raise KeyError("Error!")
        inverted_dictionary[dictionary[key]] = key
    return inverted_dictionary
    
        
def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns most prevalent color."""
    i: int = 0
    most_color: str = ""
    counting_colors: dict[str, int] = dict()
    color_counter_list: list[str] = list()
    list_of_numbers: list[int] = list()
    for names in names_colors:
        color_counter_list.append(names_colors[names])
    counting_colors = count(color_counter_list)
    for colors in counting_colors:
        list_of_numbers.append(counting_colors[colors])
        maximum: int = list_of_numbers[0]
        while i < len(list_of_numbers):
            if list_of_numbers[i] > maximum:
                maximum = list_of_numbers[i]
            i += 1
            if counting_colors[colors] == maximum:
                most_color += colors
    return most_color


def count(given_list: list[str]) -> dict[str, int]:
    """Counts the items in a list, creating a dictionary."""
    build_dict: dict[str, int] = dict()
    i: int = 0
    for string in given_list:
        if string in build_dict:
            build_dict[string] += 1
        else:
            build_dict[string] = 1
        i += 1
    return build_dict
        
