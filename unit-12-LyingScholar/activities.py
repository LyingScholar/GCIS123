from node import Node

def length_iter(node):
    while node is not None:
        count+=1
        node = node.getNext()
    return count

def sum(node, sum = 0):
    if node.getNext() == None:
        return sum + node.getValue()
    else:
        sum += node.getValue()
        return sum(node.getValue(),sum)

# def sum(node, sum = 0):
#     while node is not None:
#         sum+=node
#         node = node.getNext()
#     return sum

        
def main():
    engine = Node(1)
    passenger_car = Node(2)
    tanker_car = Node(3)
    box_car= Node(4)
    engine.setNext(passenger_car)
    passenger_car.setNext(tanker_car)
    tanker_car.setNext(box_car)