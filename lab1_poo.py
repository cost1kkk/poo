from enum import Enum
from datetime import date

class StudyField(Enum):
    MECHANICAL_ENGINEERING = "a"
    SOFTWARE_ENGINEERING = "b"
    FOOD_TECHNOLOGY = "c"
    URBANISM_ARCHITECTURE = "d"
    VETERINARY_MEDICINE = "e"

class Student:
    def __init__(self, firstname, lastname, dateofbirth, enrollmentdate, faculty):
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.enrollmentdate = enrollmentdate
        self.faculty = faculty

class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.study_field = study_field

def create_student(faculties):
    print("Available Faculties:")
    for i, faculty in enumerate(faculties, 1):
        print(f"{i}. {faculty.name} ({faculty.abbreviation})")

    faculty_choice = int(input("Choose a faculty (enter the corresponding number) or 0 to go back: "))
    if faculty_choice == 0:
        return

    selected_faculty = faculties[faculty_choice - 1]

    firstname = input("Enter student's first name: ")
    lastname = input("Enter student's last name: ")
    dateofbirth = input("Enter student's date of birth (YYYY-MM-DD): ")
    enrollmentdate = input("Enter enrollment date (YYYY-MM-DD): ")

    student = Student(firstname, lastname, dateofbirth, enrollmentdate, selected_faculty)
    selected_faculty.students.append(student)

    print(f"{student.firstname} {student.lastname} assigned to {selected_faculty.name}.")

def graduate_student(faculty):
    print(f"Students in {faculty.name}:")
    for i, student in enumerate(faculty.students, 1):
        print(f"{i}. {student.firstname} {student.lastname}")

    student_choice = int(input("Choose a student to graduate (enter the corresponding number) or 0 to go back: "))
    if student_choice == 0:
        return

    selected_student = faculty.students[student_choice - 1]
    faculty.students.remove(selected_student)

    print(f"{selected_student.firstname} {selected_student.lastname} graduated from {faculty.name}.")

def display_all_faculties(faculties):
    print("List of all faculties:")
    for faculty in faculties:
        print(f"{faculty.name} ({faculty.abbreviation}): {faculty.study_field.value}")

def display_all_students(faculties):
    print("List of all students:")
    for faculty in faculties:
        for student in faculty.students:
            print(f"{student.firstname} {student.lastname} - Faculty: {faculty.name}")

def check_student_in_faculty(faculty):
    student_name = input("Enter student's name (first name and last name): ")
    for student in faculty.students:
        if student_name.lower() == f"{student.firstname.lower()} {student.lastname.lower()}":
            print(f"{student.firstname} {student.lastname} belongs to {faculty.name}.")
            return

    print(f"No student with the name {student_name} found in {faculty.name}.")

def search_faculty_by_student_name(faculties):
    student_name = input("Enter student's name (first name and last name): ")
    for faculty in faculties:
        for student in faculty.students:
            if student_name.lower() == f"{student.firstname.lower()} {student.lastname.lower()}":
                print(f"{student.firstname} {student.lastname} belongs to {faculty.name}.")
                return

    print(f"No student with the name {student_name} found in any faculty.")

if __name__ == "__main__":
    faculties = []

    while True:
        print("\n-------- TUM Board Command Line --------")
        print("1. Faculty Operations")
        print("2. Student Operations")
        print("3. General Operations")
        print("4. Exit")

        operation_choice = input("Enter your choice (1/2/3/4): ")

        if operation_choice == "1":
            print("\n-------- Faculty Operations --------")
            print("1. Create a faculty")
            print("2. Graduate a student from a faculty")
            print("3. Display current enrolled students")
            print("4. Check if a student belongs to this faculty")
            print("0. Back")
            operation_choice = input("Enter operation choice (0/1/2/3/4): ")

            if operation_choice == "1":
                name = input("Enter faculty name: ")
                abbreviation = input("Enter faculty abbreviation: ")
                print("Choose a study field:")
                for field in StudyField:
                    print(f"{field.value}: {field.name}")
                field_choice = input("Enter the study field (a/b/c/d/e): ")
                study_field = next(field for field in StudyField if field.value == field_choice)
                faculty = Faculty(name, abbreviation, study_field)
                faculties.append(faculty)

            elif operation_choice == "2":
                print("Choose a faculty to graduate a student:")
                for i, faculty in enumerate(faculties, 1):
                    print(f"{i}. {faculty.name} ({faculty.abbreviation})")

                faculty_choice = int(input("Choose a faculty (enter the corresponding number): "))
                if faculty_choice == 0:
                    continue

                selected_faculty = faculties[faculty_choice - 1]
                graduate_student(selected_faculty)

            elif operation_choice == "3":
                print("Choose a faculty to display current enrolled students:")
                for i, faculty in enumerate(faculties, 1):
                    print(f"{i}. {faculty.name} ({faculty.abbreviation})")

                faculty_choice = int(input("Choose a faculty (enter the corresponding number): "))
                if faculty_choice == 0:
                    continue

                selected_faculty = faculties[faculty_choice - 1]
                print(f"Current enrolled students in {selected_faculty.name}:")
                for i, student in enumerate(selected_faculty.students, 1):
                    print(f"{i}. {student.firstname} {student.lastname}")

            elif operation_choice == "4":
                print("Choose a faculty to check if a student belongs to:")
                for i, faculty in enumerate(faculties, 1):
                    print(f"{i}. {faculty.name} ({faculty.abbreviation})")

                faculty_choice = int(input("Choose a faculty (enter the corresponding number): "))
                if faculty_choice == 0:
                    continue

                selected_faculty = faculties[faculty_choice - 1]
                check_student_in_faculty(selected_faculty)

            elif operation_choice == "0":
                continue

            else:
                print("Invalid choice. Please enter 0, 1, 2, 3, or 4.")

        elif operation_choice == "2":
            print("\n-------- Student Operations --------")
            create_student(faculties)

        elif operation_choice == "3":
            print("\n-------- General Operations --------")
            print("1. Display all faculties")
            print("2. Display all students")
            print("3. Search what faculty a student belongs to by a unique identifier")
            print("0. Back")
            operation_choice = input("Enter operation choice (0/1/2/3): ")

            if operation_choice == "1":
                display_all_faculties(faculties)
            elif operation_choice == "2":
                display_all_students(faculties)
            elif operation_choice == "3":
                search_faculty_by_student_name(faculties)
            elif operation_choice == "0":
                continue
            else:
                print("Invalid choice. Please enter 0, 1, 2, or 3.")

        elif operation_choice == "4":
            print("Exiting TUM Board Command Line. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
