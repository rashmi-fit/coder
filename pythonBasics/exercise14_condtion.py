# Q3.Write a program that accepts sentence from the user as input and then print the location of each vowel in the sentence.

entered_string= input("please enter a sentence:")
vowel_list = ['a', 'e', 'i', 'o', 'u']
index=0
print(entered_string)
for i in entered_string:
    if i in vowel_list:
        print(i,"i present at location",index)
    index+=1


