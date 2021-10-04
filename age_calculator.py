#note in this program i didnt use strptime method so it may look more complicated but it works just the same

from datetime import datetime
import math

year = int(input("What year were you born in \n"))
month = int(input("What month were you born in, enter in terms of numbers, e.g 1 = January, 2 = February,..etc \n" ))
day = int(input("What day of the month were you born in, e.g 2, 5, 7, 21 \n"))
hour = int(input("What hour  were you born in, use 24 hour time \n"))
minute = int(input("What minute were you born in \n"))
second  = int(input("What second were you born in \n")) 
complete_age = ""

my_birthday = datetime(year, month, day, hour, minute, second) #year, month, day, hour, minutes, seconds
age = datetime.now() - my_birthday

def with_days(my_birthday):
    age = datetime.now() - my_birthday #you can subtract datetimes
    age_with_years_and_days = str(math.floor(int(str(age).split()[0]) / 365)) + " years, " + str(int(str(age).split()[0])%365) + " days, "
    age_with_hours = (str(age).split()[2]).split(":")[0] + " hours, "
    age_with_minutes = (str(age).split()[2]).split(":")[1] + " minutes and "
    age_with_seconds = (str(age).split()[2]).split(":")[2] + " seconds"
 
    complete_age_wl = "You are " + age_with_years_and_days + age_with_hours + age_with_minutes + age_with_seconds+ " old \n" + "NOTE!! NOTE !! this is how many days you have lived for including days leap years !" 
    print(complete_age_wl)
    
def with_time(my_birthday):
    age = datetime.now() - my_birthday
    age_with_hours = str(age).split(":")[0] + " hours, "
    age_with_minutes = str(age).split(":")[1] + " minutes and "
    age_with_seconds = str(age).split(":")[2] + " seconds"
    complete_age = "You are " + age_with_hours + age_with_minutes + age_with_seconds+ " old"
    print(complete_age)


def what_day(my_birthday):
    if my_birthday.weekday() == 0:
        print("You were born on a Monday")
    elif my_birthday.weekday() == 1:
        print("You were born on a Tuesday")
    elif my_birthday.weekday() == 2:
        print("You were born on a Wednesday")
    elif my_birthday.weekday() == 3:
        print("You were born on a Thursday")
    elif my_birthday.weekday() == 4:
        print("You were born on a Friday")
    elif my_birthday.weekday() == 5:
        print("You were born on a Saturday")
    else:
        print("You were born on a Sunday")

if len(str(age).split()) == 3:
    with_days(my_birthday)
    what_day(my_birthday)
else:
    with_time(my_birthday)
    what_day(my_birthday)
