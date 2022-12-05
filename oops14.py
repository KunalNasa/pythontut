class Employee():
    no_of_leaves = 10
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#self ko bina change kiye class ko change krdeta hai👇.
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


    def __add__(self, other):  #special method known as dunder add method
        return self.salary + other.salary

    def __truediv__(self, other):  #special method known as dunder div method
        return self.salary / other.salary

    def __floordiv__(self, other):  #special method known as dunder div method
        return self.salary // other.salary

    def __repr__(self):  #this will be returned when we print(emp1)
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self): #while printing emp1 this will be preffered before repr method.(if method is not mentioned)
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"



emp1 = Employee("Harry", 150, "Instructor")
emp2 = Employee("Rohan", 150, "Programmer")
# print(emp1 + emp2)
# print(emp1 / emp2)
# print(emp1 // emp2)
print(emp1)
print(repr(emp1))
