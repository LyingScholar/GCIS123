import random

def make_cards(rank,suit):
    if suit.strip().lower() in ('diamonds', 'spades','hearts','clubs') and int(rank) < 15 and int(rank) > 1:            
        names = ["DNE","DNE",'two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
        if rank < 10:
            rank = " "+ str(rank) 
        else:
            rank = str(rank)
        suit = suit.strip().lower()
        if suit in ("diamonds","hearts"):
            short_hand = "\033[31m"+ str(rank) + suit[0].upper()+"\033[37m"
        else:
            short_hand = "\033[34m"+ str(rank) + suit[0].upper()+"\033[37m"
        rank_name = str((names[int(rank)][0])).upper() + names[int(rank)][1:]
        suit = suit[0].upper()+suit[1:]
        # i just capitalized it here, I was too lazy to rewrite the list
        return (int(rank),suit,rank_name +" of " + str(suit) ,short_hand)
    else:
        return('invalid input')

def make_deck():
    deck=[]
    for i in range(2,15):
        deck.append(make_cards(i,'diamonds'))
        deck.append(make_cards(i,'clubs'))
        deck.append(make_cards(i,'hearts'))
        deck.append(make_cards(i,'spades'))
    return deck
# print(make_cards(2,'spades'))

def shuffle(deck):
    # random.seed(2)
    for i in range(len(deck)):    
        j = random.randint(i,len(deck)-1)
        a = deck[i]
        deck[i] = deck[j]
        deck[j] = a
    return deck

def draw(deck,hand):
    card = deck.pop()
    hand.append(card)
    return card

def deal_one_hand(deck, hands_num):
    hand=[]
    for i in range(hands_num):
        draw(deck,hand)
    return hand


# p = shuffle(make_deck())
# print(deal_one_hand(p, 4))
# for card in p:
#     print(card[0],end =" ")