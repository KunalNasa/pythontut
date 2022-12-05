f = open("kannu.txt")
try:
    l = open("mannu.txt")

except  EOFError as k:
    print("EOFError occured", k)

except  IOError as k:
    print("IOError occured", k)

else:
    print("this will run if exception is not runnning") #means try is running

finally: #we run it when we want to clean the opened data.
    print("run")
    f.close()
    # l.close()
print("k")