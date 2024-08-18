import math

def add(x,y):
    return str(x)+" + "+str(y)+" = "+str(x+y)

def subtract(x,y):
    return str(x)+" - "+str(y)+" = "+str(x-y)

def multiply(x,y):
    return str(x)+" * "+str(y)+" = "+str(x*y)

def divide(x,y):
    if y != 0:
        return str(x)+" / "+str(y)+" = "+str(x/y)
    else:
        return str(x)+" / "+str(y)+" = NaN"

def exponent(x,y):
    return str(x)+"^"+str(y)+" = "+str(pow(x,y))
   
def main():
    #probably better for actual calculations, but output not equal to the assignment requirement
    # x= float(input("enter x: "))
    # y= float(input("enter y: "))
  
    x= int(input("enter x: "))
    y= int(input("enter y: "))
    
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
    print(exponent(x,y))
    
if __name__ == "__main__":
    main()