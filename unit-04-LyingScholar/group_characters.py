def is_upper(letter):
    ascii_value = ord(letter)
    if ascii_value >= 65 and ascii_value <= 90:
        return True
    else:
        return False
    

def is_lower(letter):
    ascii_value = ord(letter)
    if ascii_value >= 97 and ascii_value <= 122:
        return True
    else:
        return False
    

def is_digit(letter):
    ascii_value = ord(letter)
    if ascii_value >= 48 and ascii_value <= 57:
        return True
    else:
        return False
    
def group_characters(sentence):
    sorted = ""
    for char in sentence:
        if (is_digit(char) == True):
            sorted = sorted + char
        else:
            continue
    for char in sentence:
        if (is_lower(char) == True):
            sorted = sorted + char
        else:
            continue
    for char in sentence:
        if (is_upper(char) == True):
            sorted = sorted + char
        else:
            continue
    return sorted

def main():
    i = 0
    while(i<3):
        x = input("\nEnter a string consisting of letters and digits:")
        i += 1
        if x == "":
            break
        print(group_characters(str(x)))
main()