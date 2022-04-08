N = int(input())
empty_list = []
for i in range(N):
    mn = list((input("").split(" ")))

    if mn[0] == "insert":
            a, b = map(int, (mn[1], mn[2]))
            empty_list.insert(a, b)
            # print("insert",mn[0])
    elif mn[0] == "print":
            print(empty_list)
    elif mn[0] == "remove":
            (empty_list.remove(int(mn[1])))
    elif mn[0] == "append":
            (empty_list.append(int(mn[1])))
    elif mn[0] == "sort":
            (empty_list.sort())
    elif mn[0] == "pop":
            (empty_list.pop())
    elif mn[0] == "reverse":
            (empty_list.reverse())
