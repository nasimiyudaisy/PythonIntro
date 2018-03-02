fileName="demo.txt"
WRITE = "w"
APPEND ="a"

data= input("Please enter file name")
file=open(fileName, mode=WRITE)
file.write(data)
file.close()

#file=open(fileName, mode= WRITE)
#file.write("Elkanah, 29 \n")
#file.write("Daisy, 32")
#file.close()

print("File written succesfully")