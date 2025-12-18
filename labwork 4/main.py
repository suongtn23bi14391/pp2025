import input
import output

def main():
    students = input.input_students()
    courses = input.input_courses()
    
    input.input_marks(students, courses)
    for s in students:
        s.calculate_gpa(courses)
        
    output.display_students(students)

if __name__ == "__main__":
    main()