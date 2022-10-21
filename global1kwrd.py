# k = 10 #Global
#
# def myfunction():
#     print("this is my function")
#     #k = 5 #Local
#     m = 8 #Local
#     global k #we have to write 'global' to change the value of global variable otherwise we can't chage it.
#     k = k + 20
#     print(k,m)
# myfunction()
# print(k)


#nested functions below

# k = 89
# def kannu():
#     k = 20 #local
#     def harry():
#         global k
#         k = 80
#     print("before calling harry:", k)
#     harry()
#     print("after calling harry:", k)
# kannu()
# print(k)
