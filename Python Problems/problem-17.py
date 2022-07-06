import math

n = input("Enter the first number: \n")
y = input("Enter the second number: \n")
x = math.gcd(int(n), int(y))
print("Greatest Common Divisor Is:", x)