    # skip_card_1 = (60, 'X', 'S60')
    # skip_card_2 = (41, 'X', 'S41')
    # licorice_card_1 = (45, 'X', 'L45')
    # licorice_card_2 = (76, 'X', 'L76')
    #     deck.extend([skip_card_1, skip_card_2,licorice_card_1, licorice_card_2])

import candy_land_card

def test_draw_deck_a():
    #setup
    expected = (134, 'X', 'MC')
    #invoke
    actual = candy_land_card.draw(candy_land_card.make_deck())
    #analyse
    assert actual==expected