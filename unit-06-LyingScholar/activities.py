import arrays
import random
import math
import time
import searches
import array_utils

def make_array():
    array1=arrays.Array(10)
    print(array1)
    
    array2=arrays.Array(10,"a")
    print(array2)
    
    array3=arrays.Array(10,True)
    array3[3]=False
    print(array3)
    
    for data in range(len(array3)):
        print(array3[data], end="")
    
    counter = 0
    while counter < len(array3):
        print(array3[counter],end="")
        counter +=1

def while_fill(array):
    counter = 0
    while counter < len(array):
        array[counter]= int(math.pow(counter+1,2))
        counter +=1
def for_fill(array):
    for counter in range(len(array)):
        array[counter]= int(math.pow(counter+1,2))
        counter +=1

def roll_a_die(sides):
    # die_array = arrays.Array(sides)
    # for counter in range(len(die_array)):
    #      die_array[counter]= int(counter+1)
    #      counter +=1
    return random.randint(1,sides)

def linear_search_time(arr,target):
    start_time = time.perf_counter()
    searches.linear_search(arr,target)
    end_time = time.perf_counter()
    elapsed = end_time -start_time
    print("elapsed time:", elapsed)

def count_down(nbr):
    for i in range(nbr):
        print(nbr-i,end="")

def count_down_rec(nbr):
    if nbr == 0:
        return
    print(nbr, end=" ")
    count_down_rec(nbr-1)

def factorial(nbr):
    if nbr==0 or nbr == 1:
        return 1
    return nbr*factorial(nbr-1)

def count_up_rec(nbr):
    if nbr == 0:
        return
    count_up_rec(nbr-1)
    print(nbr,end=" ")


def linear_search_time(arr,target):
    start_time = time.perf_counter()
    searches.binary_search(arr,target)
    end_time = time.perf_counter()
    elapsed = end_time -start_time
    print("elapsed time:", elapsed)


def binary_search(arr, nbr):
    mid = len(arr) // 2
    
    if arr[mid] == nbr:
        return mid
    elif arr[mid] > nbr:
        return binary_search(arr[:mid], nbr)
    else:
        result = binary_search(arr[mid + 1:], nbr)
        return mid + 1 + result

def main():
    make_array()
    new_array =arrays.Array(10)
    for_fill(new_array)
    print(new_array)
    random.seed(10)
    for i in range(10):
        print(roll_a_die(6), end="")
    arr =array_utils.range_array(1,10000000)
    linear_search_time(arr,1)
    linear_search_time(arr,len(arr)/2)
    linear_search_time(arr,len(arr))
    count_up_rec(10)
    print(factorial(1000))


if __name__ == "__main__":
    main ()