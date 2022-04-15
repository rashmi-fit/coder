'''
Q2. Write a function call one_way that takes two strings and 
returns True if the strings are of the same length and 
differ in exactly one letter, like bike/hike or water/wafer.
'''


def one_way(string1, string2):
    for i in len(string1):
        if string1 == string2:
            print("string matches")
        else:
            print("doesnot match")
        return True


testing = one_way("bike", "hike")
print(testing)
