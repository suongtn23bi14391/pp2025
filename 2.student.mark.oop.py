# Class list
# Student : id, name, DoB
# Course : id, name and listStudent
# listCourses : course


from numpy import integer, number
class Entity():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
def getId(self):
        return self.__id
def setId(self, id):
        self.__id = id
def getName(self):
        return self.__name
def setName(self, name):
        self.__name = name
class Student(Entity):
    def __init__(self, id, name, DoB):
        super().__init__(id, name)
        self.__DoB = DoB

    def __str__(self):
        return f"Student id = {super().getId()}, name = {super().getName()}, DoB = {self.__DoB}"
# ListStudent will be a List
class Course(Entity):
    def __init__(self, id, name, listStudents):
        super().__init__(id, name)
        self.__listStudent = listStudents
def getListStudents(self):
        return self.__listStudent
def __str__(self):
        return f"Course id = {super().getId()}, name = {super().getName()}, listStudent"
# ListCourse is a dictionary with key = course id and value = course itself
class CourseManager():  # listCourse
    def __init__(self, numberOfCourses, listCourses):
        self.__numberOfCourses = numberOfCourses
        self.__listCourses = listCourses

    def markStudentScoreWithCourseId(self):
        listStudentMark = []
        courseFound = None

        idCourse = int(input("Course ID: "))

        for course in self.__listCourses:
            print(course)
            if course.getId() == idCourse:
                courseFound = course
                break

        if courseFound is not None:
            print(f"The course is {courseFound.getName()}")

            for student in courseFound.getListStudents():
                numberScore = float(
                    input(f"The mark for student {student.getId()} is: ")
                )
                listStudentMark.append(
                    f"Student {student.getId()} mark is {numberScore}"
                )
        else:
            print(f"Cannot find the course with id = {idCourse}")

        return listStudentMark

    def __str__(self):
        return f"Course Manager"


def createListStudent():
    listStudents = []
    numberStudents = int(input("Number of students: "))
    for student in range(numberStudents):
        idStudent = int(input(f"Student {student + 1} ID: "))
        nameStudent = input("Student name: ")
        DoBStudent = input("Student DoB: ")
        listStudents.append(Student(idStudent, nameStudent, DoBStudent))
        print("\n")
    return listStudents


def printListStudent(listStudents):
    for student in listStudents:
        print(student)


def createListCourses(listStudents):
    listCourses = []
    numberCourses = int(input("Number of courses: "))
    for course in range(numberCourses):
        idCourse = int(input(f"Course {course + 1} ID: "))
        nameCourse = input("Course name: ")
        print("\n")

        listCourses.append(Course(idCourse, nameCourse, listStudents))
    return listCourses


def printListCourses(listCourses):
    for course in listCourses:
        print(course)


def printListStudentMark(listStudentMark):
    for score in listStudentMark:
        print(score)
listStudents = createListStudent()
printListStudent(listStudents)
print("\nCreate course list")
listCourses = createListCourses(listStudents)
printListCourses(listCourses)
courseManager = CourseManager(len(listCourses), listCourses)
print("\nMark student scores by course ID")
listStudentMark = courseManager.markStudentScoreWithCourseId()
printListStudentMark(listStudentMark)
