from node import Node
class Stack:
    __slots__ = ['__top','__size']
        
    def __init__(self):
        self.__top = None
        self.__size = 0
        
    def isEmpty(self):
        return self.__size == 0
    
    def __str__(self):
        data = []
        node = self.__top
        while node is not None:
            data.append(node.getValue())
            node = node.getNext()
            
        return str(data)
    
    def __len__(self):
        return self.__size
        
    def push(self,value):
        new_node  = Node(value,self.__top)
        self.__top = new_node
        self.__size += 1
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.__top.getValue()


def main():
    s=Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    s.push(3)
    print(s)

main()