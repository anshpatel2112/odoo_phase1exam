import csv

students = [
    ["Name", "Age", "Course"],
    ["Ansh", 20, "Computer Science"],
    ["Rahul", 21, "IT"],
    ["Priya", 19, "Electronics"]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Data exported to CSV file successfully.")