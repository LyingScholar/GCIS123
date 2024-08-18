def increasing_comparator(a,b):
    return a<=b

def decreasing_comparator(a,b):
    return a>=b

def linear_search(an_array, target):
    """
    Searches an array for a target value.
    """
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None

def binary_search(an_array, target,comparator = increasing_comparator, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(an_array) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        # print("target =", target, "start =", start, "end =", end,
        #     "mid =", mid, "value =", an_array[mid])
        if an_array[mid] == target:
            return mid
        elif comparator(an_array[mid], target):
            start = mid + 1
            return binary_search(an_array, target, comparator, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, comparator, start, end)

def main():
    an_array = list(range(10000001,0,-1))
    print(binary_search(an_array, 1,decreasing_comparator))
    print(binary_search(an_array, 5000000,decreasing_comparator))
    print(binary_search(an_array, 10000000,decreasing_comparator))
    print(binary_search(an_array, 0,decreasing_comparator))

if __name__ == "__main__":
    main()