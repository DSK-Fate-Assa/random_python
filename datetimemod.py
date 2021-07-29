from datetime import datetime

my_birthday = datetime(2006, 10, 7, 10, 30, 21) #year, month, day, hour, minutes, seconds

print(my_birthday.weekday()) 
#prints what day of the week the day was/// 0 = monday, 1 = tuesday,..., 6 = sunday

age = datetime.now() - my_birthday #you can subract datetimes

print(datetime.now()) #prints current date and time
print(my_birthday.day)

""" 
strptime and strftime - these are methods in datetime that work with dates and strings
-p stands for parsed because it parses through a string and f stand for formt because it formats a string

strptime makes datetimes out of a string using formats and strftime makes strings out of datetimes
e.g:
""" 

parsed_string = datetime.strptime("Oct 7, 2006", "%b %d, %Y")
"""
This makes a datetime from the given string and formats and saves it to variable parsed_string

The first argument is the string from which the datetime will be created
The seconds argument is a string which shows the formatting of the previous string and to know which formats to
use,, you can use the link : https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
"""

random_day = datetime.strftime(datetime.now(), "%b %d, %Y")
"""
in strftime, the first argument is the date which will be converted to a string and
the seconds argument is a string with the format codes to show how to display the time in the string
the same format codes used in strptime can be used in strftime
"""
print(parsed_string)
print(random_day)
