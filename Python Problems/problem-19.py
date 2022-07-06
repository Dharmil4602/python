x = input("Enter the first number: \n")
y = input("Enter the second number: \n")
z = input("Enter the third number: \n")

if (x == y or z == y or x == z):
    sum = 0
else:
    sum = int(x) + int(y) + int(z)

print("Sum = ", sum)