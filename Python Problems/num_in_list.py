# checking whether specified value is in the given list or not.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
enterNumber = int(input("Enter a number: "))
if enterNumber in number_list:
    print("The number is in the list.")
else:
    print("The number is not in the list.")