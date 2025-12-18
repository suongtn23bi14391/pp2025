def display_students(students):
    students.sort(key=lambda x: x.gpa, reverse=True)
    print("\n--- Student List (Sorted by GPA) ---")
    for s in students:
        print(f"ID: {s.getId()} | Name: {s.getName()} | GPA: {s.gpa:.1f}")

def display_courses(courses):
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c.getId()} | Name: {c.getName()} | Credits: {c.getCredits()}")