string="hellorandomstring12341a2b3c"
print(string.isalnum())
# space and special char not coming under alphanumeric

string1="hello"
print(string1.isalpha())

string2="fasdf12$%^&*<><>?:I∆˙∆˙∆˙∆˚˙˙"
print(string2.isascii())

print(string2.isidentifier())

string6="123"
print(string6.isidentifier())

string3="Hello!\nAre you\t #1" 
# escape char
print(string3.isprintable())

string4=" "
print(string4.isspace())

string5="hello python "
print(string5.index("python"))

# abs
# dir
# eval
# format
# range
# round

string= "90.01"
print(eval(string))

str2 = "language"
print("This is an easy programming {}".format(str2))

print( "My name is {fname}, I'm {age}".format(fname = "John", age = 36))
print( "My name is {0}, I'm {1}".format("John",36))
print( "My name is {1}, I'm {0}".format("John",36))
print( "My name is {}, I'm {}".format("John",36))
