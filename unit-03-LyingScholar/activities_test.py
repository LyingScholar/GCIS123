import activities
import random
def test_squared_8():
    # setup
    value = 8
    expected = 64

    # execute
    actual = activities.squared(value)

    # analyse
    assert actual==expected

def test_squared_negative():
    # setup
    value = -10
    expected = 100

    # execute
    actual = activities.squared(value)

    # analyse
    assert actual==expected
    
def test_even_or_odd_even():
    # setup
    value = 10
    expected = "even"

    # execute
    actual = activities.even_or_odd(value)

    # analyse
    assert actual==expected
    
def test_coin_toss_heads():
    # setup
    random.seed(5)
    expected = "heads"

    # execute
    actual = activities.coin_toss()

    # analyse
    assert actual==expected