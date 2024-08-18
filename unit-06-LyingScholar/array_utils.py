import arrays
import random

def random_array(size,min_value=0,max_value=None):
    array=arrays.Array(10)
    if max_value==None:
        max_value = size
    for i in range(size):
        array[i] = random.randrange(min_value,max_value)
        
def range_array(start,stop,step=1):
    range_1 = range(start,stop,step)
    array = arrays.Array(len(range_1))
    
    for i in range(len(range_1)):
        array[i]=range_1[i]
        
    return array

def main():
    print(range_array(1,20,2))

if __name__ == "__main__":
    main ()