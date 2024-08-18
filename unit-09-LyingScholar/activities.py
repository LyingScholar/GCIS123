import arrays
import random



def unique_array(arr, value):
    for index in range(len(arr)):
        if arr[index] == value:
            return
        
        elif arr[index] == None:
            arr[index] = value
            return
    
def fill_array(len):
    arr = arrays.Array(len, None)
    for value in range(len):
        unique_array(arr, value)
        
def unique_list(array, value):
    for index in range(len(array)):
        if array[index] == value:
            return
    array.append(value)

def fill_list(len):
    arr = []
    for value in range(len):
        unique_list(arr, value)

def unique_set(arr, value):
    if not value in arr:
        arr.add(value)

def fill_set(len):
    arr = set()
    for value in range(len):
        unique_set(arr, value)

def coupon_collector(n):
    coupons = set()
    boxes = 0
    while len(coupons) < n:
        value = random.randrange(1, n+1)
        coupons.add(value)
        boxes += 1
    return boxes

def unique_words(file_name):
    unique_words = set()
    with open(file_name) as file:
        for line in file:
            words = line.split()
            for word in words:
                unique_words.add(word)
    return len(unique_words)

def intersection(a, b):
    c = set()
    for value in a:
        if value in b:
            c.add(value)
    return c


def main():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    # print(unique_words("data/alice.txt"))
    # n = 10000
    # print("Expected:", n*math.log(n) + 0.57721566*n)
    # print("Actual:", coupon_collector(n))
    # print(intersection(a, b))
    # count = 5000
    # timing.time_function(fill_array, 5000)
    # timing.time_function(fill_list, 5000)
    # timing.time_function(fill_set, 5000)

    
if __name__ == "__main__":
    main()



#dilkashi, uns, mohaebbat, aqeedat, ibadat, junoon, maut