fileName="perfomance.csv"
WRITE="w"
APPEND="a"
 
file=open(fileName, mode=WRITE)
file.write("Doyle McCarthy, 27 \n")
file.write("Jodi Mills, 25 \n")
file.write("Nicholas Rose, 32 \n")
file.write("Kian Goddand, 36 \n")
file.write("Zuha Hanania, 26 \n")
file.close()

print("File written successfully")