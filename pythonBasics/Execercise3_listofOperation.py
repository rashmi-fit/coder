'''Q3. Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of integers 1 through 50
(c) The list ['aa', 'bb', 'cc'.....] that ends with 26 th letter 'z'. 
(d) the list ['a','bb','ccc','dddd'.....] till z
'''


list1 = [i for i in range(50)]

print(list1)

list2 = [ i*i for i in range(1,49)]

print(list2)

L = 'abcdefghijklmnopqrstuvwxyz'
list4 = [i*2 for i in L] 
list4
print(list4)

list_3= [chr(i+96)*i for i in range(1,27)]
print(list_3)


