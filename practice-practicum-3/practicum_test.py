"""
Python unit test provided to students to test their practicum implementation.

Rather than trying to run all of the tests at once, uncomment them one at a 
time to verify that your code is working as expected. 

Remember, you can select a block of code and type CTRL+/ (or Command+/) to 
comment/uncomment it.
"""
import math
from practicum import * #this imports all functions directly here so you don't need to call practicum. before the function.

# EUCLIDEAN DISTANCE
def test_euclidean_distance_none():
    # setup
    point1 = (1, 2)
    point2 = (3, 4, 5)
    expected = None

    # invoke
    actual = euclidean_distance(point1, point2)

    # analyze
    assert expected == actual

def test_euclidian_distance_1D():
    # setup
    point1 = [1]
    point2 = [5]
    expected = 4

    # invoke
    actual = euclidean_distance(point1, point2)

    # analyze
    assert expected == actual

def test_euclidian_distance_2D():
    # setup
    point1 = (1, 2)
    point2 = (4, 6)
    expected = 5

    # invoke
    actual = euclidean_distance(point1, point2)

    # analyze
    assert expected == actual

def test_euclidian_distance_5D():
    # setup
    point1 = range(1, 6)
    point2 = range(5, 14, 2)
    expected = 13.784048752090222

    # invoke
    actual = euclidean_distance(point1, point2)

    # analyze
    assert math.isclose(expected, actual)




# DATA SORTER
def test_data_sorter_empty():
    # setup
    expected = []
    data = []
    old_data = data[:]

    # invoke
    actual = data_sorter(data)

    # analyze
    assert data == old_data
    for i in actual:
        assert i == expected

def test_data_sorter_standard():
    # setup
    data = [10,100,15,11,4,5,2]
    old_data = data[:]

    expected_alphabetical = [5,4,10,100,15,11,2]
    expected_digits = [100,10,11,15,2,4,5]

    # invoke
    actual = data_sorter(data)

    # analyze
    assert data == old_data
    assert actual[0] == expected_alphabetical
    assert actual[1] == expected_digits
    # BONUS
    # expected_frequency = [10,100,15,11,4,5,2]
    # assert actual[2] == expected_frequency

def test_data_sorter_duplicates():
    # setup
    data = [1,3,5,2,1,3,1]
    old_data = data[:]

    expected_alphabetical = [5,1,1,1,3,3,2]
    expected_digits = [1,1,1,2,3,3,5]

    # invoke
    actual = data_sorter(data)

    # analyze
    assert data == old_data
    assert actual[0] == expected_alphabetical
    assert actual[1] == expected_digits
    # BONUS
    # expected_frequency = [1,1,1,3,3,5,2]
    # assert actual[2] == expected_frequency

def test_data_sorter_duplicates_multi_digit():
    # setup
    data = [10,3000,5,20,10,3,100,3000,3120,100]
    old_data = data[:]

    expected_alphabetical = [5,10,10,100,100,3000,3,3000,3120,20]
    expected_digits = [3000,3000,3120,100,100,10,10,20,3,5]

    # invoke
    actual = data_sorter(data)

    # analyze
    assert data == old_data
    assert actual[0] == expected_alphabetical
    assert actual[1] == expected_digits
    # BONUS
    expected_frequency = [10,10,3000,3000,100,100,5,20,3,3120]
    assert actual[2] == expected_frequency
    

# PHONETIC TRANSLATION
def test_phonetic_translation_empty():
    # setup
    a_string = ""
    expected = []

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_one_letter():
    # setup
    a_string = "q"
    expected = ["Quebec"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_one_word():
    # setup
    a_string = "LOVE"
    expected = ["Lima", "Oscar", "Victor", "Echo"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_two_words():
    # setup
    a_string = "tOp GuN"
    expected = ["Tango", "Oscar", "Papa", "Golf", "Uniform", "November"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_punctuation():
    # setup
    a_string = "a.b!c-a@"
    expected = ["Alpha", "Bravo", "Charlie", "Alpha"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual


# WORDS BY LETTER
def assert_words_by_letter(first_letters, unique_words, result):
    """
    A helper-function used to verify that the result data structure contains
    the correct values. This function is needed by the words_by_letters tests.
    """
    assert len(first_letters) == len(result)
    for index in range(len(first_letters)):
        first_letter = first_letters[index]
        words = unique_words[index]
        result_words = result[first_letter]
        assert len(words) == len(result_words)
        for word in words:
            assert word in result_words

def test_words_by_letter_empty():
    # setup
    a_string = ""

    # invoke
    data = words_by_letter(a_string)

    # analyze
    assert 0 == len(data)

def test_words_by_letter_one():
    # setup
    a_string = "ant"
    first_letters = "a"
    unique_words = [["ant"]]

    # invoke
    result = words_by_letter(a_string)

    # analyze
    assert_words_by_letter(first_letters, unique_words, result)

def test_words_by_letter_same():
    # setup
    a_string = "ant an aunt ant ant aunt"
    first_letters = "a"
    unique_words = [["ant", "an", "aunt"]]

    # invoke
    result = words_by_letter(a_string)

    # analyze
    assert_words_by_letter(first_letters, unique_words, result)

def test_words_by_letter_example():
    # setup
    a_string = "The cat in the hat is back with a bright blue bat out in " \
        "the back"
    first_letters = "acbhiotw"
    unique_words = [["a"], ["cat"], ["back", "bright", "blue", "bat"], ["hat"],
        ["in", "is"], ["out"], ["the"], ["with"]]

    # invoke
    result = words_by_letter(a_string)

    # analyze
    assert_words_by_letter(first_letters, unique_words, result)
