'''
Q3. Ask user 5 times to enter a team name and how many times the team won and how many they lost. 
Store the information in a dictionary where the keys are 
team names and values are lists of form [wins, lossess].
(a) Using this dictionary, allow the user to enter a team name and print out the teams winning percentage.
(b) Using this dictionary, create a list whose entries are the number of wins of each team.
'''
'''
below using if else block 

empty_list={}
for i in range(3):
   
    team_name=input("enter the team name:")
    num_of_won= int(input("enter the number of times won:"))
    num_of_lost= int(input("enter the number of times lost: "))
    empty_list[team_name]=[num_of_won,num_of_lost]
    print(empty_list)
entered_team_name=input("enter a team name again: ")
if entered_team_name in empty_list:
    print(empty_list[entered_team_name])
    win_percentage=empty_list[entered_team_name][0] * 100  /(empty_list[entered_team_name][0] * empty_list[entered_team_name][1]) 
    print("winnning percentage is",win_percentage)

else :
    print("entered team doesnot exist in the list")
# empty_list[entered_team_name][0] --> this is wins
# empty_list[entered_team_name][1] --> this is loses
# so win percentage = wins/(wins+loses) * 100

listof_winning=[]
for i in empty_list.values():
    listof_winning.append(i[0])

print("list whose entries are the number of wins of each team: ",listof_winning)

'''
# using try exception

empty_list={}
for i in range(3):
    team_name=input("enter the team name:")
    num_of_won= int(input("enter the number of times won:"))
    num_of_lost= int(input("enter the number of times lost: "))
    empty_list[team_name]=[num_of_won,num_of_lost]
    print(empty_list)
entered_team_name=input("enter a team name again: ")
entered_team_name in empty_list
try:      
        print(empty_list[entered_team_name])
        win_percentage=empty_list[entered_team_name][0] * 100  /(empty_list[entered_team_name][0] * empty_list[entered_team_name][1]) 
        print("winnning percentage is",win_percentage)
        
except Exception as e:
        print("entered team doesnot exist in the list")
listof_winning=[]
for i in empty_list.values():
    listof_winning.append(i[0])
print("list whose entries are the number of wins of each team: ",listof_winning)

