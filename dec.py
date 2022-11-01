# def function1():
#     print("hello")
# func2 = function1
# del function1
# func2()

# def func_return(n):
#     if n==0:
#         return print
#     if n==1:
#         return sum
# a = func_return(0)
# print(a)

# def executer(func):
#     func("this")
# executer(print)


def dec1(func1):
    def exec():
        print("hello moto")
        func1()
        print("executed")
    return exec()
@dec1
def whoiskannu():
    print("kannu is kannu")
# whoiskannu = dec1(whoiskannu)



# def div(a,b):
#     # if a<b:
#     #     a,b = b,a
#     print(a/b)
#
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner
# div = smart_div(div)
# div(2,4)

def sub(a,b):
    print(a-b)

def smartsub(func):
    def exc(a,b):
        a,b = b,a
        return func(a,b)
    return exc
sub = smartsub(sub)
sub(3,2)
