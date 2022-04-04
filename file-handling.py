## We will be reading the test.txt file

## First we need to open the file with the help of open() method in which we need to pass two parameters. open("file name", "the mode in which we need to open it")

## Mode of opening the files can be read mode (r), write mode (w), append mode (a).
openFile = open("test.txt", "r") ## Read mode
x = openFile.read()
print(x)

## While we are in reading mode, we need not to close the file.
## But when we are in writing mode we need to close the file.  

# writeFile = open("test.txt", "a")
# writeFile.write( "Orange\n")
# writeFile.close()