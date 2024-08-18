import pytest
import practise13



def test_get_divisible_numbers_100():
    # setup
    expected= [100, 99, 96, 95, 93, 87, 85, 84, 81, 80, 78, 72, 70, 69, 66, 65, 63, 57, 55, 54, 51, 50, 48, 42, 40, 39, 36, 35, 33, 27, 25, 24, 21, 20, 18, 12, 10, 9, 6, 5, 3]
    
    # invoke
    actual = practise13.get_divisible_numbers(100)
        
    # Analyse
    
    assert expected == actual
    
def test_get_divisible_numbers_10():
# setup
    expected = [10, 9, 6, 5, 3]
    # invoke
    actual = practise13.get_divisible_numbers(10)
        
    # Analyse
    
    assert expected == actual
    
    
def test_get_divisible_numbers_2():
    # setup
    expected = []
    # invoke
    actual = practise13.get_divisible_numbers(2)
    # Analyse
    assert expected == actual


def test_is_word_present():
    words_array = ["apple", "banana", "orange", "grape"]
    
    word = "Apple"
    assert practise13.is_word_present(word, words_array) == True
    
    word = "mango"
    assert practise13.is_word_present(word, words_array) == False
    word = "GRAPE"
    assert practise13.is_word_present(word, words_array) == True



def test_find_words_1():
    #setup
    filename = "test_file.txt"
    letter = 'a'
    number = 2
    
    # invoke
    actual = practise13.find_words(filename, letter, number)
    expected = ["apple", "antelope"]
    
    #analyse
    assert expected == actual
    

def test_find_words_Nones():
    #setup
    filename = "test_file.txt"    

    letter = 'g'
    number = 3
    expected = ["grape", None, None]
    
    # invoke
    actual = practise13.find_words(filename, letter, number) 
    #analyse
    assert expected == actual
    

def test_find_words_empty():
    #setup
    filename = "test_file.txt"   
    letter = 'x'
    number = 3
    expected = [None, None, None]    
    
    # invoke
    actual = practise13.find_words(filename, letter, number) 
    
    #analyse
    assert expected == actual

def test_generate_calendar_0_30():
    # Setup
    weekday = 0
    num_days = 30
    expected = [['01', '02', '03', '04', '05', '06', '07'],
                ['08', '09', '10', '11', '12', '13', '14'],
                ['15', '16', '17', '18', '19', '20', '21'],
                ['22', '23', '24', '25', '26', '27', '28'], 
                ['29', '30', '  ', '  ', '  ', '  ', '  ']]
    # Invoke
    actual = practise13.generate_calendar(weekday,num_days)
    
    # Analyse
    
    assert expected == actual
    

def test_generate_calendar_2_28():
    # Setup
    weekday = 2
    num_days = 28
    expected = [['  ', '  ', '01', '02', '03', '04', '05'],
                ['06', '07', '08', '09', '10', '11', '12'],
                ['13', '14', '15', '16', '17', '18', '19'], 
                ['20', '21', '22', '23', '24', '25', '26'],
                ['27', '28', '  ', '  ', '  ', '  ', '  ']
                ]

    # Invoke
    actual = practise13.generate_calendar(weekday,num_days)
    
    # Analyse
    
    assert expected == actual
    
def test_generate_calendar_saturday_29():
    # Setup
    weekday = 6
    num_days = 29
    expected = [
        ['  ', '  ', '  ', '  ', '  ', '  ', '01'],
        ['02', '03', '04', '05', '06', '07', '08'],
        ['09', '10', '11', '12', '13', '14', '15'],
        ['16', '17', '18', '19', '20', '21', '22'],
        ['23', '24', '25', '26', '27', '28', '29'],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ']
]
    # Invoke
    actual = practise13.generate_calendar(weekday,num_days)
    
    # Analyse
    
    assert expected == actual