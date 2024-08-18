import arrays

def dict_examples():
    data = {1:"one",3:"three",2:"two"}
    print(data.keys())
    
    for value in data.keys():
        print(value, data[value])
    print('\n')
    for value in sorted(data.keys()):
        print(value, data[value])
    
def unique_words(filename):
    words = {}
    with open(filename) as file:
        for line in file:
            for word in line.split():
                if word in words:
                    words[word] +=1
                else:
                    words[word] = 1
    return words

def collision(filename,length,hash_func=hash):
    arr = arrays.Array(length,None)
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            hash_code = hash_func(line)
            index = hash_code% length
            if arr[index] == None:
                arr[index] = line
                count += 1
            else:
                return count
    
def make_myset(size,hash_fuc=hash):
    my_list = [[] for _ in range(size)]
    return hash_fuc, my_list

def add(myset,element):
    hash_func = myset[0]
    length = len(myset[1])
    hash = hash_func(element)
    index = hash%length
    list_row = myset[1][index]
    for val in list_row:
        if val == element:
            return
    myset[1][index].append(element)
    
def get(myset,element):
    hash_func = myset[0]
    length = len(myset[1])
    hash = hash_func(element)
    index = hash%length
    list_row = myset[1][index]
    for val in list_row:
        if val == element:
            return True
    return False
    
    
def string_hash(a_string):
    maxord = 0
    for char in a_string:
        if ord(char)>maxord:
            maxord = ord(char)
        else:
            continue
    return maxord

def main():
    # dict_examples()
    filename = './data/alice.txt'

    print(len(unique_words(filename)))
    print('collision test with 10', collision(filename,10,string_hash))
    print('collision test with 10', collision(filename,100000000,string_hash))
    
    
    # myset = make_myset(10)
    # print(myset)
    # add(myset,"abc")
    # add(myset,"abc1")
    # add(myset,"abc1sdfghjkl;lkjhgfdxszxcdfvgbhnjmk")
    # print(myset[1])
    # print(get(myset,"abc1"))
    # print(get(myset,"abc2"))
    
    
if __name__=="__main__":
    main()