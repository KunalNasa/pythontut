class Employee():
    no_of_leaves = 10
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, str):
        return cls(*str.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good " + string)

class Programmer(Employee):
    no_of_holidays = 30
    def __init__(self, aname, asalary, arole, lang):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lang = lang

    def printprog(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}.Known languages are{self.lang}"


harry = Employee("Harry", 150, "Instructor")
Ajay = Programmer("Ajay", 150, "Programmer", ["python", "java"])


karan = Employee.from_str("karan-150-Coach")
# print(karan.salary)
# print(karan.no_of_leaves)
# karan.printgood("work")
# Employee.printgood("work")
print(Ajay.no_of_holidays)
print(Ajay.printprog())
