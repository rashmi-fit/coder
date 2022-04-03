string = input("Enter a string")
rev_string = string[::-1]
# nothing is given means it takes bydefault 0 and -1 means it takes the string from backward
if(string == rev_string):
    print(string, "this is a palindrome")
else:
    print(string, "this is not palindrome")


# below is is an input is a numbers
string = int(input("Enter a number"))
number = str(string)
rev_number = number[::-1]
# nothing is given means it takes bydefault 0 and -1 means it takes the string from backward
if(number == rev_number):
    print(number, "this is a palindrome number")
else:
    print(number, "this is not palindrome number")

    number1 = int(input("enter a a number"))
