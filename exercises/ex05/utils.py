"""'list' Utility Functions Ex05!"""

__author__ = "730571564"


def only_evens(given_list: list[int]) -> list[int]:
    """Checks for and returns the even numbers of a list."""
    i: int = 0
    even_numbers: list = []
    while len(given_list) > i:
        if (given_list[i]) % 2 == 0:
            even_numbers.append(given_list[i])
        i += 1 
    return even_numbers


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Concatinates the first list with the second list following it."""
    i: int = 0
    j: int = 0
    concatenated_list: list = []
    while i < len(first_list):
        concatenated_list.append(first_list[i])
        i += 1
    while len(second_list) > j:
        concatenated_list.append(second_list[j])
        j += 1

    return concatenated_list

    
def sub(another_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a subset list from the given list."""
    subset_list: list = []


# return the empty list if...
# If the length of the list is 0
    if len(another_list) == 0:
        return subset_list
# start is greater than or equal the length of the list
    if start_index >= len(another_list):
        return subset_list
# end is at most 0
    if end_index < 0:
        return subset_list
#index is greater than length of list end with end of list
    if end_index > len(another_list):
        end_index == len(another_list)
# start index negative start from beginning of list
# question to ask: are we allowed to alter the parameter values?
    if start_index < 0:
        start_index = 0
    
    i: int = 0
    while i < end_index:
        subset_list.append(another_list[i])
        i += 1   
    return subset_list  