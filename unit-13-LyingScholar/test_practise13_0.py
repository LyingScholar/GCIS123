import pytest
from practise13_0 import pig_latin_translator

def test_word_starts_with_consonant():
    # Setup
    word = "bagel"
    expected = "agelbay"

    # Invoke
    actual = pig_latin_translator(word)

    # Analyse
    assert actual == expected

def test_word_starts_with_vowel():
    # Setup
    word = "apple"
    expected = "appleay"

    # Invoke
    actual = pig_latin_translator(word)

    # Analyse
    assert actual == expected

def test_word_starts_with_consonant_cluster():
    # Setup
    word = "smile"
    expected = "ilesmay"

    # Invoke
    actual = pig_latin_translator(word)

    # Analyse
    assert actual == expected

def test_word_contains_capital_letters():
    # Setup
    word = "Bagel"
    expected = "agelBay"

    # Invoke
    actual = pig_latin_translator(word)

    # Analyse
    assert actual == expected

def test_word_contains_punctuation():
    # Setup
    word = "shy,"
    expected = "shy,ay"

    # Invoke
    actual = pig_latin_translator(word)

    # Analyse
    assert actual == expected