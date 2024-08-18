import math

def fact(numbur):
    if (numbur> -1):
        return math.factorial(int(numbur))
    else:
        return 0

def root(numbur):
    if (numbur> 0):
        return math.sqrt(numbur)
    else:
        return 0

def trunk(numbur):
    return math.trunc(numbur)

def main():
    User_input = float(input("Please enter a number:\n"))
    print("factorial :",fact(User_input),"\nroot :",root(User_input),"\ntrunk :",trunk(User_input))
    
if __name__ == "__main__":
    print(main())