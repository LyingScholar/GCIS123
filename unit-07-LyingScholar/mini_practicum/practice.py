import array_utils
import random

def Max(arr,index=0,max=None):
    if index < 0 or len(arr)==0:
        return None
    if max==None:
        max = arr[0]
    if index == len(arr):
        if max > arr[index-1]:
            return max
        else:
            return arr[index-1]
    if arr[index]>max:
        max = arr[index]
    else:
        print("")
    return Max(arr,index+1, max)

def power(base,expo):
    if expo<0:
        raise ValueError
    if expo==0:
        return 1
    if expo%2 ==0:
        return power(base,expo//2) * power(base,expo//2)
    else:
        return base * power(base,expo//2) * power(base,expo//2)

def main():
    int_data = 100
    # lst_data = list(range(4))
    # mutator(lst_data,int_data)
    # print("after function call",int_data,lst_data)
    

if __name__ == "__main__":
    main ()