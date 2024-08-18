import arrays
import random
import math
import array_utils
def linear_search(an_array,value,start=None,end=None):
    if start == None or start < 0:
        start = 0
        
    if end == None or start < 0 or end > len(an_array):
        end =  len(an_array)
    
    for i in range(end-start):
        if an_array[start+i]== value:
            return start+i
    # for i in range(len(an_array)):
    #     if an_array[i]== value:
    #         return i

def binary_search(arr,target,start=None,end=None):
    if start == None or start < 0:
        start = 0    
    if end == None or end > len(arr):
        end = len(arr)-1
    if target>arr[end]:
        return None
    
    middle = (start + end)//2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search(arr, target, middle + 1, end)
    elif arr[middle] > target:
        return binary_search(arr, target, start, middle - 1)
    else:
        return None
    

def jump_search(arr, target):
    step = int(math.sqrt(len(arr)))
    current_step = int(math.sqrt(len(arr)))
    while  current_step<len(arr)-step:
        current_step += step
        if arr[current_step] == target:
            return current_step
        elif arr[current_step] < target:
            continue
        elif arr[current_step] > target:
            return linear_search(arr,target,current_step-step,current_step)


def main():
    print(linear_search(array_utils.range_array(1,100,1),40))

if __name__ == "__main__":
    main ()