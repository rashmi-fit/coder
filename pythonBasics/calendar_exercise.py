'''
You can fetch the list of the specific day for a whole year. 
For example, there is an audit day on every first Monday of a week. 
You want to know the date of first Monday for each month. You can use this code
'''


import calendar

specific_day= calendar.setfirstweekday(calendar.MONDAY)
print(specific_day)
print(calendar.firstweekday())
print(calendar.prmonth(2022,4))
print(calendar.month(2022,4))


for x in range(1,13):
    print(x, ":", calendar.month_abbr[x], "-", calendar.month_name[x])
