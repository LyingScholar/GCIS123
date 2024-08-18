import candy_land_card



def create_board():
    board = [#'R', 'B', 'O', 'G', 'Y', 'P', 'M', 'JJ', 'Y', 'B', 'R', 'G', '^', 'O', 'L', 'P', 'M', 'Y', 'B', '^', 'R', 'G', 'O', 'Y', 'P', 'v']
        'Start', 'R', 'P', 'Y', 'BS60', 'O', 'G', 'R', 'P', 'CC', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'IC', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'BS41', 'O','G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'JJ', 'B', 'O', 'GL', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'GP', 'G', 'R', 'P', 'Y', 'B', 'O', 'GL', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'LP', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'PS', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'BB', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'MC']
    board[4] = "^"
    board[60]= "v"
    board[29] = "^^"
    board[41]= "vv"
    
    
    return board
    
def move_player(player, move,board):
    colors = ['R', 'O', 'Y', 'G', 'B', 'P', 'M']
    current_location = player[1]
    
    if move[1] in colors:
        try:
            color_index = colors.index(move[1])
            next_location = board.index(colors[color_index], current_location + 1)
        except ValueError:
            next_location = 150
    elif move == 'YY':
        next_location = board.index('Y', current_location + 2)
    elif move == 'JJ':
        jello_index = board.index('JJ')
        if jello_index < current_location:
            next_location = jello_index
        else:
            next_location = current_location
    else:
        next_location = current_location

    return next_location

def take_turn(player, board, deck):
    color = player[0]
    deck_size = len(deck)
    
    if deck_size <= 0:
        deck = candy_land_card.make_deck()
    
    drawn_card = candy_land_card.draw(deck)
    move = drawn_card[2]
    next_location = move_player(player, move,board)
    
    if next_location >= len(board):
        #win
        print(f"Player {color} drew a {drawn_card}. Player wins!")
        return next_location
    elif board[next_location] == '^' or board[next_location] == 'v' or board[next_location] == '^^' or board[next_location] == 'vv':
        #shortkut
        if board[next_location] == '^':
            next_location = board.index('v')
        elif board[next_location] == '^^':
            next_location = board.index('vv')
        elif board[next_location] == 'vv':
            next_location = board.index('^^')
        else:
            next_location = board.index('^')
            
        print(f"Player {color} drew a {drawn_card}. Player took a shortcut!")
    elif board[next_location] == 'L':
        #licorice
        print(f"Player {color} drew a {drawn_card}. Player loses a turn.")
        return player[1]
    else:
        print(f"Player {color} drew a {drawn_card}. Player moves to {board[next_location]}.")
    

    return next_location

def main():
    num_players = int(input("Enter the number of players: "))
    colors = ["Red", "Blue", "Yellow", "Green", "Orange", "Purple", "Pink", "Brown", "Black", "White", "Gray", "Magenta", "Cyan", "Teal", "Turquoise", "Indigo", "Gold", "Silver", "Beige", "Burgundy"]
    players = [(colors[i],0) for i in range(num_players)]
    deck = candy_land_card.make_deck()
    # while True:
    for i in range(100):
        for player in players:
            board = create_board()
            location = take_turn(player, board, deck)
            player_index = players.index(player)
            players[player_index] = (player[0], location)
            print(location)
            if location >= len(board):
                winner = player[0]
                print(f"{winner} has won the game!")
                return

# def main():
#     num_players = int(input("Enter the number of players: "))

#     players = [('Red', 0), ('Green', 0), ('Blue', 0), ('Yellow', 0)]
    
#     deck = candy_land_card.make_deck()
    
#     board = create_board()
#     for i in range(100):
#         for player in players:
#             location = take_turn(player, board, deck)
#             if location >= len(board):
#                 winner = player[0]
#                 print(f"{winner} has won the game!")
#                 break
#             player_index = players.index(player)
#             players[player_index] = (player[0], location)

main()