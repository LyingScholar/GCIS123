import plotter
import csv
def plot_grades(infile,first_name,last_name):
    try:
        with open(infile) as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                    if line[1] == first_name and line[0]==last_name:
                        plotter.init("lab grade graph","Student","Scores")
                        plotter.new_series("Scores")
                        j = 2
                        while j<len(line):
                            plotter.add_data_point(float(line[j]))
                            j += 1
                        plotter.plot()
                        print("Plot finished (window may be hidden).")
                        return True
                    else:
                        continue
        print("Plot failed (no such student).")
        return False
    except:
        print("No such file: ", infile)
