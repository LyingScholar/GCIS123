import searches
import array_utils

def test_linear_search_inside():
    #setup  
    number = 40
    expected = number-1
    
    #invoke
    actual = searches.linear_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_linear_search_outside():
    #setup  
    number = 120
    expected = None
    
    #invoke
    actual = searches.linear_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_linear_search_start():
    #setup  
    number = 1
    expected = 0
    
    #invoke
    actual = searches.linear_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_linear_search_end_in():
    #setup  
    number = 99
    expected = 98
    
    #invoke
    actual = searches.linear_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_linear_search_end_out():
    #setup  
    number = 100
    expected = None
    
    #invoke
    actual = searches.linear_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_linear_search_specific_1():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 12
    expected = 4
    
    #invoke
    actual = searches.linear_search(array1,number)
    
    #analyse
    assert actual==expected

def test_linear_search_specific_2():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 45
    expected = None
    
    #invoke
    actual = searches.linear_search(array1,number)
    
    #analyse
    assert actual==expected

def test_linear_search_specific_3():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 6
    start = 1
    end = 4
    expected = 2
    
    #invoke
    actual = searches.linear_search(array1,number,start,end)
    
    #analyse
    assert actual==expected

def test_linear_search_specific_4():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 25
    start = 3
    end = 7
    expected = None
    
    #invoke
    actual = searches.linear_search(array1,number,start,end)
    
    #analyse
    assert actual==expected

def test_jump_search_specific_1():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 12
    expected = 4
    
    #invoke
    actual = searches.jump_search(array1,number)
    
    #analyse
    assert actual==expected

def test_jump_search_specific_2():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 45
    expected = None
    
    #invoke
    actual = searches.jump_search(array1,number)
    
    #analyse
    assert actual==expected

def test_binary_search_inside():
    #setup  
    number = 40
    expected = number-1
    
    #invoke
    actual = searches.binary_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_binary_search_outside():
    #setup  
    number = 120
    expected = None
    
    #invoke
    actual = searches.binary_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_binary_search_start():
    #setup  
    number = 1
    expected = 0
    
    #invoke
    actual = searches.binary_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_binary_search_end_in():
    #setup  
    number = 99
    expected = 98
    
    #invoke
    actual = searches.binary_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_binary_search_end_out():
    #setup  
    number = 100
    expected = None
    
    #invoke
    actual = searches.binary_search(array_utils.range_array(1,100,1),number)
    
    #analyse
    assert actual==expected

def test_binary_search_specific_1():
    #setup
    array1 = [3,5,6,8,12,17,22,25,31]
    number = 12
    expected = 4
    
    #invoke
    actual = searches.binary_search(array1,number)
    
    #analyse
    assert actual==expected