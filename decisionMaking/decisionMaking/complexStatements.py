country=input("What country do you live? ")
if country.upper()=="CANADA":
    print("Hello")
elif country.upper()=="GERMANY":
    print("bonjour")
else:
    print("aloha or Ciao")

deposit=int(input("How much do you want to deposit? "))
if deposit ==100:
    print("Get free toaster")
elif deposit==1000:
    print("Free movies")
else:
    print("welcome")  