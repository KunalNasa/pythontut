class A():
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am in class A"
        self.classvar1 = "Instance var in class A"
        self.special = "special"

class B(A):
    classvar1 = "I am a class variable in class B"
    def __init__(self):
        super().__init__() #refers to main parent class
        self.var1 = "I am in class B"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)

a = A()
b = B()

# print(b.classvar1) # sabse phle instance variable ko dhundega or usko hi print krega, na ki class var ko
print(b.special, b.var1, b.classvar1)