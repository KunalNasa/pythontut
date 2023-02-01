# x = input("enter your name")
# y = int(input ("how much do you earn"))
#
# if int(y) == 0:
#     raise ZeroDivisionError("y is zero so stopping the programme")
#
# if x.isnumeric():
#     raise Exception("numbers are not allowed")
# #1000 lines of code taking one hour
# print(f"Hello {x}")


#Python has built in errors. e.g Memory error, assertion error

# c = input("enter your name")
# try:
#     print(a)
# except Exception as e:
#     if c == "Kannu":
#         raise ValueError("you have entered blocked name")
#     print("Exception Handled")

a = int(input("enter a number"))
try:
    print(10/a)
except:
    if a == 0:
        raise ZeroDivisionError("division is not possible")
else:
    print("successful")