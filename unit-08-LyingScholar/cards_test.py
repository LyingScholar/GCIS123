import cards
import random

def test_make_cards_valid_input():
    #setup
    expected = (2, 'Spades', 'Two of Spades', '\033[34m 2S\033[37m')
    
    # invoke
    actual = cards.make_cards(2, 'spades')

    #analyze
    assert expected == actual

def test_make_cards_invalid_input():
    #setup
    expected = 'invalid input'
    # invoke
    actual = cards.make_cards(20, 'diamonds')
    #analyze
    assert expected == actual

def test_make_cards_7_diamonds():
    expected = (7, 'Diamonds', 'Seven of Diamonds', '\033[31m 7D\033[37m')
    actual = cards.make_cards(7, 'diamonds')
    assert actual == expected

def test_make_cards_10_clubs():
    expected = (10, 'Clubs', 'Ten of Clubs', '\033[34m10C\033[37m')
    actual = cards.make_cards(10, 'clubs')
    assert actual == expected


def test_make_cards_face_cards():
    expected = (11, 'Spades', 'Jack of Spades', '\033[34m11S\033[37m')
    actual = cards.make_cards(11, 'spades')
    assert actual == expected
    

    expected = (12, 'Diamonds', 'Queen of Diamonds', '\033[31m12D\033[37m')
    actual = cards.make_cards(12, 'diamonds')
    assert actual == expected

    expected = (13, 'Clubs', 'King of Clubs', '\033[34m13C\033[37m')
    actual = cards.make_cards(13, 'clubs')
    assert actual == expected

    expected = (14, 'Hearts', 'Ace of Hearts', '\033[31m14H\033[37m')
    actual = cards.make_cards(14, 'hearts')
    assert actual == expected
    

def test_len_make_deck():
    #setup
    expected = 52
    
    # invoke
    actual = len(cards.make_deck())
    #analyze
    assert expected == actual

def test_random_card_make_deck():
    #setup
    deck = cards.make_deck()
    random.seed(42)

    expected_card = (7, 'Clubs', 'Seven of Clubs', '\033[34m 7C\033[37m')
    
    assert deck[21] == expected_card

def test_shuffle_len():
    #setup
    expected = 52
    deck = cards.make_deck()
    shuffled_deck = cards.shuffle(deck)
    # invoke
    actual = len(shuffled_deck)
    
    #analyze
    assert expected == actual


def test_shuffle():
    #setup
    deck = cards.make_deck()
    expected_length = 52
    not_expected_deck = deck[:]
    # invoke
    
    actual_length = len(deck)
    actual_deck = cards.shuffle(deck)
    
    #analyze
    assert actual_length == expected_length
    assert not actual_deck == not_expected_deck

def test_draw():
    deck = cards.make_deck()
    hand = []
    card = cards.draw(deck, hand)
    
    #analyze
    # assert card in deck
    assert card in hand

def test_draw_more():
    #setup
    expected_deck_len = 50
        
    # invoke
    deck = cards.make_deck()
    hand = []
    card = cards.draw(deck, hand)
    card = cards.draw(deck, hand)
    actual_deck_len= len(deck)
    
    #analyse
    assert actual_deck_len == expected_deck_len

def test_deal_one_hand():
    #setup
    deck = cards.make_deck()
    hands_num = 4
    
    #invoke
    hand = cards.deal_one_hand(deck, hands_num)
    
    #analyze
    assert len(deck) == 48
    assert len(hand) == hands_num