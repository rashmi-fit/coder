# Accept 5 string values from user and store them as part of tuple. 
# Print the elements of tuple with their indices in reverse order.
empty_tuple=()
for i in range(5):
    entered_string= input("enter your tuple:")
    empty_tuple=empty_tuple+(entered_string,)
    print(empty_tuple)
print(empty_tuple[::-1])

for idx,val in enumerate(empty_tuple):
    print((idx,val))