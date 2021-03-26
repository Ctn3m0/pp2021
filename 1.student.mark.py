classt = {
    "number" : 0,
    "students" : []
}

course = {
    "number" : 0,
    "courses" : []
}

def sinfo():
    si = int(input("Enter student id: "))
    n = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    st = {
        "id" : si,
        "name" : n,
        "DoB" : dob,
        "courses": [],
    }
    return st

def slist():
    print("\nWe have the list of students: ")
    for i in classt["students"]:
        print(f'ID: {i["id"]} \nName: {i["name"]} \nDoB: {i["DoB"]} \nCourse: {i["courses"]}\n')

def cnumber_students():
    s = int(input("How many student?\n- ")) 
    classt["number"] = s
    for i in range(s):
        classt["students"].append(sinfo())

def list_course():
    n = int(input("Enter number of course: "))
    course["number"] = n
    for i in range(n):
        x = input("Enter course name: ")
        y = int(input("Enter course id: "))
        course["courses"].append([x,y])

def clist():
    for i in course["courses"]:
        print(f'ID: {i[1]} --- Name: {i[0]}')
        
def cmark():
    print("\nWe have courses: ")
    clist()
    ind = int(input("\nPlease choose the course id to enter mark: "))
    std = input("Please enter student name: ")
    m = int(input("Please enter student's mark: "))
    n = ""
    for i in course["courses"]:
        if i[1] == ind:
            n = i[0]
            i.append([std, m])
    for i in classt["students"]:
        if i["name"] == std:
            i["courses"].append([n, m])

def show_m():
    ind = int(input("Please enter course id to see the marks: "))
    for i in course["courses"]:
        if i[1] == ind:
            for x in range(2,len(i)):
                print(i[x])
cnumber_students()
slist()
list_course()

cmark()
slist()

show_m()
