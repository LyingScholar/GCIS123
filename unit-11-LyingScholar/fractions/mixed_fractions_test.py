import mixed_fractions

TUPLES = [(3, 1, 2), (3, -1, 1), (2, 0, 1)]
FRACTIONS = [mixed_fractions.Fraction(w, n, d) for w, n, d in TUPLES]

def test_initialising_fractions():
    
    expected = (15,0,1)
    
    actual = mixed_fractions.Fraction(15).get_fraction()
    
    assert actual ==expected

def test_simplifying_fractions():
    
    expected = (5,1,2)
    
    actual = mixed_fractions.Fraction(0,11,2).simplify().get_fraction()
    
    assert actual ==expected

def test_simplifying_more_fractions():
    
    expected = (10,0,1)
    
    actual = mixed_fractions.Fraction(0,100,10).simplify().get_fraction()
    
    assert actual ==expected

def test_simplifying_negative_fractions():
    
    expected = (15,1,10)
    
    actual = mixed_fractions.Fraction(16,9,-10).simplify().get_fraction()
    
    assert actual ==expected


def test_unique_sorted_list():
    actual = mixed_fractions.unique_sorted_list(FRACTIONS)  
    assert [FRACTIONS[1], FRACTIONS[0]] == actual

def test_partition():
    actual = mixed_fractions.partition(FRACTIONS)
    
    assert 2 == len(actual)
    assert FRACTIONS[0] in actual
    assert FRACTIONS[1] in actual
    assert FRACTIONS[2] in actual
    assert [FRACTIONS[0]] == actual[FRACTIONS[0]]
    assert [FRACTIONS[1], FRACTIONS[2]] == actual[FRACTIONS[1]]


def test_find_all():
    a_partition = mixed_fractions.partition(FRACTIONS) 
    
    actual = mixed_fractions.find_all(a_partition, FRACTIONS[0])                                 
    assert [FRACTIONS[0]] == actual
    
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(2,3,2))
    
    assert [FRACTIONS[0]] == actual
    
    actual = mixed_fractions.find_all(a_partition, FRACTIONS[2])                                 
    assert [FRACTIONS[1], FRACTIONS[2]] == actual
    
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(3,-2,2))                                 
    assert [FRACTIONS[1], FRACTIONS[2]] == actual

def test_find_all_Empty():
    a_partition = mixed_fractions.partition(FRACTIONS)
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(1,2,3))                                 
    assert [] == actual
