## For loop
# x = [0,1,2,3,4,5,6,7,8,9,10]

# for i in x:
#     print(i)
    

## Taking input from the user using for in loop
# Note: here the list should be starting from zero incase the list includes numbers.
# x = [0,1,2,3,4,5,6,7,8,9,10]
# for i in x:
#     x[i] = input("Enter The Name: ")
# print(x)

## While loop

# x = 0
# while x<10:
#     print(x)
#     x += 1

## Looping through the string
# x = "Hello"
# for i in x:
#     print(i)

## Range Function
# range(starting value or value, ending value or range, order)    

# for x in range(10):
#     print(x)

 ## Here in below one, (4,100,2) means that the range will start from 4, end at 100 or near to 100, after every digit two number will be skipped which is the order
# for x in range(4,100,2):
#     print(x)

## Nested loops

x = ["big", "small", "large", "dwarf"]
y = ["iron", "silver", "gold", "platinum"]

# for i in x:
#     for j in y:
#         print(i,j)

## We can print the very same output as it is printed by above code by below code as well

a = 0
b = 0
for i in x:
    for j in y:
        print(x[a], y[b])
        b = b + 1
    a = a + 1
    b = 0
