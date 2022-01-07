total=0
def sum(a,b):
    """This function takes two arguments which are integer
    and it will return sum of them as an output! this is called documentation function"""
    print("a:",a)
    print("b:",b)

    total=a+b
    print("total inside function",total)
    return total
n=sum(5,6)
print("Total outside function:",total)