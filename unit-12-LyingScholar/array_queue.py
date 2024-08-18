import arrays

class Queue:
    __slots__ = ['__elements', '__front', '__back', '__size']

    def __init__(self, cap= 10):
        self.__elements = arrays.Array(cap)
        self.__front = 0
        self.__back = 0
        self.__size = 0
        
    def __str__(self):
        output =[]
        i= self.__front
        while i != self.__back:
            output.append(self.__elements[i])
            i = (i+1)% len(self.__elements)
        return str(output)
    
    def get_elements(self):
        return self.__elements
    
    def is_empty(self):
        return self.__size == 0

    def _len_(self):
        return self.__size

    def enqueue(self, value):
        self.__elements[self.__back] = value

        self.__back = (self.__back +1)% len(self.__elements)
        self.__size += 1
        
    def front(self):
        if self.__size == 0:
            raise IndexError("queue is empty")
        return self.__elements[self.__front]
    def back(self):
        if self.__size == 0:
            raise IndexError("queue is empty")
        if self.__size == 1:
            return None
        back_index = self.__back -1
        
        return self.__elements[back_index]
    def dequeue(self):
        data = self.__elements[self.__front]
        self.__elements[self.__front]= None
        self.__front = (self.__front+1) % len(self.__elements)
        self.__size -= 1
        return data
    
def main():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    print(q)

main()