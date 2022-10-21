# import datetime
#
#
# def gettime():
#     return datetime.datetime.now()
#
#
# def take(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("harry-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif (k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif (k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
#
#
# def retrieve(k):
#     if k == 1:
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif (k == 2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif (k == 3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("plz enter valid input (harry,rohan,hammad)")
#
#
# print("health management system: ")
# a = int(input("Press 1 for log the value and 2 for retrieve "))
#
# if a == 1:
#     b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
#     take(b)
# else:
#     b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
#     retrieve(b)

import datetime

def gettime():
    return datetime.datetime.now()

c= int(input("enter 1 for harry\nenter 2 for kannu\nenter 3 for akash\n"))
if c==1:
    k = int(input("enter 1 for log and 2 for retrieve"))
    if k==1:
        x = int(input("enter 1 for food and 2 for exercise"))
        if x==1 or x==2:
            with open("harry.txt", "a") as of:
                l=input("enter here")
                of.write(str([str(gettime())]) + ": " + l + "\n")
    elif k==2:
        open("harry.txt", "a")
        with open("harry.txt", "r") as of:
            for i in of:
                print(gettime(), i)


elif c==2:
    k = int(input("enter 1 for log and 2 for retrieve"))
    if k==1:
        x = int(input("enter 1 for food and 2 for exercise"))
        if x==1 or x==2:
            with open("kannu.txt", "a") as of:
                l=input("enter here")
                of.write(str([str(gettime())]) + ": " + l + "\n")

    elif k==2:
        open("kannu.txt", "a")
        with open("kannu.txt", "r") as of:
            for i in of:
                print(gettime(), i)


elif c==3:
    k = int(input("enter 1 for log and 2 for retrieve"))
    if k==1:
        x = int(input("enter 1 for food and 2 for exercise"))
        if x==1 or x==2:
            with open("akash.txt", "a") as of:
                l=input("enter here")
                of.write(str([str(gettime())]) + ": " + l + "\n")
    elif k==2:
        open("akash.txt", "a")
        with open("akash.txt", "r") as of:
            for i in of:
                print(gettime(), i)
else:
    print("invalid input")
