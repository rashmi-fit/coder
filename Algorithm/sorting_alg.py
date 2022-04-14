'''
Lets write a function merge that takes two already sorted lists of possibly different lengths 
and merges them into a single sorted list.
-Do this using the sort method
-Do this without using the sort method
'''
#  using sort method


def merge_fun(list1, list2):
    list1 = input("enter inputs of legth 4")
    list2 = input("enter inputs length 3")
    empty_list = []
    while list1 and list2:
        if list1 in list2:
            empty_list.append(list1.pop())
        else:
            empty_list.append(list2.pop())

    empty_list += list1
    empty_list += list2

    return empty_list
