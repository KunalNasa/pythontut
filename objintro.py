class Employee():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"

        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self, str):
        print("setting now")
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

kannu = Employee("Kannu", "Nasa")
print(kannu.email)
# print(type(kannu))
# print(id("this is a string"))
o = "this is a string"
print(dir(kannu))

#  objet intro - type, id, dir

import inspect
print(inspect.getmembers(kannu))