def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_details(name="Rahul", role="Developer", salary=40000)