import random
import random_password

def test_create_ascii_range_string_abcde():
    #setup
    expected = "abcde"
    #invoke
    actual = random_password.create_ascii_range_string(97,102)
    #analyze 
    assert expected == actual
    
    
def test_create_ascii_range_string_3():
    #setup
    expected = "3"
    #invoke
    actual = random_password.create_ascii_range_string(51,52)
    #analyze 
    assert expected == actual
    
    
def test_create_lowercase_letters_string():
    #setup
    expected = "abcdefghijklmnopqrstuvwxyz"
    #invoke
    actual = random_password.create_lowercase_letters_string()
    #analyze 
    assert expected == actual
    
        
def test_create_uppercase_letters_string():
    #setup
    expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #invoke
    actual = random_password.create_uppercase_letters_string()
    #analyze 
    assert expected == actual

        
def test_create_digits_string():
    #setup
    expected = "0123456789"
    #invoke
    actual = random_password.create_digits_string()
    #analyze 
    assert expected == actual
    
        
def test_create_symbols_string():
    #setup
    expected = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    #invoke
    actual = random_password.create_symbols_string()
    #analyze 
    assert expected == actual
    
def test_get_random_char_from_string_abcd():
    #setup
    random.seed(100)
    expected = "b"
    #invoke
    actual = random_password.get_random_char_from_string("abcd")
    #analye
    assert actual == expected
    
def test_get_random_char_from_string_babushka():
    #setup
    random.seed(30)
    expected = "s"
    #invoke
    actual = random_password.get_random_char_from_string("babushka")
    #analye
    assert actual == expected