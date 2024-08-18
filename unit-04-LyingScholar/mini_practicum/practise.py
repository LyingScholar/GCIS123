import random
def absolute_difference(a,b):
    if(a-b>0):
        return a-b
    else:
        return b-a
    
def main():
    global a
    global b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    print("a=",a,", b=",b," absolute difference=",absolute_difference(a,b))
    
if __name__ == "__main__":
    main()