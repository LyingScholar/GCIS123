

def arithmetic_expr_test():
    output = 5 -2 * 10
    output1 = 6/2 * (1+2)
    output2 = -10/ (20 / 2 ** 2 * 5 / 5) * 8 -2
    print(output, output1, output2)

def variable_test():
    int_var = 10
    float_var = 10.5
    str_var = "Hello world"
    sum = int_var + float_var

    print(int_var, float_var, str_var)

def prompt_and_print():

    number_1 = int(input("Enter a number"))
    number_2 = int(input("Enter another number"))

    print(number_1, " + ",number_2,"=",(number_1 + number_2))
    print(number_1, " - ",number_2,"=",(number_1 - number_2))
    print(number_1, " x ",number_2,"=",(number_1 * number_2))
    print(number_1, " / ",number_2,"=",(number_1 / number_2))

def prompt_and_print2():

    print("Addition: ", (int(input("Enter a number")) +  int(input("Enter another number"))))

def main():
    # variable_test()
    # arithmetic_expr_test()
    # prompt_and_print()'
     prompt_and_print2()
main()