# Q2. Ask a use to enter a sentence
# (a) Print out the third word of sentence
# (b) Print out every second word of sentence

enter_sentence = input("enter a sentence: ")
print(enter_sentence)

count_word = enter_sentence.split()

print(count_word[:2])

new_list = count_word[1 : : 3]
for i in new_list:
    print(i)
