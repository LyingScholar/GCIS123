import cards


# there are a LOT of comments, please ignore all

def deal_hand():
    deck = cards.make_deck()
    deck = cards.shuffle(deck)
    hand = cards.deal_one_hand(deck, 4)
    short_print(hand)
    return deck, hand

def discard(hand,num):
    if len(hand) >= 4:
        if num == 4:
            current_hand = hand[:-4]
        elif num == 2:
            # print('---'+str(hand[3])+'---')
            current_hand = hand[:-3]+hand[-1:]
            # print('---'+str(hand)+'---')
    return current_hand

def short_print(hand):
    for card in hand:
        print(card[3], end = " ")#---------------------------------------------------------
    print("\n")
        
def play_round(deck,current_hand):
    while len(current_hand)<4:
        cards.draw(deck,current_hand)

    # print("deck at start of round ",i,':')
    # short_print(current_hand)
    
    while len(current_hand)>=4 and len(deck)>0:
        end_card = current_hand[-1]
        second_last_card = current_hand[-2]
        third_last_card = current_hand[-3]
        fourth_last_card = current_hand[-4]
        # print('deck inside while loop:')
        # short_print(current_hand)
        
        if end_card[0] == fourth_last_card[0]:
            current_hand = discard(current_hand,4)
            # print('deck after discarding 4 cards:')#---------------------------------------------------------
            # short_print(current_hand)
            # break
        
        elif second_last_card[0]== third_last_card[0]:
            current_hand = discard(current_hand,2)
            # print('deck after discarding 2 cards:')#---------------------------------------------------------
            # short_print(current_hand)
            # break
        
        else:
            # print("pp")
            break
    
    if len(deck)>0:
        cards.draw(deck,current_hand)
        # print("deck at the end of round ",i,':')
        short_print(current_hand)
    return current_hand, deck

def main():
    deck, hand = deal_hand()
    # print(hand)
    shuffled_deck = cards.shuffle(deck)
    while len(deck) > 0:
    # for i in range(1000):
        hand, shuffled_deck = play_round(shuffled_deck,hand)
    if len(shuffled_deck) == 0 and len(hand)==0:
        print("congratulations, you won")
    elif len(shuffled_deck) == 0 and not len(hand)==0:
        print("you lost. Try again, peasant")
        
if __name__ == "__main__":
    main()