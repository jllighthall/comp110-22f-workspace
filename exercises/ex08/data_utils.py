"""Dictionary related utility functions."""

__author__ = "730571564"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Reading the rows from filename making it into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(a_table: list[dict[str, str]], name: str) -> list[str]: 
    """Produces a list of strings of values in a single column."""
    list_of_names: list[str] = []
    for row in a_table:
        item: str = row[name]
        list_of_names.append(item)
    return list_of_names


def columnar(list_of_rows: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Tranform data of rows into a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = list_of_rows[0] 
    for column in first_row:
        result[column] = column_values(list_of_rows, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]: 
    """Produce dictionary with only the first rows of data as specified by the second parameter."""
    empty_dict: dict[str, list[str]] = {}
    for columns in table:
        i: int = 0
        list_of_values: list[str] = []
        if n > len(table[columns]):
            empty_dict[columns] = table[columns]
        else:
            while i < n:
                list_of_values.append(table[columns][i])
                i += 1
            empty_dict[columns] = list_of_values
    return empty_dict


def select(column_table: dict[str, list[str]], names_of_columns: list[str]) -> dict[str, list[str]]: 
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for names in names_of_columns:
        result[names] = column_table[names]      
    return result 


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a single dictionary from two ."""
    result: dict[str, list[str]] = {}
    for columns in table_1:
        result[columns] = table_1[columns]
    for the_columns in table_2:
        if the_columns in result:
            result[the_columns] += table_2[the_columns]
        else:
            result[the_columns] = table_2[the_columns]
    return result


def count(frequency: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears.""" 
    result: dict[str, int] = {}
    for items in frequency:
        if items in result:
            result[items] += 1 
        else:
            result[items] = 1
    return result 