import guessing_game
import random

def test_secret_number_18():
    # setup
    random.seed(1)
    expected = 18

    # invoke
    actual = guessing_game.secret_number()

    # analyze
    assert expected == actual

def test_secret_number_80():
    # setup
    random.seed(5)
    expected = 80

    # invoke
    actual = guessing_game.secret_number()

    # analyze
    assert expected == actual

def test_check_guess_low():
    # setup
    secret = 50
    guess = 25
    expected = "Too Low"

    # invoke
    actual = guessing_game.check_response(secret, guess)

    # analyze
    assert expected == actual

def test_check_guess_high():
    # setup
    secret = 27
    guess = 73
    expected = "Too High"

    # invoke
    actual = guessing_game.check_response(secret, guess)

    # analyze
    assert expected == actual

def test_check_guess_correct():
    # setup
    secret = 12
    guess = 12
    expected = "Correct"

    # invoke
    actual = guessing_game.check_response(secret, guess)

    # analyze
    assert expected == actual