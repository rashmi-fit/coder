'''Q2. Write a program that accepts sentence from the user as input and 
then print the unique words present in that sentense 
along with the number of times they appeared in the sentence. 
Don't use any of the built in fuction or other data structure.'''

empty_list=[]
entered_input=input("Please enter a sentence").split()
print(entered_input)
# [i for i in entered_input if i not in entered_input[entered_input.index(i)+1:]]
print([i for i in entered_input if i not in entered_input[entered_input.index(i)+1:]])

for i in range(len(entered_input)):
    print(entered_input)



# Need to look into it again