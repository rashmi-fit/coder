''' Q2. Create a dictionary where keys are name of months and days are values.
(a) Ask the user to input a month name and use the dictionary to tell how many days are in that month.
(b) Print out all the keys in alphabetical order.
'''

empty_dict={}
for i in range(3):
    keys=input("Enter month name")
    values=input("enter days ")
    empty_dict[keys]= values
    print(empty_dict)
searched_month=input("enter the month name you want to know the days ")
print(searched_month)

searched_month in empty_dict
print("relevant days are",empty_dict[searched_month])

for keys in sorted(empty_dict):
    print(keys)  