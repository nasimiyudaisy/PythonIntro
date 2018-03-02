#n =0

#n= int(input("Enter value of n "))
#print(n)

#if (n%2==1):
#    print("Wierd")
#else:
#    print("Not Wierd")
#if (n%2==0) and (n in range(2,5)):
#    print("Not Wierd")
#else:
#    print("Wierd")
#if (n%2==1) and (n in range(6,20)):
#    print("Wierd")
#else:
#    print("Not Wierd")
#if (n%2==0) and (n>20):
#    print("Not Wierd")

n=''

n=int(input("Enter value of n"))

if (n%2==1):
    print("Wierd")

elif (n%2==0) and (n in range(2,5)):
    print("Not Wierd")

elif (n%2==1) and (n in range(6,20)):
    print("Wierd")

elif (n%2==0) and (n>20):
    print("Not Wierd")
else:
    (print("Wierd"))
