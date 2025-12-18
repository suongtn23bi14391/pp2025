import math
from domains.student import Student
from domains.course import Course

def input_students():
    students = []
    n = int(input("Number of students: "))
    for _ in range(n):
        sid = int(input("ID: "))
        name = input("Name: ")
        dob = input("DoB: ")
        students.append(Student(sid, name, dob))
    return students

def input_courses():
    courses = []
    n = int(input("Number of courses: "))
    for _ in range(n):
        cid = int(input("Course ID: "))
        name = input("Course Name: ")
        cre = int(input("Credits: "))
        courses.append(Course(cid, name, cre))
    return courses

def input_marks(students, courses):
    c_id = int(input("Enter Course ID to mark: "))
    for s in students:
        score = float(input(f"Score for {s.getName()}: "))
        s.marks[c_id] = math.floor(score * 10) / 10