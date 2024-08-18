prices = {

    'Soda' : 1.95,
    'Milk shake' : 2.95,
    'Tea' : 2.15,

    'Burger' :  3.95,
    'Cheese burger' : 4.45,
    'Chicken fingers' : 4.95,

    'Fries' : 1.95 ,  
    'Waffle fries' : 2.95,
    'Tater tots' : 2.45,
    'Side salad' : 2.25,
    }


codes = {}
for item in prices:
    code_list = [name_of_food[0] for name_of_food in item.split()]
    try:
        code = code_list[0] + code_list[1]
        #i've assumed menu has 2 named items only as per example provided
    except:
        code = code_list[0]
    codes[code.lower()] = item
    # print(codes)



class Combo:
    __slots__ = ['drink', 'entree', 'side', 'price']

    def __init__(self, drink, entree, side, price):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.price = price


menu = [{'submenu': 'Drinks',
        'items': 
            {'Soda' : 1.95,
            'Milk shake' : 2.95,
            'Tea' : 2.15,
            }
        },
        
    {'submenu': 'Entrees',
    'items': 
        {'Burger' :  3.95,
        'Cheese burger' : 4.45,
        'Chicken fingers' : 4.95,
        }
    },
    
    
        {'submenu': 'Sides',
        'items': 
            {'Fries' : 1.95 ,  
            'Waffle fries' : 2.95,
            'Tater tots' : 2.45,
            'Side salad' : 2.25,
            }
        }
    ]


def print_menu():
    for category in menu:
        print("\n"+category['submenu'] + " :")
        
        for item in category['items'].items():
            item_name = item[0]
            item_price = category['items'][item[0]]
            code = ""
            for word in item_name.split():
                code += word[0]
            code = code.lower()
            print(item_name,"(",code,")", " : $",item_price)

# print_menu()

def order_combo():
    drink = input("What would you like to drink: ")
    entree = input("What would you like for your entree: ")
    side = input("What would you like for your side: ")
    
    price = prices[codes[drink]] + prices[codes[entree]] + prices[codes[side]]
    return Combo(drink, entree, side, price)


def ordering():
    order = []
    while True:
        combo = order_combo()
        order.append(combo)
        more = input("Would you like to add another combo (Y/N): ")
        if more.lower() != 'y':
            break
    return order


def main():
    print("Welcome to the ASCII Food Truck!")
    print("Here's the menu:")
    print("(All orders are combos)\n")
    print_menu()
    order = ordering()
    print("Your order:")
    total_price = 0
    for combo in order:
        print("Drink: ",codes[combo.drink]," $",prices[codes[combo.drink]], "\nEntree: ",codes[combo.entree]," $", prices[codes[combo.entree]],"\nSide: ",codes[combo.side]," $", prices[codes[combo.side]], "\nCombo Price: $",round(combo.price,3))
        total_price += combo.price
    print("\nTotal: $",round(total_price,3))

if __name__ == "__main__":
    main()