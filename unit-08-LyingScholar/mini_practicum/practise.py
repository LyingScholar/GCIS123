def in_place_reverse(a_list):
    for i in range(len(a_list)):
        a_list.insert(i,a_list.pop())
    return a_list

def make_multiplication_table():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]

# a = [1,1,46,4,2,3,5,453,22]
# print(in_place_reverse(a))