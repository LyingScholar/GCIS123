import plotter
import csv
import re

def plot_grades(file_name,first_name,last_name):

    with open(file_name) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        name = last_name +", "+ first_name
        plotter.init("lab grade graph","Student","Scores")
        plotter.new_series(first_name + last_name)
        for line in csv_reader:
            if line[0] == name: 
                j = 2
                while j<len(line):
                    plotter.add_data_point(float(line[j]))
                    j += 1
        plotter.plot()
        print("Plot finished (window may be hidden).")
        return True

def get_average(file_name,column):
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        total = 0
        list = 0
        for line in csv_reader:
            try:
                total += float(line[(column)])
                list += 1
            except:
                list += 1
        return total/list

def plot_class_average(file_name):
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        plotter.init("lab grade graph","Student","Scores")
        plotter.new_series("avg")
        j = 3
        for line in csv_reader:
             while j<len(line):
               plotter.add_data_point(get_average(file_name,j))
               j += 1
        plotter.plot()
        print("Plot finished (window may be hidden).")
        return True
    
def main():
    plot_grades("data/full_grades_100.csv", "Christena", "Lott")
    
    plot_grades("data/full_grades_100.csv", "Hanna", "Knippers")
    plot_class_average("data/full_grades_999.csv")
    
if __name__ == "__main__":
    main()
