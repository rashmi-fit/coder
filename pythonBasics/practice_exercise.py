
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


import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# print(r)
# print(len(r.json()['data']))
data = r.json()
# print(data)
print(r.content)
print(r.iter_content())
# count = 0
# value = data['data'].replace(' ', '').split(',')

# print(value)
# for v in value:
    
#     if 'age' not in value:
#         continue
#     age = int(value.split('=')[1])
#     print(age)
#     if age > 50:
#         count += 1
# print(count)




