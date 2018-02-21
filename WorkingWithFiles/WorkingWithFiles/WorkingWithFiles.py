fileName="demo.txt"
WRITE = "w"

file=open(fileName, mode= WRITE)
file.write("Hello Daisy \n")
file.write("How are you doing?")
file.close()

print("File written succesfully")