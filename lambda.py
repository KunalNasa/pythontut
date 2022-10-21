# def func(a,b):
#     return a + b
# print(func(3,4))

# given above and below works same

# add = lambda x, y: x + y
# print(add(3,4))

# x = lambda a, b, c: a * b + c
# print(x(2,3,4))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
