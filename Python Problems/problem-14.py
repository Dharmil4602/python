arr = [2,4,6,7,20,10,1,8,9]
num = int(input("Enter A Number: "))
for i in range(arr):
    if(arr[i] == num):
        print("Found")
        break
    else:
        print("Not Found")
        break