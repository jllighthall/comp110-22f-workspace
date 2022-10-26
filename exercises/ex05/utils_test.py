"""Unit Testing 'list' Utility Functions Ex05!"""

__author__ = "730571564"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens() -> None:
    """Tests if the numbers in data set given are even, returning the even numbers."""
    given_list: list[int] = [1, 5, 6, 8, 9]
    assert only_evens(given_list)


def test_only_evens_twice() -> None:
    """Tests if the numbers in data set given are even, returning the even numbers."""
    given_list: list[int] = [82, 36, 41, 97, 54]
    assert only_evens(given_list)


def test_only_evens_again() -> None:
    """Tests if the numbers in data set given are even, returning the even numbers."""
    given_list: list[int] = [47, 66, 98, 3, 44]
    assert only_evens(given_list)


def test_concat() -> None:
    """Creates a list from 2 lists listing the values from 1st list and then values from second list."""
    first_list: list[int] = [-29, 6, 30, 86, -45]
    second_list: list[int] = [77, -58, 30, -72, -82]
    assert concat(first_list, second_list)


def test_concat_twice() -> None:
    """Creates a list from 2 lists listing the values from 1st list and then values from second list."""
    first_list: list[int] = [10, 20, 30, 40, 50]
    second_list: list[int] = [60, 70, 80, 90, 100]
    assert concat(first_list, second_list)  


def test_concat_again() -> None:    
    """Creates a list from 2 lists listing the values from 1st list and then values from second list."""
    first_list: list[int] = [12, 14, 16, 18, 20]
    second_list: list[int] = [21, 23, 25, 27, 29]
    assert concat(first_list, second_list)  


def test_sub() -> None:
    """Creates a list from a given range of indexes inside a given list."""
    another_list: list[int] = [6, 7, 4, 5, 83, 6]
    assert sub(another_list, 2, 3)


def test_sub_twice() -> None:
    """Creates a list from a given range of indexes inside a given list."""
    another_list: list[int] = [4, 8, 12, 16, 20, 24, 28]
    assert sub(another_list, 1, 3)


def test_sub_again() -> None:
    """Creates a list from a given range of indexes inside a given list."""
    another_list: list[int] = [10, 20, 30, 40]
    assert sub(another_list, 0, 2)