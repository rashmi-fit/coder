"""Given an array which may contain duplicates, 
print all elements and their frequencies."""
array = [1, 2, 3, 2, 5, 3, 4, 6, 5, 4, 3, 2, 5, 2, 1]

output = {}

for i in array:
    if i in output.keys():
        output[i] += 1
    else:
        output[i] = 1
print(output)
