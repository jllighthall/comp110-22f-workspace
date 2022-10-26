"""'list' Utility Functions."""

__author__ = "730571564"


def all(A: list[int], B: int) -> bool:
    """Checks numbers in list for matches of indicated number."""
    i: int = 0
    while len(A) > i:
        if A[i] != B:
            return False
        i += 1
    if len(A) == 0:
        return False   
    return True
        

def max(user_list_input: list[int]) -> int:
    """Returns the largest number in the list."""
    maximum: int = user_list_input[0]
    i = 0
    
    while i < len(user_list_input):
        if user_list_input[i] > maximum:
            maximum = user_list_input[i]
        i += 1
    return maximum

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Evaluating whether or not lists match exactly."""
    if first_list == second_list:
        return True
    else:
        return False
