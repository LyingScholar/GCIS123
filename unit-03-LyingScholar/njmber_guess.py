import random
MIN = 0
MAX = 100
number = random.randint(MIN,MAX)

def check_number(x):
    inp = int(input("guess who??"))
    if(x < 6):
        if (inp > number):
            print("Too high")
            check_number(x+1)
        if (inp < number):
            print("Too low")
            check_number(x+1)
        if (inp == number):
            print("You won. But at what cost? You wasted precious moments of your life. You're pathetic. Nobody loves you. KY")
    else:
        print("bohooo, you're out of tries. Can't even win at a text game. What will you do with your life. You're pathetic. Nobody loves you. KY")
def main():
    check_number(1)
    
main()