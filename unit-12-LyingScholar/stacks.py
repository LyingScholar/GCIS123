from list_stack import Stack

def process_file(filename):
    main_stack = Stack()


    with open(filename, 'r') as file:
        for line in file:
            line_stack = Stack()
            for char in line.strip():
                line_stack.push(char)
            main_stack.push(line_stack)
    return main_stack

def process_stack(main_stack):
    while not main_stack.isEmpty():
        line_stack = main_stack.peek()

        while not line_stack.isEmpty():
            char = line_stack.peek()
            print(char, end='')
            line_stack.pop()
        print()
        main_stack.pop()

def main():
    filename = "unit-12-LyingScholar\data\walrus.txt"
    main_stack = process_file(filename)

    process_stack(main_stack)


main()