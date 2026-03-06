import json

student = {
    "name": "Ansh",
    "age": 20,
    "course": "Computer Science",
    "marks": 85 
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("Student data stored in JSON file.")