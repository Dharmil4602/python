# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

# n = input("Enter Any Number: \n")
def double(n):
    if n <= 17:
        return 17-n
    else:
        return abs(n - 17)*2

print(double(20))