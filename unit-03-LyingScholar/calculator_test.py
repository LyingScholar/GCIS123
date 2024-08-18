import calculator
import math

def test_add_5_6():
    #setup
    expected = "5 + 6 = 11"
    #invoke
    actual = calculator.add(5,6)
    #analyse
    assert actual == expected
 
    
def test_add_8_2():
    #setup
    expected = "8 + 2 = 10"
    #invoke
    actual = calculator.add(8,2)
    #analyse
    assert actual == expected

    
def test_subtract_2_17():
    #setup
    expected = "2 - 17 = -15"
    #invoke
    actual = calculator.subtract(2,17)
    #analyse
    assert actual == expected
    
    
def test_subtract_17_2():
    #setup
    expected = "17 - 2 = 15"
    #invoke
    actual = calculator.subtract(17,2)
    #analyse
    assert actual == expected
 
    
def test_multiply_3_9():
    #setup
    expected = "3 * 9 = 27"
    #invoke
    actual = calculator.multiply(3,9)
    #analyse
    assert actual == expected


def test_multiply_negative7_8():
    #setup
    expected = "-7 * 8 = -56"
    #invoke
    actual = calculator.multiply(-7,8)
    #analyse
    assert actual == expected


def test_divide_16_8():
    #setup
    expected = "16 / 8 = 2.0"
    #invoke
    actual = calculator.divide(16,8)
    #analyse
    assert actual == expected


def test_divide_8_0():
    #setup
    expected = "8 / 0 = NaN"
    #invoke
    actual = calculator.divide(8,0)
    #analyse
    assert actual == expected
  
    
def test_exponent_8_0():
    #setup
    expected = "8^0 = 1"
    #invoke
    actual = calculator.exponent(8,0)
    #analyse
    assert actual == expected
  
    
def test_exponent_2_6():
    #setup
    expected = "2^6 = 64"
    #invoke
    actual = calculator.exponent(2,6)
    #analyse
    assert actual == expected