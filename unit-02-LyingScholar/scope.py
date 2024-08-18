global_var = "hello world"

def prameter_function(parameter_var):
    global_var = "hello world function"
    local_var = "Local Variable"

    print(global_var, parameter_var,local_var)

def main():
    prameter_function("paramater value")
    print (global_var)

main()