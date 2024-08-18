import random

def create_ascii_range_string(start,stop):
    string = ""
    for i in range(int(start),int(stop)):
        string = string + chr(i)
        continue
    return string

def create_uppercase_letters_string():
    return create_ascii_range_string(65,91)

def create_lowercase_letters_string():
    return create_ascii_range_string(97,123)

def create_digits_string():
    return create_ascii_range_string(48,58)

def create_symbols_string():
    return create_ascii_range_string(33,48) + create_ascii_range_string(58,65) + create_ascii_range_string(91,97)+create_ascii_range_string(123,127)

def get_random_char_from_string(string):
    length = len(string)
    return string[random.randint(0, length-1)]

def generate_random_password(upper_case,lower_case,digits,symbols):
    password_length = int(upper_case)+int(lower_case)+int(digits)+int(symbols)
    length_password = 0
    password = ""
    u = 0
    l = 0
    d = 0
    s = 0
    for z in range (0,200000):  
        shuffler = random.randint(1,4)
        if length_password == password_length:
            break
        elif shuffler == 1 and u < upper_case:
            password = password + get_random_char_from_string(create_uppercase_letters_string())
            u+=1
            length_password+=1
        
        elif shuffler == 2 and l < lower_case:
            password = password + get_random_char_from_string(create_lowercase_letters_string())
            l+=1
            length_password+=1
        
        elif shuffler == 3 and d < digits:
            password = password + get_random_char_from_string(create_digits_string())
            d+=1
            length_password+=1
        
        elif shuffler == 4 and s < symbols:
            password = password + get_random_char_from_string(create_symbols_string())
            s+=1
            length_password+=1

    return password
            
# def shuffler(base_string):
#     shuffled_string = ""
#     for i in base_string:
#         shuffled_string = shuffled_string + " "
        
#     for i in base_string:
#         for j in range(0,100000000000000):
#             position = random.randint(0,len(base_string)-1)
#             if shuffled_string[int(position)] == " ":
#                 shuffled_string[int(position)] = str(i)
#                 break
#             else:
#                 continue
#         break
    
#     return shuffled_string
            
def main():
    while True:
        User_input = input("Enter <num uppers> <num lowers> <num digits> <num symbols>:")
        token = User_input.split()
        if User_input == "":
            print("Goodbye!")
            break
        elif len(token) != 4:
            print("You must enter exactly 4 values")
        else:
            print("Password : ",generate_random_password(int(token[0]),int(token[1]),int(token[2]),int(token[3])))
    
main()