"""Four functions that do different things regarding dictionary data types."""

__author__ = "730643202"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Swaps the keys and values at each point in the dictionary"""
    new_set: dict[str, str] = dict()
    for key in d:
        k: str = key
        v: str = d[key]
        new_set[v] = k
    return new_set


def count(list: list[str]) -> dict[str, int]:
    """Produce dictionary with words with number of times value is on list"""
    new_set: dict[str, int] = {}
    idx: int = 0
    while idx < len(list):
        if list[idx] in new_set:
            new_set[list[idx]] += 1
        else:
            new_set[list[idx]] = 1
        idx += 1
    return new_set


def favorite_color(colors: dict[str, str]) -> str:
    """Return most frequent color in a dictionary"""
    # Create a list with the individual color values
    list1: list[str] = []
    for key in colors:
        v: str = colors[key]
        list1.append(v)
    # Then return the dictionary by calling the count function
    list2: dict[str, int] = count(list1)
    # Then identify which color has the greatest numerical value in the list
    fav_color: str = list1[0]
    for key in list2:
        if list2[key] > list2[fav_color]:
            fav_color = key
    return fav_color


def bin_len(strings: list[str]) -> dict[int, list[str]]:
    """Bins a list of strings together based on string lengths"""
    set: dict[int, list[str]] = {}
    idx: int = 0
    string = strings[0]
    while idx < len(strings):
        if (len(strings[idx]) == len(string)) and (strings[idx] != string):
            set[len(strings[idx])] += strings[idx]
        string = strings[idx]
        idx += 1
    return set
