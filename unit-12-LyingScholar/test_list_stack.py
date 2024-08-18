from list_stack import Stack

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert len(stack) == 1



def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert len(stack) == 2

def test_len():
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    assert len(stack) == 1
    stack.push(2)
    assert len(stack) == 2


def test_multiple_stacks():
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack2.push('a')
    stack2.push('b')
    stack2.push('c')

    assert len(stack1) == 2
    assert len(stack2) == 3

    assert stack1.peek() == 2
    assert stack2.peek() == 'c'

    assert stack1.pop() == 2
    assert stack2.pop() == 'c'

    assert len(stack1) == 1
    assert len(stack2) == 2

    assert stack1.isEmpty() == False
    assert stack2.isEmpty() == False

#you made me write tests, i hate you
def test_empty_stack():
    stack = Stack()
    assert stack.isEmpty() == True
    
#not really, just a little bit