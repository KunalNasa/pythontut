# def searcher():
#     import time
#     file = "This is a reading file"
#     time.sleep(4)
#
#
#     while True:
#         text = (yield)
#         if text in file:
#             print("Your text is present in this file")
#         else:
#             print("Your text is not present in this file")
#
# search = searcher()
# print("search started")
# next(search)
# search.send("This")
# input("press any key")
# search.send("That")
# search.close()

def searcher():
    f = open("book.txt", "r+")
    # x = f.write("kannu\n" "mannu\n" "tannu\n"  "akash\n" "kunal\n")
    readfile = f.read()


    while True:
        name = (yield)
        if name in readfile:
            print("Your name is found in book")
        else:
            print("Your name is not found in book")

search = searcher()
next(search)
x = input("write your name")
search.send(x)
