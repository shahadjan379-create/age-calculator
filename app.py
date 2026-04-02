from datetime import  datetime
name= str(input("name:"))
date= int(input("date:"))
month= int(input("month:"))
year= int(input("year:"))
print("DOB:",date,".",month,".",year)
birth_date = datetime(year, month, date)
 
now = datetime.now()

age = now.year - birth_date.year

if (now.month, now.day) < (birth_date.month, birth_date.day):
    age -= 1
    print(name, "is", age, "years old")
    
if year >= 2013:
    print (name, "is a Gen Alpha")
elif year >= 1997:
    print (name, "is a Gen Z")
elif year >= 1981:
    print (name, "is a Millennial")
elif year >= 1965:
    print (name, "is a Gen X")
elif year >= 1946:
    print (name, "is a Baby Boomer")
else:
    print (name, "is from Lost Genration")
    