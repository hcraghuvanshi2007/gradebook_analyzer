# ===================================================================
# GradeBook Analyzer - Student Performance Analysis System
# Course: Programming for Problem Solving using Python
# Author: [Himanchal Raghuvanshi]
# Date: November 5, 2025
# Assignment : 02
# ===================================================================

def display_welcome():
    print("="*50)
    print("GRADEBOOK ANALYZER")
    print("="*50)

def display_menu():
    print("\n1. Input Student Data")
    print("2. View Statistics")
    print("3. View Grade Distribution")
    print("4. View Pass/Fail Summary")
    print("5. View Complete Results Table")
    print("6. Exit Program")

def input_student_data():
    marks = {}
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        name = input(f"Enter student {i+1} name: ")
        while name in marks or name.strip() == "":
            name = input("Duplicate or empty name, enter again: ")
        mark = int(input(f"Enter {name}'s marks (0-100): "))
        while mark < 0 or mark > 100:
            mark = int(input("Invalid marks, enter again (0-100): "))
        marks[name] = mark
    return marks

def calculate_average(marks):
    return sum(marks.values()) / len(marks) if marks else 0

def calculate_median(marks):
    vals = sorted(marks.values())
    n = len(vals)
    if n == 0:
        return 0
    if n % 2 == 1:
        return vals[n // 2]
    return (vals[n//2 - 1] + vals[n//2]) / 2

def find_max_score(marks):
    if not marks:
        return "", 0
    student = max(marks, key=marks.get)
    return student, marks[student]

def find_min_score(marks):
    if not marks:
        return "", 0
    student = min(marks, key=marks.get)
    return student, marks[student]

def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

def calculate_grades(marks):
    grades = {}
    for student in marks:
        grades[student] = assign_grade(marks[student])
    return grades

def display_statistics(marks):
    print("\nSTATISTICS")
    print("Students:", len(marks))
    print("Average:", round(calculate_average(marks),2))
    print("Median:", calculate_median(marks))
    max_student, max_score = find_max_score(marks)
    print("Highest:", max_score, "-", max_student)
    min_student, min_score = find_min_score(marks)
    print("Lowest:", min_score, "-", min_student)

def display_grade_distribution(marks):
    grades = calculate_grades(marks)
    grade_counts = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades.values():
        grade_counts[grade] += 1
    print("\nGRADE DISTRIBUTION")
    for grade in grade_counts:
        print(f"{grade}: {grade_counts[grade]}")

def filter_pass_fail(marks):
    passed = [name for name in marks if marks[name] >= 40]
    failed = [name for name in marks if marks[name] < 40]
    return passed, failed

def display_pass_fail_summary(marks):
    passed, failed = filter_pass_fail(marks)
    print("\nPass:", len(passed), "-", ", ".join(passed))
    print("Fail:", len(failed), "-", ", ".join(failed))

def display_results_table(marks):
    grades = calculate_grades(marks)
    print("\nRESULTS TABLE")
    print("Name        Marks   Grade")
    for name in sorted(marks):
        print(f"{name:10} {marks[name]:7} {grades[name]:5}")

def main():
    display_welcome()
    marks = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            marks = input_student_data()
        elif choice == '2':
            display_statistics(marks)
        elif choice == '3':
            display_grade_distribution(marks)
        elif choice == '4':
            display_pass_fail_summary(marks)
        elif choice == '5':
            display_results_table(marks)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


