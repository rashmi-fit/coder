# for num in range(101):
num = int(input("enter a number"))
sum = 0
order = len(str(num))
result = num

while(num > 0):
    digit = num % 10
    sum = sum + digit ** order
    num = num//10

if(result == sum):
    print(result, "given number is an Armstrong number")
else:
    print(result, "given number is not an Armstrong number")
