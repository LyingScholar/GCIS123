
NAME_TO_TABLE = {'t': [[1,1,1],[0,1,0]], 
                 'T': [[1,1,1],[0,1,0],[0,1,0]], 
                 'z': [[1,1,0],[0,1,1]],
                 'c': [[1,1],[1,0],[1,1]],
                 'f': [[1,1],[1,0],[1,1], [1,0]],
                 'L': [[1,0,0],[1,1,1]],
                 'l':[[1,0], [1,1]]}
EMPTY_SPOT = '-'
BLOCKER_SPOT = 'o'

def remove_duplicates(input_list):
    return list(set(input_list))

def transpose(M):
    return [[ M[col][row] for col in range(len(M))] for row in range(len(M[0]))]

def flip_rows(M):
    return M[::-1]

def flip_cols(M):
    return [M[row][::-1] for row in range(len(M)) ]

def help_message():
    print("- 'help' to display commands")
    print("- 'quit' to quit the game" )
    print("- 'a <piece name> <row> <col>' to add a piece to the board at the position ") 
    print("- 'r <piece name>' to remove a piece")
    
class Shape:
    __slots__ = ['__table', '__position']
    
    def __init__(self, table):
        self.__table = table
        self.__position = None        
    
    def get_table(self):
        return self.__table      
    def get_position(self):
        return self.__position
    
    def __str__(self):
        return str(self.__table) + " " + str(self.__position)
    
    def __repr__(self):
        return repr(self.__table) + " " + repr(self.__position)
    
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__table == other.__table
        return False
    
    def __hash__(self):
        return hash(str(self.__table))
    
    
    
    
    def fit(self, board, position):
        num_of_rows = len(self.__table)
        num_of_cols = len(self.__table[0])
        
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if self.__table[row][col] == 1: #this part makes sure i'm checking the shape, not thw whole rectangle
                    print(position)
                    
                    if int(position[0]) + row >= len(board) or int(position[1]) + col >= len(board[0]) or board[int(position[0]) + row][int(position[1]) + col] != '-':
                        # i go through the whole shape, making sure no part of it is forced outside the board
                        # then the last part is to check if the whole shape is only "-" on the board at given position``
                        return False
        return True
    
    def add(self, board, position, symbol):
        num_of_rows = len(self.__table)
        num_of_cols = len(self.__table[0])
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if self.__table[row][col] == 1:
                    board[position[0] + row][position[1] + col] = symbol
        self.__position = position
    
    def remove(self, board):
        num_of_rows = len(self.__table)
        num_of_cols = len(self.__table[0])
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if self.__table[row][col] == 1:
                    board[self.__position[0] + row][self.__position[1] + col] = '-'
        self.__position = None



class Puzzle:
    __slots__ = ['__board', '__pieces', '__pieces_on_board', '__game_over']
    
    def __init__(self, blockers):
        self.__board = [[EMPTY_SPOT for _ in range(6)] for _ in range(6)]
        for r, c in blockers:
            self.__board[r][c] = BLOCKER_SPOT
        self.__pieces = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.__pieces_on_board = []
        self.__game_over = False


    def add_piece(self, piece, position):
        piece.set_fit_shapes(self.__board, position)
        print(type(piece.get_fit_shape))
        piece.add(self.__board, piece.get_fit_shape, position)
        print(self)
        while True:
            alpha =input("like this? (y/n)")
            if alpha.strip().lower() == 'y':
                print(self)
                break
            elif alpha.strip().lower() == 'n':
                piece.remove(self.__board)
                piece.add(self.__board, piece.get_fit_shape, position)
                print(self)
                continue
            else:
                continue
                
        if piece.get_fit_shape(self.__board, position):
            piece.add(self.__board, position)
            return True
        return False

    def play(self):
        print(self)
        while not self.__game_over:
            response = input("Enter a command or 'help': ")
            if response == "quit":
                print("Bye!")
                break
            elif response == "help":
                help_message()
            else:
                responses = response.strip().split()
                if responses[0].lower() == "a":
                    piecee = Piece(responses[1])
                    self.add_piece(piecee,[responses[2],responses[3]])
                    continue
    
    def __str__(self):
        s = '    0 1 2 3 4 5\n'
        s +='   ------------\n'
        for index in range(len(self.__board)):
            s += str(index) + " | "
            for elt in self.__board[index]:
                s += elt + " "
            s += "\n"
        return s

class Piece:
    __slots__ = ['__distinct_name_of_piece','__shapes', '__current_shape', '__fit_shapes', '__round_robbin_index']
        
    def __init__(self, distinct_name_of_piece):
        self.__distinct_name_of_piece = distinct_name_of_piece
        self.__current_shape = None
        self.__round_robbin_index = 0

        #adding the list of shapes
        self.__shapes= []
        base_shape = NAME_TO_TABLE[str(distinct_name_of_piece).strip()]
        self.__shapes.append(Shape(base_shape))#1,3
        self.__shapes.append(Shape(transpose(base_shape)))#1,7
        self.__shapes.append(Shape(flip_rows(base_shape)))#3,1
        self.__shapes.append(Shape(flip_cols(transpose(base_shape))))#3,9
        self.__shapes.append(Shape(flip_rows(transpose(base_shape))))#7,1
        self.__shapes.append(Shape(flip_cols(base_shape)))#7,9
        self.__shapes.append(Shape(flip_rows(flip_cols(transpose(base_shape)))))#9,3
        self.__shapes.append(Shape(flip_cols(flip_rows(base_shape))))#9,7
        self.__shapes= remove_duplicates(self.__shapes)

    def get_name(self):
        return self.__distinct_name_of_piece

    def get_current_shape(self):
        return self.__current_shape

    def set_fit_shapes(self, board, position):
        self.__fit_shapes = []
        for shape in self.__shapes:
            if shape.fit(board, position):
                self.__fit_shapes.append(shape)

    def get_fit_shapes(self):
        return self.__fit_shapes

    def get_fit_shape(self):
        if len(self.__fit_shapes) == 0:
            return None
        chosen_fit_shape = self.__fit_shapes[self.__round_robbin_index]
        self.__round_robbin_index = (self.__round_robbin_index + 1) % len(self.__fit_shapes)
        #simple soluton, modulus loop
        return chosen_fit_shape

    def add(self, board, shape, position):
        self.__current_shape = shape
        shape.add(board, position, self.__distinct_name_of_piece)

    def remove(self, board):
        self.__current_shape.remove(board)
        self.__current_shape = None


# TABLE1 = [[1,1], [1,0], [1,1]] 
# TABLE2 = [[1,1], [1,0], [1,1]]
# TABLE3 = [[1,1,1], [1,0,1]]

# BOARD1 = [['o','o','-','-','-','-'],
#          ['t','t','t','-','-','-'],
#          ['-','t','-','-','-','-'],
#          ['-','L','L','z','o','-'],
#          ['o','L','z','z','-','-'],
#          ['-','L','z','-','-','o']]

# BOARD2 = [['o','o','-','-','-','-'],
#           ['-','-','-','-','z','-'],
#           ['-','-','-','z','z','-'],
#           ['-','-','-','z','o','-'],
#           ['o','-','-','-','-','-'],
#           ['-','-','-','-','-','o']]

def main(): 
    # piece = Piece('L')
    # piece.set_fit_shapes(BOARD2, (3,0))
    # shapes = piece.get_fit_shapes()
    # print(len(shapes))
    # print(piece)
    # blocker_locations = ((0,1), (0,5), (2,0), (5,1), (5,4))
    # blocker_locations = ((0,0), (0,1), (3,4), (4,0), (5,5))
    
    blocker_locations = ((0,1), (0,3), (4,3), (5,3), (5,5)) 
    a_puzzle = Puzzle(blocker_locations)
    a_puzzle.play()
    
if __name__ == '__main__':     
    main()