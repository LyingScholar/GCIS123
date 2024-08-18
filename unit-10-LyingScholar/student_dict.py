
def make_student(id, name):
    return [id, name, 0, 0]

def add_students(population, id, name):
    student_data = make_student(id,name)
    population[id] = student_data
    # for index in range(len(population)):
    #     if population[index][0] == id:
    #         population.pop(index)
    #         break     
    # population.append(make_student(id, name))

def get_student(popl, id):
    if id in popl:
        return popl[id]
    else:
        return
    # for student in popl:
    #     if student[0] == id:
    #         return student
    # return None

def add_credits(popl, id, credit):
    student = get_student(popl, id)
    if student != None:
        student[2] += credit

def get_credits(population, id):
    student = get_student(population, id)
    if student != None:
        return student[2]
    else:
        return None

def main():
    print("Student Information System")
    population = {}
    
    add_students(population, "ab1234", "Sam")
    # print(population)
    add_students(population, "gh3834", "Lacy")
    print(population["gh3834"])
    add_students(population, "gh3834", "Nick")
    
    print(population)

    
if __name__ == "__main__":
    main()

#dilkashi, uns, mohabbat, aqeedat, ibadat, junoon, maut