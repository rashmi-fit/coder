
'''
Q1. Write a program that asks user to enter a length in centimeters. If negative value is entered, 
the program should tell the user that the entry is invalid. Otherwise the program should convert the 
length to inches and print out the result. 
There are 2.54 centimeters in inches. 
'''

entered_length=eval(input("enter length in centimeters:"))

'''
if entered_length <= 0 :
    print("negative value is entered, the program should tell the user that the entry is invalid")

else:
    total_inch= 2.54 * entered_length
    print("result is: ", total_inch)

'''
try:
    if entered_length <= 0:
        print("negative value is entered, the program should tell the user that the entry is invalid")
    else:
        total_inch= 2.54 * entered_length
        print("result is: ", total_inch)
except:
   
    print("something gone wrong here")
