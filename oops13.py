class A():
    def met(self):
        return "This is from class A"
class B(A):
    def met(self):
        return "This is from class B"
class C(A):
    def met(self):
        return "This is from class C"
class D(B,C):
    def met(self):
        return "This is from class D"


a = A()
b = B()
c = C()
d = D()

print(d.met())