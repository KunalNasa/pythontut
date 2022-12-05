#Generators are used to conserve ram. Generators are type of iterators.
# If the body of a def contains yield, the function automatically becomes a generator function.
"""
Iterable - __iter__() or __getitem__() is defined
Itertor - __next__() is defined
Iteration -
"""
#return - return the value and move back to the start of a function.
#print - print the value on the console.
#yield(Generator) - generate values on the fly.
# def gen(n):
#     for i in range(n):
#         yield i
        # return i

# g = gen(3454564354545334534)
# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# print(g) #output = <generator object gen at 0x100581a10>
# print(g) #output  = 0

# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n-1)
# num = int(input("enter here\n"))
# print(fac(num))



def fac(num):
    facto = 1
    for i in range(1,num+1):
        facto *= i
    yield facto

x = fac(5)
print(x.__next__())





