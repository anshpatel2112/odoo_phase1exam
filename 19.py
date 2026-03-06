import json

data = {
    "name": "Ansh",
    "age": 20,
    "course": "Computer Science"
}

with open("data.json", "w") as file:
    json.dump(data, file)

print("Dictionary converted to JSON and saved in file.")