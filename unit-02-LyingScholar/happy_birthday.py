
def ask_question():
    #i think the name of the file is self explanatory but if this seems complex to you, try HTML

    """
    please kill yourself in minecraft
    """
    name = input("Enter name: ")
    '''
    Here you ask user for their name
    '''
    month = input("Enter birth month: ")
    '''
    Here you ask user for their birth month
    '''
    day = input("Enter day of birth: ")
    '''
    Here you ask user for their birth day
    '''
    year = input("Enter birth year: ")
    '''
    Here you ask user for their year of birth
    '''
    print("Thank you",name,"your birthday is",day,month,year)

# ask_question()

def main():
    print(ask_question.__doc__)

main()    