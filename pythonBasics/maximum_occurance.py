'''
#to read the entire contents of text into a single string
with open('/Users/rmn7591/PycharmProjects/Practice/data/poet.txt', 'r') as f:
    contents = f.read()
#to read each line and store them as list
with open('/Users/rmn7591/PycharmProjects/Practice/data/poet.txt', 'r') as f:
    lines = f.readlines()
#for iterative method of reading text in files
with open('/Users/rmn7591/PycharmProjects/Practice/data/poet.txt', 'r') as f:
    for line in f:
        print(len(line))

        fname = input("enter file name")
        count = 0  # count of a specific word
        maxcount = 0  # maximum among the count of each words
        l = []  # list to store the words with maximum count
        with open(fname, 'r') as f:
            contents = f.read()
            words = contents.split()

        for i in range(len(words)):
            for j in range(len(words)):
                if (words[i] == words[j]):  # finding count of each word
                    count += 1
                else:
                    count = count
                if (count == maxcount):  # comparing with maximum count
                    l.append(words[i])
                elif (count > maxcount):  # if count greater than maxcount
                    l.clear()
                    l.append(words[i])
                    maxcount = count
                else:
                    l = l
                count = 0
        print(l)
'''
import re
from collections import Counter
x = Counter(re.findall(
    '\w+', open("/Users/rmn7591/PycharmProjects/Practice/data/poet.txt").read().lower()))
print(x.most_common(5))  # it gives first 5 highest word
