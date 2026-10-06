# labwork1b.py - Student Mark Management System

def input_students():
    students = []
    n = int(input("Enter number of students in a class: "))
    for i in range(n):
        print(f"--- Enter info for student {i+1} ---")
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DoB (Day/Month/Year): ")
        students.append({"id": sid, "name": name, "dob": dob})
    return students

def input_courses():
    courses = []
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print(f"--- Enter info for course {i+1} ---")
        cid = input("Course ID: ")
        cname = input("Course Name: ")
        courses.append({"id": cid, "name": cname})
    return courses

def input_marks(students, courses):
    marks = {} # course_id -> {student_id: mark}
    if not courses or not students:
        print("Please input students and courses first!")
        return marks
    
    print("\nAvailable courses:")
    for c in courses:
        print(f"ID: {c['id']} - Name: {c['name']}")
    
    selected_cid = input("Select a course (Enter Course ID): ")
    course_found = any(c['id'] == selected_cid for c in courses)
    if not course_found:
        print("Course not found!")
        return marks
    
    marks[selected_cid] = {}
    print(f"Enter marks for course {selected_cid}:")
    for s in students:
        mark = float(input(f"Mark for student {s['name']} (ID: {s['id']}): "))
        marks[selected_cid][s['id']] = mark
        
    return marks

def list_courses(courses):
    print("\n--- List of Courses ---")
    if not courses:
        print("No courses available.")
        return
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def list_students(students):
    print("\n--- List of Students ---")
    if not students:
        print("No students available.")
        return
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def show_marks(courses, students, marks):
    print("\n--- Show Student Marks for a Given Course ---")
    if not courses:
        print("No courses available.")
        return
    
    for c in courses:
        print(f"ID: {c['id']} - Name: {c['name']}")
        
    selected_cid = input("Enter Course ID to view marks: ")
    if selected_cid not in marks:
        print("No marks recorded for this course yet.")
        return
    
    print(f"Marks for course {selected_cid}:")
    for s in students:
        sid = s['id']
        m = marks[selected_cid].get(sid, "N/A")
        print(f"Student: {s['name']} (ID: {sid}) - Mark: {m}")

def main():
    students = []
    courses = []
    marks = {}
    
    while True:
        print("\n=== STUDENT MARK MANAGEMENT SYSTEM ===")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            students = input_students()
        elif choice == '2':
            courses = input_courses()
        elif choice == '3':
            marks.update(input_marks(students, courses))
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            show_marks(courses, students, marks)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()