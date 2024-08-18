
import random
import arrays
import array_utils

def create_big_wheel():
    return array_utils.range_array(5,105,step=5)

def big_wheel_values(array_base):
    print('Big Wheel Values:')
    for i in range(len(array_base)):
        print(array_base[i],',',sep = "",end ="")

def spin_wheel(array):
    return int(array[random.randrange(0,len(array))])

def run_round(array,threshold):
    spin1 = spin_wheel(array)
    if spin1> threshold:
        return spin1
    else:
        spin2 = spin_wheel(array)
        return spin1+spin2

def results_printer(array,counter=0):
    if counter<len(array):
        print(array[counter])
        counter +=1
        results_printer(array,counter)
    else:
        return

def results_sum(array,counter=0,sum = 0):
    if counter<len(array):
        sum = sum + array[counter]
        counter +=1
        results_sum(array,counter,sum)
        return sum
    else:
        return sum

def less_than_100_checker(array,counter=0,num = 0):
    if counter<len(array):
        if array[counter]>100:
            counter +=1
            less_than_100_checker(array,counter,num)
        else:
            num +=1
            counter +=1
            less_than_100_checker(array,counter,num)
        return num
    else:
        return num

def main():
    spin_threshold = int(input("Enter Spin Threshold To Spin a Second Time (between 5 and 100): "))

    Number_of_Rounds = int(input("How Many rounds to run the simulation (between 1 and 100): "))
    big_wheel_array = create_big_wheel()
    big_wheel_values(big_wheel_array)
    results_array = arrays.Array(Number_of_Rounds)
    for i in range(Number_of_Rounds):
        results_array[i]=run_round(big_wheel_array,spin_threshold)
    print("\nResults from",Number_of_Rounds,"rounds:")
    results_printer(results_array)
    print("Sum: ",results_sum(results_array))
    print("Rounds less than or equal to $100: ",less_than_100_checker(results_array))
    print("Average: ", results_sum(results_array)/Number_of_Rounds)



if __name__ == '__main__':
    main ()