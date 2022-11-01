"""
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))


# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])


numbers[2] = numbers[2] + 1
# print(numbers[2])


num = [1, 2, 3, 4, 5, 6, 7, 8]

# def sq(a):
#     return a*a

square = list(map(lambda x : x*x ,num))
print(square)
"""

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)

#_____________ FILTER _____________

# list1 = [1, 2 ,3 ,4, 5, 6, 7, 8]
# def is_greater(num):
#     return num > 5
# grt = list(filter(is_greater, list1))
# print(grt)

#------------ REDUCE -------------

# from  functools import reduce
# num = [1,2,3,4]
# val = reduce(lambda x,y : x+y, num)
# print(val)


n = [1, 2, 3, 4, 5]

y = list(map(lambda x: x/2, n))
print(y)
