class Course:#TODO: add student and the mark
    def __init__(self, course_name: str, course_id: int, mark = []):
        self.validateCourse_name(course_name)
        self.validateCourse_id(course_id)
        
        self._course_name = course_name
        self._course_id = course_id
        self._course_mark = mark
        
    def setCourse_name(self, course_name):
        self.validateCourse_name(course_name)
        self._course_name = course_name
    def getCourse_name(self):
        return self._course_name
    def validateCourse_name(self, course_name: str):
        if not isinstance(course_name, str):
            raise TypeError("Type is not valid")
        elif len(course_name)<1:
            raise Exception("Sorry length of the cousre's name must be longer than 1")
            
    def setCourse_id(self, course_id):
        self.validateCourse_id(course_id)
        self._course_id = course_id
    def getCourse_id(self):
        return self._course_id
    def validateCourse_id(self, course_id):
        if not isinstance(course_id, int):
            raise TypeError("Type is not valid")
        elif course_id<0:
            raise Exception("Sorry course id cannot be negative")
            
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
            
    def addCourse(self):
        return self.__dict__

class MyClass(Course):
    
    def __init__(self, number_student: int, student: list):#auto update the value and the list in stu
        
        self.validateNumberStudent(number_student)
        
        self.age = number_student
        
    def setNumberStudent(self, number_student):
        self.validateNumberStudent(student_number)
        self.number_student = number_student
    def getNumberStudent():
        return self.number_student
        
    def validateNumberStudent(self, number_student: int):
        if not isinstance(number_student, int):
            raise TypeError("Type is not valid")
        elif number_student<0:
            raise Exception("Sorry number of student is not valid")
            
class Person:
    def __init__(self, name, DoB):
        self.validateName(name)
        self.validateDoB(DoB)
        
        self._name = name
        self._DoB = DoB
        
    def setName(self, name):
        self.validateName(name)
        self._name = name
    def getName(self):
        return self._name
    def validateName(self, name):
        if not isinstance(name, str):
            raise TypeError("Type of is not valid")
        elif len(name)<0 or len(name)>100:
            raise Exception("Name is not valid")
            
    def setDoB(self, DoB):
        self.validateDoB(DoB)
        self._DoB = DoB
    def getDoB(self):
        return self._DoB
    def validateDoB(self, DoB):
        if not isinstance(DoB, str):
            raise TypeError("Type is not valid")
        elif len(DoB)<0:
            raise Exception("DoB id is not valid")
    
class Student(Person):
    def __init__(self, name: str, student_id: int, DoB: str, course = []):
        super().__init__(name, DoB)
        self.validateStudentId(student_id)
        #self.validateCourse(course)
            
        self._student_id = student_id
        self._course = course
        
    def setName(self, name):
        super().validateName(name)
    def getName(self):
        super().getName()
    def validateName(self, name: str):
        super().validateName(name)
            
    def setStudent_id(self, student_id):
        self.validateStudent_id(student_id)
        self._student_id = student_id
    def getStudent_id(self):
        return this._student_id
    def validateStudentId(self, student_id: int):
        if not isinstance(student_id, int):
            raise TypeError("Type is not valid")
        elif student_id<0:
            raise Exception("Student id is not valid")
            
    def setDoB(self, DoB):
        super().setDoB(DoB)
    def getDoB(self):
        super().getDoB()
    def validateDoB(self, DoB: str):
        super().validateDoB(DoB)
            
    def addCourse(self, course):#TODO:
        self._course.append(course)
    def getCourse(self):
        return self._course
    def validateCourse(self, course: list):
        if not isinstance(course, list):
            raise TypeError("Type is not valid")
        elif DoB<0:
            raise Exception("Course id is not valid")
    
    def getStudent(self):
        return self.__dict__
        


class_student = {
    "number" : 0,
    "students" : []
}

course = {
    "number" : 0,
    "courses" : []
}

def student_info():#done
    student_id = int(input("Enter student's id: "))
    name = input("Enter student name: ")
    date_of_birth = input("Enter student's DoB: ")
    stu = Student(name, student_id, date_of_birth, [])
    return stu
    
def student_list():#done
    print("\nWe have the list of students: ")
    for student in class_student["students"]:
        print("ID: "+str(student["_student_id"])+ "\nName: "+student["_name"]+ "\nDoB: "+student["_DoB"]+ "\nCourse: "+str(student["_course"])+"\n")

def class_number_students():#done
    student_number = int(input("How many student?\n- ")) 
    class_student["number"] = student_number
    for i in range(student_number):
        class_student["students"].append(student_info().getStudent())

def list_course():#done
    course_number = int(input("Enter number of course: "))
    course["number"] = course_number
    for i in range(course_number):
        course_name = input("Enter course name: ")
        course_id = int(input("Enter course id: "))
        x = Course(course_name, course_id)
        course["courses"].append(x.addCourse())

def course_list():#done
    for cour in course["courses"]:
        print("ID: " +str(cour["_course_id"])+ " --- Name: " +cour["_course_name"])
        print(cour["_course_mark"])
        
def course_mark():#TODO
    print("\nWe have courses: ")
    course_list()
    course_id = int(input("\nPlease enter course's id to enter mark: "))
    student_name = input("Please enter student's name: ")
    mark = int(input("Please enter student's mark: "))
    course_name = ""
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            course_name = cour["_course_name"]
            cour["_course_mark"].append([student_name, mark])#????????
    for student in class_student["students"]:
        if student["_name"] == student_name:
            student["_course"].append([course_name, mark])

def show_mark():#TODO
    course_id = int(input("Please enter course id to see the marks: "))
    for cour in course["courses"]:
        if cour["_course_id"] == course_id:
            for i in range(2,len(cour)):
                print(cour["_course_mark"])
                

class_number_students()
student_list()

list_course()
course_mark()
show_mark()
