from mixed_fractions import *

def test_subtract():
    a_fraction = Fraction(0,4,3)  
    b_fraction = Fraction(1,0,1)
    actual_subtract = a_fraction.subtract(b_fraction)
    expected_subtract = Fraction(0,1,3)
    print(actual_subtract)
    print(expected_subtract)
    assert expected_subtract == actual_subtract

def test_sum():
    a_fraction = Fraction(1,3,10)   # 1.3
    b_fraction = Fraction(4,6,10)   # 4.6
    expected_sum = Fraction(5,9,10) # 5.9
    actual_sum = a_fraction.add(b_fraction)
    assert expected_sum.get_fraction() == actual_sum

def test_eq_1():
    a_fraction = Fraction(-2,27,13)
    b_fraction = Fraction(0,7,91)
    assert a_fraction == b_fraction 

def test_eq_2():
    x = Fraction(199933,0,1)
    y = Fraction(11111111111111111,0,1)
    b_fraction = y
    a_fraction = x.divide(x)
    print(a_fraction)
    
    assert y.multiply(a_fraction) == b_fraction
    
def test_neq():
    a_fraction = Fraction(0,100000000000000000,3)
    b_fraction = Fraction(0,100000000000000001,3)
    assert a_fraction != b_fraction
    
def test_lt():
    a_fraction = Fraction(0,100000000000000000,3)
    b_fraction = Fraction(0,100000000000000001,3)
    assert a_fraction < b_fraction 

def test_gt():
    a_fraction = Fraction(0,100000000000000000,3)
    b_fraction = Fraction(0,100000000000000001,3)
    assert b_fraction > a_fraction