import math
import random

PI = 3.14
def squared(nbr):
    invalid = 12/0
    return math.pow(nbr,2)

def circle_circumference(radius):
    return PI * radius * 2

def additionalSquared(nbr):
    value = squared(nbr)
    return value

def cubed(nbr):
    return math.pow(nbr,3)

def even_or_odd(nbr):
    if nbr % 2 ==0:
        return "even"
    if nbr % 2 !=0:
        return "odd"
    
def coin_toss():
    toss = random.randint(1,2)
    if toss == 1:
        return "heads"
    if toss == 2:
        return "tails"
    

def main():
    # nbr = int(input("Enter a number: "))
    # print("square:", squared(nbr))
    # print("cube:", cubed(nbr))
    # print(even_or_odd(nbr))
    # print(coin_toss())    
    # print(coin_toss())    
    # print(coin_toss())    
    
    # random.seed(100)
    # print(random.random())
    # print(random.random())
    # print(random.random())
    # print(random.randint(1,100))
    # print(random.randint(1,100))
    # print(random.randint(1,100))
    # print(random.randrange(1,100))
    # print(random.randrange(1,100))
    # print(random.randrange(1,100))
    print(circle_circumference(4))
    
if __name__ == "__main__":
    main()
    
main()