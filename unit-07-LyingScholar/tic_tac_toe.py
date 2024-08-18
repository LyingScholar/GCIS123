
def make_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    for row in range(len(board)):
        print(board[row][0]+ " | "+board[row][1]+ " | "+board[row][2])
        if row< len(board)-1:
            print("---------")

def make_move(board,symbol):
    user_input = input("Enter row and column (" + symbol +") : ")
    
    token = user_input.split()
    row = int(token[0])
    column = int(token[1])
    
    board[row][column]= symbol
    
    print_board(board)

def main():
    board = make_board()
    print_board(board)
    
    symbol = "X"
    for i in range(10):
        if symbol=="X":
            symbol = "O"
        else:
            symbol = "X"
        make_move(board,symbol)

if __name__ == "__main__":
    main()