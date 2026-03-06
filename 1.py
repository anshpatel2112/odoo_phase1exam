employees = {
    "emp1": {"name": "ansh", "role": "Developer", "salary": 35000},
    "emp2": {"name": "rishit", "role": "Designer", "salary": 28000},
    "emp3": {"name": "rita mam", "role": "Manager", "salary": 45000},
    "emp4" : {"name": "ram", "role":"functional", "salary": 20000}
}

for emp in employees.values():
    if emp["salary"] > 30000:
        print(emp["name"])