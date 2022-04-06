'''Q4. Write a program that asks the user to enter the password. 
If the user enters the right password, the program should tell them they are logged in to the system. 
Otherwise, the program should ask them to reenter the password. The user should get only five tries to enter the password, 
after which point the program should tell them that they are kicked off of the system.'''


# count=0
# while count<=5:
#     password = input("Password: ")
#     if password == 'blue':
#         print("the program should tell them they are logged in to the system. ")
#         break

#     else:
#         count+=1
#         if count==5:
#              print("password entered incorrectly.")
#              break
#         else:
#             print("the program should ask them to reenter the password")

no_of_try = 0

while True:
    pswd = input('Enter Password: ')
    if pswd == 'blue':
        print('Welcome !!')
        break
    else:
        print('Incorrect Password')
        no_of_try += 1
        if no_of_try == 5:
            print('Maximum try reached')
            break
