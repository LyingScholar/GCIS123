from node_stack import Stack


def reverse_digits_1(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str)
    return reversed_num

'''
    Just in case you have an expectation of stacks
'''

def reverse_digits(number):
    main_stack = Stack()
    reversed = ""
    for char in str(number):
        main_stack.push(char)
    
    while not main_stack.is_empty():
        reversed = reversed + str(main_stack.pop)

    return int(reversed)




import random

def toss(player_a,names):
        player_b = random.choice(names)

        while player_a == player_b:
            player_b = random.choice(names)

        print(f"{player_a} tosses the potato to {player_b}")
        return player_b

def hot_potato(names):
    
        
    while len(names) > 1:
        print("\nNew round starts!")
        tosses = random.randint(1, 5)
        holder = random.choice(names)
        for i in range(tosses):
            holder = toss(holder,names)
        
        print(f"\nThe music stops and",holder,"is holding the potato!")
        names.remove(holder)

    print(f"\nThe game is over!",names[0],"wins the game!")
    
hot_potato(["a","b","c","d","e","f","g"])