import random
def tuples():
    a= (1,2,3,4,"a")
    b = tuple('abcdef')
    
    print(a,b)
    
    for data in a:
        print(data,end=" ")
    print()
    for data in  range(len(b)):
        print(b[data],end=" ")

def multiple():
    a=1
    b="b"
    c = 3
    return a,b,c


def make_list(a_sequence):
    list =[]
    for i in range(len(a_sequence)):
        list.append(a_sequence[i])
        print(list)

def scale(a_sequence, scalar):
    list =[]
    for i in range(len(a_sequence)):
        list.append(int(a_sequence[i])*scalar)
        print(list)

def mutator(ref_data,value_data):
    print("Before", ref_data,value_data)
    value_data=100
    ref_data.append("Added new value")
    print("After",ref_data,value_data)

def extender(a_list,b_list):
    a_list+=b_list
    return a_list

def insert_data(a_list,value):
    mid = len(a_list)//2
    a_list.insert(mid,value)
    return a_list

def popper(lst):
    if len(lst)>0:
        popped = lst.pop(random.randrange(len(lst)))
        print(lst,popped)
        print()

def reverse_sequence(lst):
    output =[]
    for data in range(len(lst)-1,-1,-1):
        output.append(lst[data])
    print(output)

def slices():
    txt = "Crazy? I was crazy once.They locked me in a room. A rubber room. A rubber room with rats. Rats? Rats drive me crazy."
    start = 0
    end = 0
    lst = list(txt)
    for index in range(len(lst)):
        if lst[index] == " ":
            stop = index
            word = lst[start:stop]
            print(word)
            start = stop +1

def for_loop():
    for _ in range(10):
        print(_)

# def dices(a_list):
#     if len(a_list) == 0:
#         return
#     else:
#         print(a_list.pop(random.randrange(len(a_list))))
#         dices(a_list)

def dices(a_list):
    if len(a_list) == 0:
        return
    else:
        num = random.randrange(len(a_list))
        print(a_list[num])
        b_list = a_list[:num] + a_list[num+1:]
        dices(b_list)

def swapper(List):
    mid = len(List)//2
    return List[mid:]+List[:mid]

def twod_list():
    
    a = [
        [2,3,4],
        [5,6,7],
        [8,9,10,12]
    ]
    print(a[1])
    
    for row in range(len(a)):
        print(row)
        

def sort(list):
    print("Before ", list)
    list.sort()
    new_list = sorted(list, reverse=True)
    print("After ",list,new_list)

def even_first(key):
    if key%2 !=0:
        return 100+key
    else:
        return key


def main():
    # a= multiple()
    # x,y,z = multiple()
    # print(a,type)
    # print(x,y,z)
    # tuples()
    # a =[1,2]
    # b = [3,4]
    # print(extender(a,b))
    # print(a,b)
    # print(a)
    # print(b)
    
    a = [1,2,3,6,8,9,345,4,5]
    
    # print(insert_data(a,20))
    
    # reverse_sequence(a)
    
    # slices()
    # dices(a)
    
    # twod_list()
    a.sort(key = even_first)
    print(a)
    # sort(a)

if __name__ == "__main__":
    main ()