num = 153
sum = 0
order = len(str(num))
copy_num = num
while(num > 0):
    digit = num % 10
    sum += digit ** order
    num = num//10
# at the end of the iteration num will be zero so we are saving in copy_num
if(sum == copy_num):
    print(copy_num, "It is a armstrong number")
else:
    print(copy_num, "It is not an armstrong number ")
