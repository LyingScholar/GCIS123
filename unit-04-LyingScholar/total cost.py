def calculate_total_cost(quantity):
    if 0 < quantity and quantity < 10:
        return (50 * quantity)
    elif 9 < quantity and quantity < 20:
        return (45 * quantity)
    elif 19 < quantity and quantity < 30:
        return (38 * quantity)
    else:
        return (32 * quantity)
    
def main():
    i = 1
    while i>0:
        User_input = int(input("Enter a quantity to be purchased: ") )
        i += 1
        if (User_input>0):
            print("Total cost: ",calculate_total_cost(User_input))
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()