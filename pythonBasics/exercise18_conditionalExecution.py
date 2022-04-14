'''
Q3. Use a for loop to print a triangle like the one below. 
Allow the user to specify how high the triangle should be.
@
@@
@@@
@@@@
'''

'''increasing pattern'''
# for i in range(4):
#     for j in range(i+1):
#         print('@',end=" ")
#     print()

'''decresing pattern'''
# for i in range(4):
#     for j in range(i,4):
#         print('@',end=" ")
#     print()


# n=4
# for i in range(n):
#     for j in range(i,n):
#         print('',end=" ")


#     for j in range(i+1):
#         print('@',end=" ")
#     print()

'''below is for decresing then increasingpattern'''
# n=4
# for i in range(n):

#     for j in range(i,n):
#         print('',end=" ")
#     for j in range(i+1):
#         print('@',end='')
#     print()

'''below is for increasing then decresing pattern'''
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print('',end='')
#     for j in range(i,n):
#         print('@',end=" ")

#     print()


# n = 4
# for i in range(n):
#     for j in range(i-1):
#         print('', end=' ')
#     for j in range(i, n):
#         print('@', end=" ")

#     print()

'''below is again decresing space and increasing @ pattern'''

# n = 4
# for i in range(n):
#     for j in range(i, n):
#         print('', end=" ")
#     for j in range(i+1):
#         print('@', end='')

#     print()

'''below is for hill pattern
decreasing space,increasing star and increasing star

'''
# n=4
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print('',end='')
#     for j in range(i):
#         print('@',end='')
#     for j in range(i+1):
#         print('@',end='')

#     print()


'''reverse hill'''
# n=4
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print('',end='')
#     for j in range(i):
#         print('@',end='')


#     print()

times = int(input("Enter the height of triangle\n"))
print()

items = []
for i in range(times,-1,-1):
    items.append(i+1)

for x in items:
    print(x * "@")
print()