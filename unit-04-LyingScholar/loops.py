def while_loop():
    counter = 0
    while counter < 5:
        print(counter)
        counter = counter + 1

def print_even_nbr():
    counter = 0
    max_value = 100
    sum = 0

    while True:
        
        sum = sum + counter
        counter = counter + 1
        if counter > max_value:
            break
        if(counter % 2 == 0):
            print(counter, end =" ")
        else:
            continue

                    
    print("Sum = ",sum)        

def loop_test_using_while(message):
    index = 0
    while index<len(message):
        print(message[index],end=" ")
        index +=1

def loop_using_for(message):
    for loop_var in message:
        print(loop_var, end = " ")
def main():
    # while_loop() 
    # print_even_nbr() 
    range_var = range(10)
    str_value = "one,two,three,four,five"
    # loop_test_using_while(range_var)
    tokens = str_value.split(",")
    loop_using_for(tokens)
    # loop_using_for("this is test")

if __name__ == "__main__":    
    main()