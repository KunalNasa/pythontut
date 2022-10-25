# colleges = ["DTU", "NITH", "NSUT", "USICT"]
# colleges[1] = "NITKKR"
# x = colleges.copy()
# colleges.insert(3, "IIT")
# y = colleges.count("IIT")
# print(y)
# print(colleges)
# print(x)
#tup = (2, 3, 4)
#print(tup)

#list = ["kannu", "34", "tannu","15", "mannu", "channu"]

#list constructor
# names = list(("kannu", "mannu", "channu"))
# print(type(names))


#to change the item in the list
# fist = ["kannu", "34", "tannu","15", "mannu", "channu"]
# fist[1] = "20"
# print(fist) #output will show 20 on index 1, this is why lists are mutable as we have changed some values in it
# fist[1:3] = ("15", "bannu")
# print(fist)
#note we can add less or more values while changing the list items in some range

#we can also insert new items without replacing them with old items by using insert method
# chest = ["34", "36", "38", "40"]
# chest.insert(2, "39")
# print(chest)

#to add items of list to other list use extend() method. {we can also add tups, dicts, sets etc.}

# fruits = ["mango", "apple", "grapes"]
# vegitables = ["carrot", "raddish", "onion"]
# fruits.extend(vegitables)
# print(fruits)
# fruits.pop(1) #empty () will remove the last item
# print(fruits)
# # fruits.clear() #clears the list but empty list remains
# # print(fruits)
# # del fruits #deletes the entire list
#
# #to sort list in descending order , reverse = True.[ We can also use reverse.fruits method if lst contains alphbts.]
# fruits.sort(reverse=False)
# print(fruits)


#add two lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# list3 = list1 + list2
# print(list3)
