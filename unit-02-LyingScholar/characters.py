def add_chars(char1,char2):
    print(chr(int(char1)+int(char2))+"\n")
def subtract_chars(char1,char2):
    print(chr(int(char1)-int(char2))+"\n")
def main():
    add_chars(ord(input("Enter first character:\n")),ord(input("Enter second character:\n")))
    subtract_chars(ord(input("Enter first character:\n")),ord(input("Enter second character:\n")))
main()

# I do see wierd characters but they are just part of the ASCII table. I understand that the ASCII table is much larger than the english alphabets
# I haven't seen errors in the subtractiong function when the ASCII number is negative, I fixed it by just flipping the 2 characters
# I haven't seen any other errors regarding symbols