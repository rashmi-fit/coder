
# Q1. Write a program that accepts 5 lists from the user, each one of which contains three values in it assignment marks, midsem marks and compre marks.
# (a) Compute the total marks obtained by each student
# (b) Print out the average of the class.

# empty_list=[]
# for k in range(3):
#     for i in range(3):
#         entered_string=eval(input("enter three marks :"))
#         for i in range
#         empty_list.append(entered_string).__format__
#     print(empty_list)
    

# sum_mark= sum(empty_list)
# print("sum of marks:",sum_mark)
# average_marks=sum_mark/len(empty_list)
# print("average of mark:",average_marks)



for k in range(5):
    empty_list = []
    for i in range(3):
        entered_string=eval(input("enter the marks :"))
        empty_list.append(entered_string)
        sum_mark = sum(empty_list)
    print(empty_list)
    print("Marks obtained for student ", k+1 ,"is:","\t", sum_mark)
average_marks=sum_mark/len(empty_list)
print(average_marks)