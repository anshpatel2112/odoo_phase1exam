class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def object_count(cls):
        print("Number of objects created:", cls.count)

e1 = Employee("virat")
e2 = Employee("rohit")
e3 = Employee("Anshuuu")
e4 = Employee("ansh")

Employee.object_count()