## All Tutorial Will Be Updated Here Only.

# print('Hello')
# x = 2
# y = float(x)
# print(type(y))
# print(dir("strings"))
# print(" ")
# print(dir("int"))
# print(" ")
# print(dir("float"))


## String Formatter
## First String Formating Method.
x = "Hello..!!"
y = "My Name Is"
z = "Alex And My Age Is:"
a = 20

e = x + " " + y + " " + z
e = "My Name Is {} {}".format(z,a) ## We have used format method because considering that users name is not provided and is being entered dynamically. Here {} are used to represent the value of z. There can be more than one {}.

# print(e)

## Second String Formatting Method.

e = f"My name is {z} {a}" ## Here we have used f in the starting which is used for formatting the string according to our need.
# print(e)

## String Formatting Using List

hey = ["Dev", "Sports", "20"]
e = f"My name is {hey[0]}, my hobby is {hey[1]} and my age is {hey[2]}"
print(e)
