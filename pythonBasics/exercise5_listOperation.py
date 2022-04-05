# Ask a user to enter a list of strings. Create a new list 
# that consists of those strings with their first characters removed.

entered_string= input("enter a list of strings").split()
print(entered_string)
for i in range(len(entered_string)):
    entered_string[i]= entered_string[i][1:]
print(entered_string)

# l1=(input("enter a list of strings"))
# l2=[]
# for i in range(len(l1)):
#     l2.append(l1[i][1:])
# print("list after removing first characters")
# print(l2)





