# f = open("kannu2.txt", "w")
# f.write("10 rupee ki papsi kannu bhai saxy")
# f.close()


# f = open("kannu2.txt", "a")
# a = f.write("10 rupee ki papsi kannu bhai saxy\n")
# print(a)
# f.close()



#below: handle read and write both
#below function only works when file is already created

f = open("kannu2.txt", "r+")
print(f.read())
f.write("thank you")
