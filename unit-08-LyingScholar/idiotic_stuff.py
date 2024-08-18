
# IMPORTANT IMPORTANT IMPORTANT IMPORTANT
#this is NOT the assignment file, this is just a practise module, the assignemnt is idiots_deight.py


import cards_stuff
import cards

def deal_hand():
    deck = cards_stuff.make_deck()
    deck = cards_stuff.shuffle(deck)
    hand = cards_stuff.deal_one_hand(deck, 4)
    return deck, hand

def short_print(hand):
    for card in hand:
        print(card[3], end = " ")#---------------------------------------------------------
    print("\n")

def discard(hand,num):
    if len(hand) >= 4:
        if num == 4:
            current_hand = hand[:-4]
        elif num == 2:
            current_hand = hand[:-3]+hand[-1:]
    return current_hand

def play_round(deck,current_hand):
    while len(current_hand)<4:
        cards.draw(deck,current_hand)
        short_print(current_hand)

    while len(current_hand)>=4:
        end_card = current_hand[-1]
        second_last_card = current_hand[-2]
        third_last_card = current_hand[-3]
        fourth_last_card = current_hand[-4]
        short_print(current_hand)
        print('issue here?')
        short_print(current_hand)
        
        if end_card[0] == fourth_last_card[0]:
            current_hand = discard(current_hand,4)
            print(4)#---------------------------------------------------------
            short_print(current_hand)
            # break
        
        elif second_last_card[0]== third_last_card[0]:
            current_hand = discard(current_hand,2)
            print(2)#---------------------------------------------------------
            short_print(current_hand)
            # break
        
        else:
            break
    
    if len(deck)>0:
        cards.draw(deck,current_hand)
        print("\nadding 1")#---------------------------------------------------------
        short_print(current_hand)


def main():
    deck, hand = deal_hand()
    while len(deck) > 0:
        play_round(deck, hand)
        short_print(hand)
    if len(deck) == 0 and len(hand) == 0:
        print("Congratulations! You won.")
    else:
        print("Game over. Try again.")

if __name__ == "__main__":
    main()