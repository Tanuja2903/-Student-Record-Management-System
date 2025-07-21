#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2

student_records = []

def accept():
    num_entries = int(input("Enter the number of student records you want to add: "))
    
    for i in range(num_entries):
        print(f"\nStudent #{i + 1}")
        name = input("Enter student name: ")
        rollno = input("Enter roll number: ")
        marks1 = float(input("Enter marks for subject 1: "))
        marks2 = float(input("Enter marks for subject 2: "))
        student = Student(name, rollno, marks1, marks2)
        student_records.append(student)
    
    print(f"\n{num_entries} student record(s) added successfully.")

def display_all_students():
    if not student_records:
        print("No student records found.")
    else:
        print("Student records:")
        for student in student_records:
            print(f"Name: {student.name}")
            print(f"Roll No: {student.rollno}")
            print(f"Marks 1: {student.marks1}")
            print(f"Marks 2: {student.marks2}")
            print()

def search_student(rollno):
    for student in student_records:
        if student.rollno == rollno:
            print("Student found.")
            print(f"Name: {student.name}")
            print(f"Roll No: {student.rollno}")
            print(f"Marks 1: {student.marks1}")
            print(f"Marks 2: {student.marks2}")
            return
    print("Student with roll number", rollno, "not found.")

def delete_student(rollno):
    for student in student_records:
        if student.rollno == rollno:
            student_records.remove(student)
            print("Student with roll number", rollno, "deleted successfully.")
            return
    print("Student with roll number", rollno, "not found.")

def update_student(rollno):
    for student in student_records:
        if student.rollno == rollno:
            print("Enter updated student details:")
            name = input("Name: ")
            marks1 = float(input("Marks 1: "))
            marks2 = float(input("Marks 2: "))
            student.name = name
            student.marks1 = marks1
            student.marks2 = marks2
            print("Student with roll number", rollno, "updated successfully.")
            return
    print("Student with roll number", rollno, "not found.")

# Menu function
def menu():
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

# Main program
while True:
    menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        accept()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        rollno = input("Enter roll number to search: ")
        search_student(rollno)
    elif choice == "4":
        rollno = input("Enter roll number to delete: ")
        delete_student(rollno)
    elif choice == "5":
        rollno = input("Enter roll number to update: ")
        update_student(rollno)
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")


# In[ ]:





# In[ ]:




