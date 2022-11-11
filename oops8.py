class Employee():
    no_of_leaves = 10
    var = 8
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
    var = 9
    no_of_holidays = 30
    def __init__(self, aname, asalary, arole, lang):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lang = lang

    def printprog(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}.Known languages are{self.lang}"

class Player():
    no_of_games = 4
    var = 10
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printplay(self):
        f"The name of the player is {self.name} and he/she plays {self.game}"

class Coolprogrammer(Employee, Player): #order of employee and player is important

    language = "C++"
    def printlang(self):
        print(self.language)



harry = Employee("Harry", 150, "Instructor")
Ajay = Programmer("Ajay", 150, "Programmer", ["python", "java"])

aman = Player("Aman", ["basketball", "chess"])
karan = Coolprogrammer("Karan", 150, "Coolprogrammer")
# karan.printlang()
print(karan.var)
