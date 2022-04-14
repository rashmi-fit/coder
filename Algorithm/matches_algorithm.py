'''Lets write a function called matches that takes two strings as arguments 
and returns how many matches there are between the strings. 
A match is where the two strings have same character at the same index. 
For instance, 'python' and 'path' match in the first, third and fourth 
characters, so it should return 3.'''


def matches(string1,string2):
    string1 = input("enter string1:")
    string2 = input("enter string2:")
    no_of_matches = 0
    if string1==string2:
        print("both are same")
    for char in range(len(string1)):
     if char < len(string2) and string1[char] == string2[char]:
            no_of_matches=no_of_matches+1
    # print(no_of_matches)
    return no_of_matches

   
match_count = matches("string1", "string2")
print("The match count is ", match_count)
