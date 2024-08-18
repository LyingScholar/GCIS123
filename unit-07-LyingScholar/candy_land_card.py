import random

def make_deck():
    deck = []
        
    special_cards = [
        (9, 'X', 'CC'),  #  Cupcake
        (20, 'X', 'IC'),  # IceCream
        (42, 'X', 'JJ'),  # JellOjiggler
        (69, 'X', 'GB'),  # Gingerbread
        (92, 'X', 'LP'),  # Lollipop
        (102, 'X', 'PC'),  # Popsicle
        (117, 'X', 'BB')  # BonBon
    ]

    colors = ['Red', 'Purple', 'Yellow', 'Blue', 'Orange', 'Green']
    for color in colors:
        single_move_card = (1, color[0], 'S' + color[0])
        
        for i in range(6):
            deck.append(single_move_card)
        
        double_move_card = (2, color[0], 'D' + color[0])
        for i in range(4):
            deck.append(double_move_card)
    
    deck.extend(special_cards)
    
    return deck

def shuffle(deck):
    for i in range(len(deck) - 1):
        j = random.randint(i, len(deck) - 1)
        eef = deck[i]
        deck[i] = deck[j]
        deck[j]=eef
    return deck

def draw(deck):
    if len(deck) == 0:
        return None
    shuffle(deck)
    banana= deck.pop(0)
    return banana

# print(make_deck())
# print(type(make_deck()))