import csv
import random
import node_stack
import array_queue
class item:
    __slots__ = "__name__", "__weight__", "__price__"
    
    def __init__(self, name,weight, price):
        self.__name__ = name
        self.__weight__= weight
        self.__price__ = price

    def get_name(self):
        return self.__name__

    def get_price(self):
        return self.__price__

    def set_price(self, price):
        if price>=0:
            self.__price__ = price

    def get_weight(self):
        return self.__weight__

    def __repr__(self):
        return "Name: " + str(self.get_name()) + ", Weight: " + str(self.get_weight())+ ", Price: "+ str(self.get_price())
    
    def __eq__(self,other):
        if type(self) == type(other):
            return self.get_name() == other.get_name()
        return False
    
    def hash(self):
        return hash(self.get_name())

    def __lt__(self,other):
        if type(self) == type(other):
            return self.get_name() < other.get_name()
        return False
    
    
    def __gt__(self,other):
        if type(self) == type(other):
            return self.get_name() > other.get_name()
        return False

class Customer:
    __slots__ = "__shopping_cart__","__shopping__list__","__bags"

    def __init__(self, shopping_list):
        self.__bags = []
        self.__shopping_cart__ = []
        self.__shopping__list__ = shopping_list
    
    def shop(self, store):
        for item in self.__shopping__list__:
            self.__shopping_cart__.add(store[item])


    def checkout(self,conveyer_belt):
        price = 0
         
        while not conveyer_belt.is_empty():
            item = conveyer_belt.dequeue()
            price += item.get_price()
            is_item_added = False
            for bag in self.__bags:
                if item.get_weight()< bag.peek().get_weight():
                    bag.push(item)
                    is_item_added = True
                    break
    
            if is_item_added == False:
                new_bag = node_stack.Stack()
                new_bag.push(item)
                self.__bags.append(new_bag)
    
    
        return price
    
    def unpack(self):
        bag_number =1
        for bag in self.__bags:
                print("Unpacking bag number "+ str(bag_number))
                bag_number+=1

                while not bag.is_empty():
                    print("     ",bag.pop())



def stock_store(file):
    stock = {}
    with open(file) as fille:
        csv_reader = csv.reader(fille)
        next(csv_reader)
        for record in csv_reader:
            name = record[0]
            grocery_item = item(name,int(record[1]),int(record[2]))
            stock[name] = grocery_item
    
    return stock

def main():
    store = stock_store("data/groceries.csv")
    # for key in store:
    #     print(key, "|",store[key])
    items = list(store.keys())
    random.shuffle(items)
    shopping_list = items[:25]



    John = Customer(shopping_list)
    John.shop(store)

    conveyer_belt = array_queue.arrays
    John.unload(conveyer_belt)


main()