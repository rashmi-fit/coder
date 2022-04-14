'''
Q1. Write a function called closest that takes a list of numbers L and a number n and 
returns the largest element in L that is not larger than n. For instance, 
if L=[1, 6, 3, 9, 11] and n =8, then the function should return 6, 
because 6 is the closest thing in L to 8 that is not larger than 8.

'''

def closest(L,n):

    min_diff= abs(L[0]-n)
    index=-1
    for i in range(len(L)):
        diff=abs(L[i]-n)
        if diff<=min_diff:
            min_diff=diff
            index=1
        
    return L[index]
L=[1, 6, 3, 9, 11]
n =8

closest_num=closest(L,n)
print(closest_num)