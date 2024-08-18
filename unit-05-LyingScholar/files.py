import plotter
import csv
def print_lines(filename):
    file = open(filename)

    for line in file:
        print(line, end="")

def print_lines_b(filename):
    file = open(filename)

    for line in file:
        print(line.strip())
    file.close()
    
def print_autoclose(filename):
    with open(filename) as file:
        for line in file:
            print(line.strip())
            
def word_search(filename):
    word = input("Enter word :")
    line_no = 0
    file = open(filename)
    for line in file:
        line_no += 1
        if word.strip().lower() == line.strip().lower():
            print("Found", line_no)
            return
    print("not found")

def print_name(filename):
    with open(filename) as file:
        next(file)
        next(file)
        for line in file:
            words = line.split(",")
            print(words[1],words[0])
    print()
        
def longest_word(filename):
    final_word = ""
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(final_word):
                    final_word = word
    print("final word -- ",final_word)  

def plot_graph():
    plotter.init("First Graph", "X-Axis","Y-Axis")
    plotter.new_series("First series")
    plotter.add_data_point(10)
    plotter.add_data_point(100)
    plotter.add_data_point(50)
    plotter.new_series("Second series")
    plotter.add_data_point(40)
    plotter.add_data_point(90)
    plotter.add_data_point(10)
    plotter.plot()

def student_data(filename,columnnbr):
    plotter.init("lab grade graph", "Studnet","Grade")
    
    with open(filename) as file:
        header = next(file).split(",")[columnnbr]
        plotter.new_series(header)
        for line in file:
            words = line.split(",")
            plotter.add_data_point(int(float(words[columnnbr])))
    plotter.plot()
    
def print_name_address(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            # words = line.split()
            print(line[0],line[1])
    print()
       
def main():
    # try:
    #     ask_password()
    # except:
    #     print("Main error")
    
    # print_name_address("full_grades_010.csv")
    
    plot_graph()
    # student_data("data/grades_010.csv", 5)
    # print_name(
    # print_autoclose("data/words.txt")

if __name__ == "__main__":
    main()