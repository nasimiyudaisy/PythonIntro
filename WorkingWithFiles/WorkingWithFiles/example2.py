fileName = "Letter.txt"
WRITE="w"
APPEND="a"

data=input("Enter your data here ")

file = open(fileName, mode=WRITE)
file.write(data)
file.close()

print("This file has been printed successfully")