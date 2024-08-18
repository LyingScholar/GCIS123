
def ascii_functions():
    print(ord("A"), ord("a"))
    print(chr(65120), chr(97))

def print_user_info(name,age,address):
    print(name,age,address)
global_variable = (int(ord("A")) - 1)   
def alphabet_position(char_value):
    if ((int(ord(char_value))-global_variable)<27):
       number = (int(ord(char_value))-global_variable)
    else:
        number = (int(ord(char_value))-global_variable)   - 32
    
    print (char_value, "is in position",number,"in alphabet")
def main():
    # ascii_functions()
    # print_user_info("Sam",10,"RIT")
    alphabet_position(input("Enter character(if you dare):"))
    alphabet_position(input("Enter character(if you dare):")) 
    alphabet_position(input("Enter character(if you dare):"))

main()