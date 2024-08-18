def triangle_type(side1,side2,side3):
    
    # if side1 == side2 and side2 == side3:
    #     return "equilateral"
    # if side1 == side2 or side2 == side3 or side3 == side1:
    #     return "isoscles"
    
    # return "scalene"
    if side1 == side2 and side2 == side3:
        return "equilateral"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "isoscles"
    else:
        return "scalene"

def main():
    print(triangle_type(1,3,5))
    
if __name__ == "__main__":
    main()