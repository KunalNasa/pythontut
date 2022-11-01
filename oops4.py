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


harry = Employee("Harry", 150, "Instructor")
print(harry.salary)
Employee.change_leaves(10)
# harry.change_leaves(0)
print(harry.no_of_leaves)
