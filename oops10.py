# public - Ghar ke bahar poster lagado
# protected - Ghar ke andar poster lagado
# private - Sirf apne kamre ke andar poster lagado

class Employee():
    no_of_leaves = 10  #public
    var = 8
    _protect = 9 #protected, (underscore is used before to make variable protective)
    __private = 5 #Private, (doubleunderscore is used before to make variable private)
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp = Employee("Ajay", 150, "teacher")
print(emp._Employee__private) #to print private file
