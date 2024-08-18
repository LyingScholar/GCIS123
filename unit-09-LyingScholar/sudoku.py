import random
import math
import time

def print_board(board):
    RED = "\033[31m"
    BLACK = "\033[37m"
    
    N = len(board)
    n = math.floor(math.sqrt(N))
    assert N == n*n

    board_string = ""
    for row in range(N):
        if row > 0 and row % n == 0:
            board_string += "\n"
        for col in range(N):
            if col > 0 and col % n == 0: 
                board_string += " "
            value = board[row][col]
            if value != 0:
                board_string += RED
            else:
                board_string += BLACK
            board_string += "[{:02.0f}]".format(value)
            
        board_string += "\n" + BLACK

    print(board_string)

def make_puzzle(N):
    n = int(N**(1/2))
    board = [[0] * N for _ in range(N)]
    #this is here just because assignments wants me to print the empty board
    print_board(board)
    nums = list(range(1, N + 1))
    random.shuffle(nums)
    
    for num in nums:
        while True:
            i, j = random.randint(0, N - 1), random.randint(0, N - 1)
            if board[i][j] == 0:
                board[i][j] = num
                break
    
    row_sets = []
    for row in board:
        row_set = set()
        for value in row:
            if value != 0:
                row_set.add(value)
        row_sets.append(row_set)
    
    col_sets = []
    for col in range(N):
        col_set = set()
        for row in range(N):
            value = board[row][col]
            if value != 0:
                col_set.add(value)
        col_sets.append(col_set)
    
    # print(row_sets)    
    # print(col_sets)
    # row_sets = [set(filter(lambda x: x != 0, row)) for row in board]
    # col_sets = [set(filter(lambda x: x != 0, [board[i][j] for i in range(N)])) for j in range(N)]
    reg_sets = []

    # print(row_sets)
    # print(col_sets)
        
    for i in range(n):
        for j in range(n):
            reg = []
            for r in range(i * n, (i + 1) * n):
                for c in range(j * n, (j + 1) * n):
                    value = board[r][c]
                    if value != 0:
                        reg.append(value)
            reg_sets.append(set(reg))
    print(reg_sets)
    
    puzzle = {
        'board': board,
        'row_sets': row_sets,
        'col_sets': col_sets,
        'reg_sets': reg_sets
    }
    
    return puzzle

def get_square(puzzle, row, col):
    board_as_a_variable = puzzle['board']
    row_sets_as_a_local_list = puzzle['row_sets']
    col_sets_as_a_local_list = puzzle['col_sets']
    reg_sets_as_a_local_list = puzzle['reg_sets']
    
    
    value = board_as_a_variable[row][col]
    row_set_of_value = row_sets_as_a_local_list[row]
    col_set_of_value = col_sets_as_a_local_list[col]
    
    
    # col_set_of_value = set()
    # for r in range(len(board_as_a_variable)):
    #     value = board_as_a_variable[r][col]
    #     if value != 0:
    #         col_set_of_value.add(value)
    
    reg_size = int(len(board_as_a_variable) ** 0.5)
    reg_row = row // reg_size
    reg_col = col // reg_size
    
    #this took waaaaaaay too long to figure out
    reg_index = reg_row * reg_size + reg_col
    reg_sets_of_value = reg_sets_as_a_local_list[reg_index]
    
    
    square_information = {
        'value': value,
        'row_set': row_set_of_value,
        'col_set': col_set_of_value,
        'reg_set': reg_sets_of_value
    }
    
    return square_information
    pass

def move(puzzle, row, col, new_value):
    square_information = get_square(puzzle, row, col)
    
    if square_information['value'] != 0:
        return False
    
    if new_value in square_information['row_set'] or new_value in square_information['col_set'] or new_value in square_information['reg_set']:
        return False
    reg = square_information['reg_set']
    puzzle['board'][row][col] = new_value
    square_information['row_set'].add(new_value)
    square_information['col_set'].add(new_value)
    square_information['reg_set'].add(new_value)
    #Is this necessary? Do i need to calculate the reg_index everytime? in each function?
    #Maybe i'll make a helper function...
    #NAH, I'm lazy af
    # reg_size = int(len(puzzle['board']) ** 0.5)
    # reg_row = row // reg_size
    # reg_col = col // reg_size
    # reg_index = reg_row * reg_size + reg_col
    # puzzle['reg_sets'][reg_index].add(new_value)
    
    return True

def fill_puzzle(puzzle):
    
    N = len(puzzle['board'])
    attempts = 0
    attempts_limit = N**4
    while attempts < attempts_limit and filled_cells_percentage(puzzle,N) < 75:
        row = random.randint(0, N - 1)
        col = random.randint(0, N - 1)
        value = random.randint(1, N)
        attempts += 1
        
        move(puzzle, row, col, value)
            
    print("board is filled :", filled_cells_percentage(puzzle,N), "percentage")
    return puzzle
    
def filled_cells_percentage(puzzle,N):
    board_as_a_variable =  puzzle['board']
    filled_cells = 0
    for row in range(N):
        for col in range(N):
            if board_as_a_variable[row][col] != 0:
                filled_cells += 1 
    return filled_cells *100 / (N**2)
    pass

def main():
    N = 64
    # N = 9
    # print("Board size:", N, "x", N)
    puzzle = make_puzzle(N)
    print_board(puzzle['board'])
    # print(puzzle)
    # print("Initial puzzle:")
    # print(puzzle,sep = "/n")
    # print("Initial board:")
    start = time.perf_counter()
    fill_puzzle(puzzle)
    print_board(puzzle['board'])
    end = time.perf_counter()
    
    print("Total time elapsed: ",end - start)
    
main()
