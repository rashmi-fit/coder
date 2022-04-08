
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example,
#  alison heck should be capitalised correctly as Alison Heck. 

# entered_string="rashmi m"
entered_string=input("enter fullname:")
# print(entered_string.split())
for i in entered_string.split():
    entered_string=entered_string.replace(i,i.capitalize())
print(entered_string)
