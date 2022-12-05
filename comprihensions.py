# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

#_______LISTCOMPREHENSION________
# ls = [i for i in range(100) if i%3==0]
# print(ls)


#_______DICTIONARYCOMPREHENSION_______
# dict1 = {i:f"item {i}" for i in range(5)}
# # dict1 = {value:key for key,value in dict1.items()}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)

#_______SETCOMPREHENSION________
# dresses = {dress for dress in ["dress1", "dress2","dress1", "dress2","dress1", "dress2","dress1", "dress2"]}
# print(dresses)
# print(type(dresses))

#_______GENERATORSCOMPREHENSION__________
# evens = (i for i in range(100) if i%2==0)
# print(evens)
# print(evens.__next__())
# print(evens.__next__())

# for items in evens:
#     print(items)

# print(type(evens))




# n  = int(input("enter the number of items in your list"))
# x = int(input("Enter 1 for list comprehension.\n"
#           "Enter 2 for dictionary comprehension\n"
#           "Enter 3 for set comprehension\n"))
# string = (input("enter the name of items with _ between them "))
# list = string.split("_")  #split func will convert string into list
#
# if x == 1:
#     lst = [i for i in list]
#     print(lst)
#     print(type(lst))
# if x == 2:
#     dict = {i:f"{i}" for i in  list}
#     print(dict)
#     print(type(dict))
# if x == 3:
#     set = {i for i in  list}
#     print(set)
#     print(type(set))
