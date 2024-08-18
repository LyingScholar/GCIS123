import food_truck

def test_codes():
    assert 'soda' in food_truck.codes
    
    assert food_truck.codes['soda'] == 'Soda'

def test_prices():
    assert 'Soda' in food_truck.prices
    assert food_truck.prices['Soda'] == 1.95
    

    
def test_item_not_in_menu():
    assert 'Water' not in food_truck.prices
    
    
# def test_ordering_function():
#     food_truck.Combo('soda','burger','fries')
    