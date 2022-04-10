def primefactor(num):
    divisor = 2
    quotient = num
    while (divisor <= quotient):
        if (quotient % divisor) == 0:
            print(divisor)
            quotient = quotient/divisor

        elif (quotient == 1):
            break
        else:
            divisor += 1


primefactor(12)


# def draw_rectangle(length, height):

#     for i in range(length):
#         print("")
#         for j in range(height):
#             print('*' if i in [0, length-1]
#                   or j in [0, height-1] else " ", end=" ")

#         print('\n')

# draw_rectangle(5, 3)
