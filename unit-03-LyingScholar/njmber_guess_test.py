import njmber_guess
import random

def test_secret_number_10():
    random.seed(100)
    expected = 10
    
    actual = njmber_guess.number()
    
    assert actual == expected