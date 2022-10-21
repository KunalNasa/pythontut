# def fac_iterative(n):
#     fac = 1
#     for i in range (n):
#         fac = fac * (i+1)
#     return fac
# number = int(input("enter an integer"))
# print("factorial using iterative method", fac_iterative(number))

# def fac_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n * fac_recursive(n-1)
# number = int(input("enter an integer"))
# print("factorial using recursive method", fac_recursive(number))


#this is how this recursive code will run
# 5 * fac_recursive(4)
# 5 * 4 * fac_recursive(3)
# 5 * 4 * 3 * fac_recursive(2)
# 5 * 4 * 3 * 2 fac_recursive(1)
# 5 * 4 * 3 * 2 * 1



#fibbonacci numbers

# def function(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return function(n-1) + function(n-2)
# number = int(input("enter an integer"))
# print(function(number))
