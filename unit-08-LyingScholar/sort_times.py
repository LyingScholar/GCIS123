import random
import time
import sorts

list_size =3000
def insertion_sort_function_times(a_list):
    start = time.perf_counter()
    sorts.insertion_sort
    end = time.perf_counter()
    print("Total time elapsed: ",end - start)
    
def main():
    list = [n for n in range(6000)]
    insertion_sort_function_times(list)

    list = [random.randrange(list_size) for n in range(3000)]
    insertion_sort_function_times(list)

if __name__ == "__main__":
    main()