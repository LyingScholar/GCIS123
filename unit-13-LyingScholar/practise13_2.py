import csv
import random


def street_print(filename):
    street_names = {}
    with open(filename) as file:
        reader = csv.reader(file)
        
        next(reader)

        for row in reader:
            street_name = row[0].split(',')[0].strip().upper()  
            street_type = row[1].strip().upper() if row[1].strip() else None

            if street_type:
                if street_type in street_names:
                    street_names[street_type].add(street_name)
                else:
                    street_names[street_type] = {street_name}
    return street_names

class Exam:
    __slots__ = ["__stdnt_name", "__ttl_points", "__ernd_points"]

    def __init__(self, stdnt_name, ttl_points):
        self.__stdnt_name = stdnt_name
        self.__ttl_points = ttl_points
        self.__ernd_points = 0

    def get_name(self):
        return self.__stdnt_name

    def get_ttl(self):
        return self.__ttl_points

    def get_ernd(self):
        return self.__ernd_points

    def set_ernd(self, points):
        if points > self.__ttl_points:
            self.__ernd_points = self.__ttl_points
        else:
            self.__ernd_points = points

    def ratio(self):
        return (self.__ernd_points / self.__ttl_points) * 100 if self.__ttl_points != 0 else 0

    def __repr__(self):
        return self.__stdnt_name + str(int(self.ratio()))

    def __eq__(self, other):
        return self.__stdnt_name == other.__stdnt_name

    def __lt__(self, other):
        if self.ratio() == other.ratio():
            return self.__stdnt_name < other.__stdnt_name
        return self.ratio() < other.ratio()

def exam_writing(num_stdnts, ttl_points):
    exams = []
    completed_exams = []

    print("Administering  exams:")
    for i in range(num_stdnts):
        stdnt_name = "student " + str(i+1)
        exam = Exam(stdnt_name, ttl_points)
        exam.set_ernd(random.randint(0, ttl_points))
        exams.append(exam)
        print("  Completed:", exam)

    print("\nGrading exams:")
    while exams:
        exam = exams.pop()
        completed_exams.append(exam)
        print("  Graded:", exam)

    print("\nEntering grades into grade database:")
    for exam in completed_exams[::-1]:
        print("  Entered:", exam)

    sorted_grades = sorted(completed_exams, reverse=True)
    print("\nSorted grades:")
    for exam in sorted_grades:
        print(" ", exam)


def main():
    file_name = './unit-13-LyingScholar/data/streets.csv'
    street_names_data = street_print(file_name)


    # How many of the streets are a drive (DR)?
    
    
    if 'DR' in street_names_data:
        print("There are", len(street_names_data["DR"]),  "street_names that are DR.")
    else:
        print("There are no drive streets.")

    # Is there a RED LEAF lane (LN)?
    if 'LN' in street_names_data and 'RED LEAF' in street_names_data["LN"]:
        print("RED LEAF lane.")
    else:
        print("No RED LEAF lane.")

    # listing of all street types for the street name VISTA
    if 'VISTA' in street_names_data:
        print("Street types for VISTA: ")
        print(street_names_data['VISTA'])
    else:
        print("No streets named VISTA.")


    exam_writing(30, 100)
main()