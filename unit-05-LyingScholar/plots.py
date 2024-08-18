import plotter
# import csv
def terminate():
    User_input = input ("Are you sure you want to quit(y/n):")
    if User_input == "y" or User_input == "Y":
        return True
    else:
        return False

def plot_grades(filename,first_name,last_name):
    try:
        with open(filename) as file:    
                for line in file:
                    words = line.split(",")
                    if words[1] == first_name and words[0]==last_name:
                        plotter.init("lab grade graph","Student","Scores")
                        plotter.new_series("Scores")
                        j = 2
                        while j<len(words):
                            plotter.add_data_point(float(words[j]))
                            j += 1
                        plotter.plot()
                        print("Plot finished (window may be hidden).")
                        return True
                    else:
                        continue
        print("Plot failed (no such student).")
        return False
    except:
        print("No such file: ", filename)

def student_grades(filename,first_name,last_name):
    plot_grades(filename,first_name,last_name)

def help():
    print("stu <filename> <first name> <last name> - plot student grades\nitem\nquit - quits\nhelp - displays this message\n") 

def main():
    z = 0
    q = True
    while q == True:
        tokens = input().split(" ")
        if tokens[0] == "":
            print("Enter a command or 'quit' to quit.")
        elif tokens[0] == "quit":
            if terminate():
                print("Goodbye!")
                q == False
                break
            else:
                continue
        elif tokens[0] == "help":
            help()
            continue
        elif z == 3:
            number3 = tokens[0]
            student_grades(number1,number2,number3)
            break
        elif z == 2:
            number2 = tokens[0]
            z+=1
            continue
        elif z == 1:
            number1 = tokens[0]
            z+=1
            continue
        elif tokens[0] == "stu" and z == 0:
            z+=1
            continue
        # break
    # plot_grades("data/grades_010.csv", "Lucresha", "Zbell")
    
main()