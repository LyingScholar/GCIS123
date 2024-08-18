def division():
    first_value = input("Enter first number")
    second_value = input("Enter second number")
    
    try:
        first_nbr = int(first_value)
        second_nbr = int(second_value)
        print(first_nbr/second_nbr)
    except ValueError:
        print("cannot convert string to number")
    except ZeroDivisionError:
        print("cannot divide by zero")
    finally:
        print("in the finally")
    return first_nbr - second_nbr

def validatePassword(password):
    if password == "":
        raise ValueError("Password is blank")
    elif len(password) < 5 or len(password) > 10:
        raise ValueError("Invalid password length")
    else:
        return "corret value"
def ask_password():
    try:
        password = input("enter password:")
        validatePassword(password)
    except ValueError as value_error:
        print("Error:", value_error)
        raise value_error

def numbers(filename):
    sum = 0
    with open(filename) as file:
        for line in file:        
            nbr = int(line.strip())
            sum += nbr
            
    print("total sum:", sum)

def main():
    # try:
    #     ask_password()
    # except:
    #     print("Main error")
    ask_password()

if __name__ == "__main__":
    main()    