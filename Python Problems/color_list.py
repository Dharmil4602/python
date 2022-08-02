# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
color_list_1 = set(["Red", "Green", "White", "Black"])
color_list_2 = set(["Green", "Black"])
# for i,j in color_list_1,color_list_2:
#     if color_list_1[i] != color_list_2[j]:
print(color_list_1.difference(color_list_2))