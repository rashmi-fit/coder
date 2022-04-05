'''Q1. Write a program that asks user to enter the 5 product names and prices.
Store all of these in a dictionary with keys are product names and prices are values. 
Then allow the user to input the product name and print the corresponding price of the product.
'''

empty_dict={}
for i in range(3):
    key=input("enter product names:")
    value=int(input("enter product prices:"))
    empty_dict[key]=value
    print(empty_dict)

input_product=input("enter product names you are want the price for:")
if input_product in empty_dict:
    print("the respective price is",empty_dict[input_product] )
else:
    print("product is not available in the dictionary")