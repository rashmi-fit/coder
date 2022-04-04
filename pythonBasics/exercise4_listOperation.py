# Write a program that counts the number of occurances of word in a sentence entered by user without using built in function.

count = 0
sentence = input("Enter a sentence: ")
print(sentence)
list_word = input("Wanted word: ")
print(list_word)

for i in range(len(sentence)-len(list_word)+1):
    if sentence[i: i+len(list_word)] == list_word:
        count += 1
        print(list_word)
print(count)


'''
Another way
sentence = input("Please enter a sentence\n")
list_of_word = sentence.split()

for word in list_of_word:
    cnt = list_of_word.count(word)
    print(word, "    ", cnt)
'''