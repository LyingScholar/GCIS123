import random

def random_list(len):
    return [random.randrange(len) for _ in range(len)]

def swap(lst,first_pos,second_pos):
    temp = lst[first_pos]
    lst[first_pos] = lst[second_pos]
    lst[second_pos] = temp

def shift(lst,index):
    # temp = lst[index]
    while index > 0 and lst[index-1]>lst[index]:
        swap(lst,index,index-1)
        index -=1

def shift_no_swap(lst,index):
    index_value = lst[index]
    counter = index_value
    while counter > 0 and lst[counter-1]>lst[counter]:
        lst[counter] = lst[counter-1]
        counter -=1
    lst[counter] = index_value
    
def insertion_sort(list):
    for i in range(len(list)):
        shift(list,i)

def insertion_sort_no_swap(list):
    for i in range(len(list)):
        shift_no_swap(list,i)

def split(lista):
    mid = (len(lista)) // 2
    
    return lista[:mid],lista[mid:]

def merge(list1,list2):
    merged = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] <= list2[i2]:
            merged.append(list1[i1])
            i1 = i1 + 1
        elif list1[i1] > list2[i2]:
            merged.append(list2[i2])
            i2 = i2 + 1
    if i1 < len(list1):
        merged = merged + (list1[i1:])
    else:
        merged= merged + (list2[i2:])
    return merged

def partition(alist):
    if len(alist) <=1:
        return alist
    less = []
    same = []
    more = []
    pivot = alist[0]
    for i in range(len(alist)):
        if alist[i]>pivot:
            more.append(alist[i])
        elif alist[i]<pivot:
            less.append(alist[i])
        else:
            same.append(alist[i])
    return less, same, more

def quick_sort(alist):
    if len(alist) <=1:
        return alist
    less = []
    same = []
    more = []
    pivot = alist[0]
    for i in range(len(alist)):
        if alist[i]>pivot:
            more.append(alist[i])
        elif alist[i]<pivot:
            less.append(alist[i])
        else:
            same.append(alist[i])
    return quick_sort(less)+ same+ quick_sort(more)

def merge_sort(a_list):
    if len(a_list)<= 1:
        return a_list
    else:
        left,right = split(a_list)
        return merge(merge_sort(left), merge_sort(right))


def main():
    rand_list = random_list(10)
    print(rand_list)
    # swap(rand_list,2,3)
    # insertion_sort(rand_list)
    # insertion_sort_no_swap(rand_list)
    # print(rand_list)
    # print(split(rand_list))
    # print(random_list(10))
    # print(merge_sort(rand_list))
    print(quick_sort(rand_list))

if __name__ == "__main__":
    main()