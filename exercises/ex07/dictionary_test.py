"""Unit testing the dictionary file in ex07!"""

__author__ = "730571564"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert() -> None:
    """Tests if list inverts properly."""
    megs_favorites: dict[str, str] = {"color": "blue", "animal": "cat", "sport": "football"}
    assert invert(megs_favorites)


def test_invert_twice() -> None:
    """Tests if list inverts properly."""
    my_favorites: dict[str, str] = {"color": "green", "animal": "cat", "sport": "baseball"}
    assert invert(my_favorites)


def test_invert_again() -> None:
    """Tests if list inverts properly."""
    yes_or_no_or_maybe: dict[str, str] = {"Black": "Yes", "Yellow": "Maybe", "Black and Yellow": "Yes", "Orange": "No"}
    assert invert(yes_or_no_or_maybe)


def test_favorite_color() -> None:
    """Test if most prevalent color is returned."""
    yay_colors: dict[str, str] = {"megan": "blue", "syd": "blue", "me": "green", "mb": "blue", "dan": "blue"}
    assert favorite_color(yay_colors)


def test_favorite_color_twice() -> None:
    """Test if most prevalent color is returned."""
    second_favorites: dict[str, str] = {"megan": "black", "syd": "green", "me": "black", "mb": "black", "dan": "orange"}
    assert favorite_color(second_favorites)


def test_favorite_color_again() -> None:
    """Test if most prevalent color is returned."""
    naming_the_rainbow: dict [str, str] = {"1": "red", "2": "orange", "3": "yellow", "4": "green", "5": "blue", "6": "violet"}
    assert favorite_color(naming_the_rainbow)


def test_count() -> None:
    """Test if key of dictionary is properly counted."""
    yay_colors: list[str] = ("blue", "blue", "green", "blue", "blue")
    assert count(yay_colors)

def test_count_twice() -> None:
    """Test if key of dictionary is properly counted."""
    second_favorites: list[str] = ("black", "green", "black", "black", "orange")
    assert count(second_favorites)

def test_count_again() -> None:
    """Test if key of dictionary is properly counted."""
    bday_month: list[str] = ("july", "july", "april", "april", "may", "september", "september", "july", "december")
    assert count(bday_month)