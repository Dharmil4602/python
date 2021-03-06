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
# x = "Hello..!!"
# y = "My Name Is"
# z = "Alex And My Age Is:"
# a = 20

# e = x + " " + y + " " + z
# e = "My Name Is {} {}".format(z,a) ## We have used format method because considering that users name is not provided and is being entered dynamically. Here {} are used to represent the value of z. There can be more than one {}.

# print(e)

## Second String Formatting Method.

# e = f"My name is {z} {a}" ## Here we have used f in the starting which is used for formatting the string according to our need.
# print(e)

## String Formatting Using List

# hey = ["Dev", "Sports", "20"]
# e = f"My name is {hey[0]}, my hobby is {hey[1]} and my age is {hey[2]}"
# print(e)

## String Formatting Ended

## List Data Type Starts

## --> List is simply defined as the array of strings, numbers, etc.

# print(dir(list)) ## This will shows how many methods we can use with list

# x = ["Hello", "There", "How", "Are", "You", 8, 10.6]
# print("Length Of List x is: ", len(x)) ## Prints the length of the list

# x.pop() ## Here last element if removed
# x.append(11) ## Here element is added at last position
# x.remove("There") ## Here selected element is removed from the list
# del x ## Deletes the list
# print(x)

## Likewise there are other methods in list

## List Data Type Ended

## Tuple Data Type Starts

## lists are written in square brackets [] while tuples are written in () brackets. Elements of tuple cannot be changed. i.e we cannot add or remove elements in tuple like we can do it in lists. Once tuple is created it will remain the same through out the program

# x = ("Bread", "Slice", "Mango", "Maza", 8, 10.6)
# print(x[2])

## Tuples Data Type Ended

## Dictionary Starts

## Dictionary are nothing but the key value pairs. Here we access particular element with the help of Key.



x = {"name":"Dharmil", "sname":"Shah", "age":21}
# print(x["name"])
# print(x["sname"])
# print(x["age"])

## If we want to change any particular value, we can do it with the help of dictionary.
## Always mention the name of key in quotes.

x["age"] = 22
print(len(x)) ## prints the length of dictionary in terms of key value

## Added element in the dictionary
x["year"] = 2022

## Removing element from dictionary
x.pop("year")

## For removing the last item in the dictionary, we'll be using: x.popItem() method

x.popitem()
print(x)
