import practise

def test_absolute_difference_1_3():
    #setup
    expected = 2
    #invoke
    actual = practise.absolute_difference(1,3)
    #analyse
    assert actual == expected

def test_absolute_difference_1_n3():
    #setup
    expected = 4
    #invoke
    actual = practise.absolute_difference(1,-3)
    #analyse
    assert actual == expected
 
def test_absolute_difference_n1_n3():
    #setup
    expected = 2
    #invoke
    actual = practise.absolute_difference(-1,-3)
    #analyse
    assert actual == expected
  