class Employee():
    no_of_leaves = 10
    pass
harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 150
harry.role = "guide"

rohan.name = "Rohan"
rohan.salary = 150
rohan.role = "tutor"
print(harry.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 9 #can not change no of leaves of class
Employee.no_of_leaves = 9 #can change no of leaves of class
print(rohan.__dict__)
print(Employee.no_of_leaves)
