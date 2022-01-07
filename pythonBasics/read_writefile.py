'''
f= open("Practice/write.txt","a")
f.write("\nI love PHP") # append
f.close()
'''

f= open("Practice/write.txt","r")
f_out= open("Practice/write_wc.txt","w+")

# print(f.read())
# f.close()
for line in f:
    tokens= line.split(' ')
    f_out.write("Wordcount: "+str(len(tokens))+line)
f.close()
f_out.close()

# count number of words in each line