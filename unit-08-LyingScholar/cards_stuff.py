

# IMPORTANT IMPORTANT IMPORTANT IMPORTANT
#this is NOT the assignment file, this is just a practise module, the assignemnt is cards.py




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

def shuffle(deck):
    # random.seed(2)
    for i in range(len(deck)):    
        j = random.randint(i,len(deck)-1)
        a = deck[i]
        deck[i] = deck[j]
        deck[j] = a
    return deck



def deal_one_hand(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        card = deck.pop(0)
        hand.append(card)
    return hand

def draw(deck, hand):
    card = deck.pop(0)
    hand.append(card)