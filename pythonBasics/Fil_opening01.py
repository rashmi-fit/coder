''' Write a program that reads a file and prints out occurences of each word.'''
File = [File.strip("\n") for File in open(
    "/Users/rmn7591/Documents/BITS/Class/CS3/Additional Notebooks S3/my_file.txt")]
my_dict= dict()
for l in File:
    l=l.strip()
    w=l.split(" ")
    for word in w:
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1
for key in list(my_dict.keys()):
    print(key,my_dict[key])
