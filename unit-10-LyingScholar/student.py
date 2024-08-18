class student:
    # id = "No id"
    # name = ""
    # credit = 0
    # gpa = 0
    # courses = ['math','python']
    __slots__ = ["id","name","credit","gpa", "courses"]
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credit = 0
        self.gpa = 0
        self.courses = ['math','python']
        print("constructor")

def print_student(student):
    print("student -->", student.id, student.name, student.credit, student.gpa, student.courses)
    
    
def main():
    student1 = student("ab1234","Sam")
    # student1.crdit = 2.0
    student1.credit = 0
    student1.gpa = 0
    student1.courses[0] = "English"
    student2 = student("xyz1234","Lucy")
    # student1.id = "ab1234"
    # student1.name = "Sam"
    # student1.credit = 0
    # student1.gpa = 0
    print_student(student1)
    print_student(student2)

if __name__ == "__main__":
    main()