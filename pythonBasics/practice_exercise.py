
# import numpy as np
# x = [[2, 1],
#      [3, 4]]
# max_v = np.array(x)[:, 0].max()


# w = input("What is the word?\n")
# while w != "Quit":
#     print("word:", w)
#     break


""" hello
hello
hello hellohellohellohellohello
hellohellohellohellohellohello
hellohellohello

"""

'''
def len_upper(input):
    count = 0
    input = "rashmi is A Girl" 
    for i in input:

        if i.isupper():
            count += 1
            print(count)
    

    if count == 0:
        print("prints the error message")
        return -1
    return count

len_upper("rashmi is A Girl")
'''

''' i need some help . i want to count how many items that have age>=50 . Where am i going wrong ?'''
import requests
r = requests.get("https://coderbyte.com/api/challenges/json/age-counting")
data_dict = r.json()

all_ages_str = data_dict['data'] # read the data dict value of this key, this is where age values are present
all_ages_list = all_ages_str.split(',')[:5] # convert this big string into a dict by using split on comma character
print(all_ages_list)

count = 0 # let's begin counting how many items that have age>=50
for element in all_ages_list: # iterate on the age list created above
    if 'age' not in element:
        continue
    age = int(element.split('=')[1]) # when we are here, it means age is present in the string, split and get the age number
    if age > 50: # check if age is greater than 50
        count += 1 # if age>50, increment the count by 1
print(f'count of how many items that have age>=50 is : {count}') # print final count of how many age>50 found 



