import datetime
currentDate= datetime.datetime.now()
print(currentDate.minute)
#print(currentDate.year)
#print(currentDate.month)
#print(currentDate.day)

##formatting dates using strftime
#print(currentDate.strftime("%d %B %y"))
#print(currentDate.strftime("%d %b %Y"))

userInput=input('Enter your birthday(mm/dd/yyyy) ')
birthday=datetime.datetime.strptime(userInput,"%m/%d/%Y").date()
print(birthday)

days=birthday-currentDate
print(days)