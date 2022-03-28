# you are given two lissts of numbers and you need to find the total of each of these lists
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

tom_total = calculate_total(tom_exp_list)
joe_total = calculate_total(joe_exp_list)

print("tom's total expense is :", tom_total)
print("joe's total expense is :", joe_total)

'''for item in tom_exp_list:
    total=0
    total=total+item
print('Total expenses of tom:', total)
for item in joe_exp_list:
    total=total+item
print('Total expenses of Joe:', total)
'''
# repeating the above for loop again,so lets do using a function
