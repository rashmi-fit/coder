import calendar
# c=calendar.TextCalendar(calendar.FRIDAY)
# str=c.formatmonth(2022,4)
# print(str)

'''HTML formattter

hc=calendar.HTMLCalendar(calendar.FRIDAY)
str_hc=hc.formatmonth(2022,4)
print(str_hc)
'''

'''text calender
tc=calendar.TextCalendar(calendar.FRIDAY)
str_tc=tc.formatmonth(2022,4)
# print(str_tc)

for i in tc.itermonthdays(2022,4):
    print(i)
'''
# it will fetch list of days for the april month with some zeros 
# which are days belong to the other month as we declared the start day would be friday


'''fetch local machine date and time
import calendar
for name in calendar.month_name:
    print(name)

'''

''' below will give you the day of your ststem where ever you are
import calendar
for day in calendar.day_name:
    print(day)
'''

'''You can fetch the list of the specific day for a whole year. 
For example, there is an audit day on every first Monday of a week. 
You want to know the date of first Monday for each month. '''
import calendar
for month in range(1,13):
    mycal=calendar.monthcalendar(2022, month)
    week1=mycal[0]
    week2=mycal[1]
    if week1[calendar.MONDAY]!=0:
        auditday=week1[calendar.MONDAY]
    else:
        auditday=week2[calendar.MONDAY]
    print(calendar.month_name[month],auditday)
