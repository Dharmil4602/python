## Types Of Operators
## 1. Arithmetic Operators
## 2. Assignment Operators
## 3. Comparison Operators
## 4. Logical Operators
## 5. Identity Operators
## 6. Membership Operators
## 7. Bitwise Operators

## 1. Arithmetic Operators

# print(4+5) ## Addition
# print(5-4) ## Subtraction
# print(10/5) ## Division --> Division operator is used for finding the quotient
# print(4*5) ## Multiplication
# print(25%2) ## Modulo --> Modulo operator is used for finding the remainder
# print(2**4) ## Power Operator
# print(9//2) ## Same as division operator but here the value gets rounded off (We get only integer values here)


## 2. Assignment Operator

# x = 2 ## Equals Operator
# print(x)
# x += 4 ## This is same as x = x + 4
# print(x)
# x -= 2 ## This is same as x = x - 2
# print(x)
# x *= 2 ## This Is Same As x = x * 2
# print(x)
# x /= 2 ## This Is Same As x = x / 2
# print(x)
# x %= 2 ## This Is Same As x = x % 2
# print(x)
# x **= 2 ## This Is Same As x = x ** 2
# print(x)

## Comparison Operators

# 1. Equality Operator (==)
# 2. Not Equal To Operator (!=)
# 3. Greater Than Operator (>)
# 4. Greater Than Equal To Operator (>=)
# 5. Less Than Operator (<)
# 6. Less Than Equal To Operator (<=)

## Identity Operators

# 1. is
# 2. is not
# x = 3
# y = 3
# a = 1
# b = 2
# print(x is y)
# print(a is not b)

## Membership Operators

# 1. in ## Specifies whether the particular element is present in the list, tuple. If not present then it will return false
# 2. not in ## Specifies whether the particular element is not present in the list, tuple. If not present then it will return true

x = [1,2,3,4]
print(2 in x)
print(5 not in x)
print(4 not in x)

## Similarly we can check it for strings too.

a = "Hey There"
print("e" in a)
print("T" not in a)