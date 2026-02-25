students = {}
courses = {}
enrollments = {}

COURSE_LIMIT = 3

# ---------------- ADD STUDENT ----------------
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    sec = input("Enter Section: ")

    students[sid] = {
        "name": name,
        "roll": roll,
        "section": sec
    }
    print("Student added successfully!\n")

# ---------------- ADD COURSE ----------------
def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")

    courses[cid] = cname
    print("Course added successfully!\n")

# ---------------- ENROLL STUDENT ----------------
def enroll_student():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    if sid not in students or cid not in courses:
        print("Invalid Student or Course ID\n")
        return

    count = 0
    for key in enrollments:
        if key[0] == sid:
            count += 1

    if count >= COURSE_LIMIT:
        print("Course limit exceeded!\n")
        return

    enrollments[(sid, cid)] = {
        "attendance": 0,
        "grade": None
    }
    print("Student enrolled successfully!\n")

# ---------------- MARK ATTENDANCE ----------------
def mark_attendance():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    key = (sid, cid)
    if key not in enrollments:
        print("Enrollment not found\n")
        return

    att = float(input("Enter Attendance %: "))
    enrollments[key]["attendance"] = att

    if att < 75:
        print("⚠ Defaulter: Attendance below 75%\n")
    else:
        print("Attendance updated\n")

# ---------------- ASSIGN GRADE ----------------
def assign_grade():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    key = (sid, cid)
    if key not in enrollments:
        print("Enrollment not found\n")
        return

    grade = input("Enter Grade: ")
    enrollments[key]["grade"] = grade
    print("Grade assigned successfully!\n")

# ---------------- STUDENT REPORT ----------------
def student_report():
    sid = input("Enter Student ID: ")

    if sid not in students:
        print("Student not found\n")
        return

    print("\n--- Student Report ---")
    print(students[sid])

    for (s, c), data in enrollments.items():
        if s == sid:
            print("Course:", courses[c],
                  "| Attendance:", data["attendance"],
                  "| Grade:", data["grade"])
    print()

# ---------------- COURSE WISE REPORT ----------------
def course_report():
    cid = input("Enter Course ID: ")

    if cid not in courses:
        print("Course not found\n")
        return

    print("\n--- Course Wise Report ---")
    print("Course:", courses[cid])

    for (s, c), data in enrollments.items():
        if c == cid:
            print("Student:", students[s]["name"],
                  "| Attendance:", data["attendance"],
                  "| Grade:", data["grade"])
    print()

# ---------------- MAIN MENU ----------------
while True:
    print("""
1. Add Student
2. Add Course
3. Enroll Student
4. Mark Attendance
5. Assign Grade
6. View Student Report
7. Course Wise Report
8. Exit
""")

    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        add_course()
    elif ch == "3":
        enroll_student()
    elif ch == "4":
        mark_attendance()
    elif ch == "5":
        assign_grade()
    elif ch == "6":
        student_report()
    elif ch == "7":
        course_report()
    elif ch == "8":
        print("Thank You!")
        break
    else:
        print("Invalid choice\n")
