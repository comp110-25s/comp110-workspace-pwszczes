"""Test functions for the dictionary.py file"""

__author__ = "730643202"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert1() -> None:
    """Tests a first use case for the invert() function"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert2() -> None:
    """Tests a second use case for the invert() function"""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert3() -> None:
    """Tests an edge case for the invert() function"""
    assert invert({}) == {}


def test_count1() -> None:
    """Tests a first use case for the count() function"""
    assert count(["berry", "banana", "berry"]) == {"berry": 2, "banana": 1}


def test_count2() -> None:
    """Tests a second use case for the count() function"""
    assert count(["fruit", "grapes", "grapes", "fruit"]) == {"fruit": 2, "grapes": 2}


def test_count3() -> None:
    """Tests an edge case for the count() function"""
    assert count(["berry", "berry", "berry"]) == {"berry": 3}


def test_favorite_color1() -> None:
    """Tests a first use case for the favorite_color() function"""
    assert (
        favorite_color(
            {"Preston": "Yellow", "Izzi": "Green", "Mason": "Yellow", "James": "White"}
        )
        == "Yellow"
    )


def test_favorite_color2() -> None:
    """Tests a second use case for the favorite_color() function"""
    assert (
        favorite_color(
            {"Preston": "Violet", "Izzi": "Green", "Mason": "Green", "James": "Green"}
        )
        == "Green"
    )


def test_favorite_color3() -> None:
    """Tests an edge case for the favorite_color() function"""
    assert (
        favorite_color(
            {"Preston": "Violet", "Izzi": "Green", "Mason": "Green", "James": "Violet"}
        )
        == "Violet"
    )


def test_bin_len1() -> None:
    """Tests a first use case for the bin_len() function"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    """Tests a second use case for the bin_len() function"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len3() -> None:
    """Tests an edge case for the bin_len() function"""
    assert bin_len([]) == {}
