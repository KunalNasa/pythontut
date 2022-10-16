x = (input("enter your first number\n"))
y = (input("enter your second number\n"))

try:
  print("the sum of two numbers is",
       int(x) + int(y))
except Exception as d:
    print(d)

print("this txt is very important")
