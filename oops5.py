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
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))



# harry = Employee("Harry", 150, "Instructor")
# print(harry.salary)
karan = Employee.from_str("karan-150-Coach")
print(karan.salary)
print(karan.no_of_leaves)
# harry.change_leaves(0)
# print(harry.no_of_leaves)
