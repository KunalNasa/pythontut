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
#bina self ke ag kuch class me add krna ho to static method use krte hai
    @staticmethod
    def printgood(string):
        print("this is good " + string)

karan = Employee.from_str("karan-150-Coach")
# print(karan.salary)
# print(karan.no_of_leaves)
karan.printgood("work")
Employee.printgood("work")

#encapsulation - hide the implemnetation work. " Aam khaye, Ghutliya na gine "
