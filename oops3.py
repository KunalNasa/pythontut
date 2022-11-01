# class Employee():
#     no_of_leaves = 10
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def printdetails(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
# harry = Employee("Harry", 150, "Instructor")
# print(harry.salary)

# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 150
# harry.role = "guide"
#
# rohan.name = "Rohan"
# rohan.salary = 150
# rohan.role = "tutor"

# print(rohan.printdetails())

class students():
    def __init__(self, aname, aclass, asection, arole, arollno):

        self.name = aname
        self.Class = aclass
        self.section = asection
        self.role = arole
        self.roll_number = arollno
    def printthis(self):
        return f"My name is {self.name} and I am in {self.Class} standard. My section is {self.section} , I am  {self.role} and " \
               f"my roll number is {self.roll_number}"

kannu = students("Kunal", 12, "A", "Monitor", 15)
print(kannu.printthis())
