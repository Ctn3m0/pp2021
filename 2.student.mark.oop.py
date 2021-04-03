class MyClass(Course):
    
    def __init__(self, number_student: int, student: list):
        
        validateNumberStudent(number_student)
        
        self.age = number_student
        
    def setNumberStudent(self, number_student):
        if !validateNumberStudent(number_student):
            print("Number of student is not valid")
            return False
        else:
            self.number_student = number_student
            return True
        
    def addStudent(self):#TODO: how to connect this with my previous function
        
        
    def validateNumberStudent(self, number_student: int):
        if not isinstance(number_student, int):
            raise TypeError("Type is not valid")
        elif number_student<0:
            raise Exception("Sorry number of student is not valid")
            

class Course:
    def __init__(self, course_name: str, course_id: int):
        validateCourse_name(course_name)
        validateCourse_id(course_id)
        
        this._course_name = course_name
        this._course_id = course_id
    def setCourse_name(self, course_name):
        validate(course_name)
        this._course_name = course_name
    def getCourse_name(self):
        return this.course_name
    def validateCourse_name(self, course_name: str):
        if not isinstance(course_name, str):
            raise TypeError("Type is not valid")
        elif len(course_name)<1:
            raise Exception("Sorry length of the cousre's name must be longer than 1")
            
    def setCourse_id(self, course_id):
        validate(course_id)
        this._course_id = course_id
    def getCourse_id(self):
        return this._course_id
    def validateCourse_id(self, course_id):
        if not isinstance(course_id, int):
            raise TypeError("Type is not valid")
        elif course_id<0:
            raise Exception("Sorry course id cannot be negative")

class Person:
    def __init__(self, name, DoB):
        validateName(name)
        validateDoB(DoB)
        
        this._name = name
        this._DoB = DoB
        
    def setName(self, name):
        validateName(name)
        this._name = name
    def getName(self):
        return this._name
    def validateName(self):
        if not isinstance(name, str):
            raise TypeError("Type of is not valid")
        elif len(name)<0 || len(name)>100:
            raise Exception("Name is not valid")
            
    def setDoB(self, DoB):
        validateDoB(DoB)
        this._DoB = DoB
    def getDoB(self):
        return this._DoB
    def validateDoB(self):
        if not isinstance(DoB, str):
            raise TypeError("Type is not valid")
        elif DoB<0:
            raise Exception("DoB id is not valid")
    
        
class Student(Person):
    def __init__(self, name: str, student_id: int, DoB: str, course: list):
        super().__init__(name, DoB)
        validateStudentId(student_id)
        validate(course)
            
        this._student_id = student_id
        this._course = course
        
    def setName(self, name):
        super().validateName(name)
    def getName(self):
        super().getName()
    def validateName(self, name: str):
        super().validateName(name)
            
    def setStudent_id(self, student_id):
        validate(student_id)
        this._student_id = student_id
    def getStudent_id(self):
        return this._student_id
    def validateStudent_id(self, student_id: int):
        if not isinstance(student_id, int):
            raise TypeError("Type is not valid")
        elif student_id<0:
            raise Exception("Student id is not valid")
            
    def setDoB(self):#TODO: as the below
    def getDoB(self):
    def validateDoB(self, DoB: str):
        super().validateDoB(DoB)
            
    def addCourse(self):#TODO: Can I use the previous one?
    def getCourse(self):
    def validateCourse(self, course: list):
        if not isinstance(course, list):
            raise TypeError("Type is not valid")
        elif DoB<0:
            raise Exception("Course id is not valid")
        
#st
courses = []
Class = []
student = []

class_student = {
    "number" : 0,
    "students" : []
}

course = {
    "number" : 0,
    "courses" : []
}

def student_info():
    student_id = int(input("Enter student's id: "))
    name = input("Enter student name: ")
    date_of_birth = input("Enter student's DoB: ")
    student = {
        "id" : student_id,
        "name" : name,
        "DoB" : date_of_birth,
        "courses": [],
    }
    return student

def student_list():
    print("\nWe have the list of students: ")
    for student in class_student["students"]:
        print(f'ID: {student["id"]} \nName: {student["name"]} \nDoB: {student["DoB"]} \nCourse: {student["courses"]}\n')

def class_number_students():
    student_number = int(input("How many student?\n- ")) 
    class_student["number"] = student_number
    for i in range(student_number):
        class_student["students"].append(student_info())

def list_course():
    course_number = int(input("Enter number of course: "))
    course["number"] = course_number
    for i in range(course_number):
        course_name = input("Enter course name: ")
        course_id = int(input("Enter course id: "))
        course["courses"].append([course_name,course_id])

def course_list():
    for cour in course["courses"]:
        print(f'ID: {cour[1]} --- Name: {cour[0]}')
        
def course_mark():
    print("\nWe have courses: ")
    course_list()
    course_id = int(input("\nPlease enter course's id to enter mark: "))
    student_name = input("Please enter student's name: ")
    mark = int(input("Please enter student's mark: "))
    course_name = ""
    for cour in course["courses"]:
        if cour[1] == course_id:
            course_name = cour[0]
            cour.append([student_name, mark])
    for student in class_student["students"]:
        if student["name"] == student_name:
            student["courses"].append([course_name, mark])

def show_mark():
    course_id = int(input("Please enter course id to see the marks: "))
    for cour in course["courses"]:
        if cour[1] == course_id:
            for i in range(2,len(cour)):
                print(cour[i])
                
class_number_students()
student_list()
list_course()
course_mark()
show_mark()

