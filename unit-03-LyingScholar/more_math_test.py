import more_math
import math

def test_fact_5():
    # setup
    expected = 120

    # invoke
    actual = more_math.fact(5)

    # analyze
    assert expected == actual

def test_root_81():
    # setup
    expected = 9

    # invoke
    actual = more_math.root(81)

    # analyze
    assert expected == actual

def test_root_80():
    # setup
    expected = 8.944271909999

    # invoke
    actual = more_math.root(80)

    # analyze
    assert True == math.isclose(actual,expected)


def test_trunk_4_2():
    # setup
    expected = 4

    # invoke
    actual = more_math.trunk(4.2)

    # analyze
    assert expected == actual