students = {}

def create_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    students[roll] = name
    print("Student added successfully")

def read_students():
    print("Student List:")
    for roll, name in students.items():
        print("Roll:", roll, "Name:", name)

def update_student():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        name = input("Enter new name: ")
        students[roll] = name
        print("Student updated")
    else:
        print("Student not found")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted")
    else:
        print("Student not found")


while True:
    print("\n1.Create  2.Read  3.Update  4.Delete  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")