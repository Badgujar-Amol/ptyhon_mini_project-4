import calendar

year = int(input("Enter Year:"))
month = int(input("Enter month:"))
date = int(input("Enter date:"))

day = calendar.weekday(year,month,date)

weekday = calendar.day_name[day]

print(weekday)
