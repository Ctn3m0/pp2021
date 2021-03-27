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
