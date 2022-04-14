import calendar
# print(calendar.month(2022,4))

# print (calendar.calendar(2022, 2))
# print (calendar.calendar(2022, 2, 1, 6))

# hc=calendar.HTMLCalendar(firstweekday = 1)
# print(hc.formatmonth(2022,4))

ct=calendar.TextCalendar(calendar.WEDNESDAY)
print(ct.formatmonth(2022,4))
ct_month= ct.itermonthdates(2022,4)
print(ct_month)
for i in ct_month:
    print(i)
ct_days= ct.itermonthdays(2022,4)
for days in ct_days:
    print(days)

for l in calendar.month_name:
    print(l)

for m in calendar.monthcalendar(2022,4):
    print(m)
for day in calendar.day_name:
    print(day)