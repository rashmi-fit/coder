'''
Q2. Write a function call one_way that takes two strings and 
returns True if the strings are of the same length and 
differ in exactly one letter, like bike/hike or water/wafer.
'''


def one_way(string1, string2):
    if len(string1) == len(string2):
        if string1 == string2:
            print("strng matches")
        else:
            print("doesnot match")
        return True


testing = one_way("bike", "hike")
print(testing)
