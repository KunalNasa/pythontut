import os
# print(dir(os))
# print(os.getcwd())
# f = open("Kunal.txt") #file will be opened
# (os.chdir("/users"))
# print(os.getcwd())
# f = open("Kunal.txt") #will give error

#print(os.listdir()) #will give all the files of this folder(pythontut)
# print(os.listdir("/users"))
# os.mkdir("This")
# os.makedirs("This/that")
# os.rename("Kunal.txt", "kannu.txt")
# print(os.path.join("/Users", "kannu.txt"))
# print(os.path.isfile("/Users/akashnasa"))






# import os
# def soldier(path, file, format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f:
#         filelist = f.read().split("\n")
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#
#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}{format}")
#             i +=1
#
# soldier(r"C:\Users\Haris\Desktop\testing",
#         r"C:\Users\Haris\PycharmProjects\PythonTuts\ext.txt", ".png" )


# print(os.name)
# print(os.sep)
# print(os.uname())


# x = os.getcwd()
# print(os.walk(x)) #it will give generator
#
# for dirpath, dirnames, filenames  in os.walk(x):
#     print(dirpath)

# print(os.stat("kannu.txt"))




# new_folder_path = os.path.join(x, "This")
# file_name = os.path.join(new_folder_path, "sample.txt")
#
# with open(file_name, "w") as f:
#     f.write("hurrrraaayyyyy")


# x = os.getcwd()
# filename = os.path.join(x, "kannu.txt")
# print(os.path.splitext(filename))

# os.remove("book.txt") #it will delete a file


