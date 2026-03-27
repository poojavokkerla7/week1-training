students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully")

def view_students():
    if not students:
        print("No students found")
    else:
        for i, student in enumerate(students):
            print(i + 1, student)

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        students.remove(name)
        print("Student deleted")
    else:
        print("Student not found")

def search_student():
    name = input("Enter name to search: ")
    if name in students:
        print("Student found")
    else:
        print("Student not found")

while True:
    print("\n1.Add 2.View 3.Delete 4.Search 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice"
