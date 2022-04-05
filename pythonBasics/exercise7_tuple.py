# Q1. Accept 5 string values from user and store them as part of tuple. 
# Print the elements of tuple with their indices.
my_string=()
for i in range(5):
    entered_string=input("enter 5 string values")
    my_string=my_string+ (entered_string,)
    print(my_string)

for idx,val in enumerate(my_string):
    print(idx,val)

# enumerate helps to get both indices and its elements