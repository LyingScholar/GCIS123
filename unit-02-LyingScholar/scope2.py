global_var1 = "hello world"
global_var2 = "hi life"
global_var3 = "greetings universe"
def print_param(parameter1):
    print(parameter1)
def print_local():
    local_variable1 = "yo peeps"
    print(local_variable1)
def print_which():
    global_var1 = "adios muchachos"
    print(global_var1)
def main():
    print_param(global_var1)
    print_param(global_var2)
    print_param(global_var3)
    local_variable1 = "hello humans"
    print_local()
    print_which()
    print(global_var1)
main()