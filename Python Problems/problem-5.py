## Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

x = input("Enter Some Numbers: \n")
list = x.split(",")
tuple = tuple(list)
print("list: ", list)
print("tuple: ", tuple)