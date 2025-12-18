import math
import numpy as np

class Entity:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def getId(self): return self._id
    def getName(self): return self._name

class Student(Entity):
    def __init__(self, id, name, DoB):
        super().__init__(id, name)
        self.__DoB = DoB
        self.marks = {}  
        self.gpa = 0.0

    def calculate_gpa(self, courses_list):
        if not self.marks:
            return 0.0
        
        scores = []
        credits = []
        
        course_credits_map = {c.getId(): c.getCredits() for c in courses_list}
        
        for c_id, score in self.marks.items():
            if c_id in course_credits_map:
                scores.append(score)
                credits.append(course_credits_map[c_id])
        
        np_scores = np.array(scores)
        np_credits = np.array(credits)
        
        if np_credits.sum() == 0:
            self.gpa = 0.0
        else:
         
            self.gpa = np.sum(np_scores * np_credits) / np.sum(np_credits)
        return self.gpa

    def __str__(self):
        return f"Student ID: {self._id}, Name: {self._name}, DoB: {self.__DoB}, GPA: {self.gpa:.1f}"

class Course(Entity):
    def __init__(self, id, name, credits):
        super().__init__(id, name)
        self.__credits = credits
    def getCredits(self): return self.__credits
    def __str__(self):
        return f"Course ID: {self._id}, Name: {self._name}, Credits: {self.__credits}"

class CourseManager:
    def __init__(self, listCourses):
        self.__listCourses = listCourses

    def markStudentScore(self, listStudents):
        try:
            idCourse = int(input("Enter Course ID to mark: "))
            courseFound = next((c for c in self.__listCourses if c.getId() == idCourse), None)

            if courseFound:
                print(f"Marking for course: {courseFound.getName()}")
                for student in listStudents:
                    score = float(input(f"  Score for {student.getName()} (ID: {student.getId()}): "))
                
                    student.marks[idCourse] = math.floor(score * 10) / 10
            else:
                print("Course not found!")
        except ValueError:
            print("Invalid input! Please enter numbers.")

def createListStudent():
    listStudents = []
    n = int(input("Number of students: "))
    for i in range(n):
        sid = int(input(f"Student {i+1} ID: "))
        name = input("Name: ")
        dob = input("DoB: ")
        listStudents.append(Student(sid, name, dob))
    return listStudents

def createListCourses():
    listCourses = []
    n = int(input("Number of courses: "))
    for i in range(n):
        cid = int(input(f"Course {i+1} ID: "))
        name = input("Name: ")
        credits = int(input("Credits: "))
        listCourses.append(Course(cid, name, credits))
    return listCourses


if __name__ == "__main__":
 
    students = createListStudent()
    courses = createListCourses()
    manager = CourseManager(courses)

    print("\n Mark Entry")
    manager.markStudentScore(students)

    for s in students:
        s.calculate_gpa(courses)

    students.sort(key=lambda x: x.gpa, reverse=True)

    print("\nStudent List Sorted by GPA ")
    for s in students:
        print(s)