'''Game Rules

Both players are given the same string,
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
print: the winner's name and score, separated by a space on one line, or Draw if there is no winner
'''

input_string = "BANANA"
vowels = "AEIOU"
Stuart_score = 0
Kevin_score = 0

for i in range(len(input_string)):
        if input_string[i] in vowels:
            Kevin_score += (len(input_string)-i)
        else:
            Stuart_score += (len(input_string)-i)
if Kevin_score == Stuart_score:
        print("Draw")
elif Kevin_score >= Stuart_score:
        print("Kevin", Kevin_score)
elif Kevin_score <= Stuart_score:
        print("Stuart", Stuart_score)
