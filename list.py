#List

#The list are multiple values stored in single variable.
#It has orderd, changeble and allow duplicates.
#It is list(()) to use list[].It is called as "Constructor".

 
# list=["jack","master","rose","spell"]        
               
# print(list[3])                                      -            It is index as 0 to start and find out.

# print(len(list))                                    -            It is length as 1 to start and find out.

# print(list[-1])                                     -            It is negative index to reverse.

# print(list[1:5])                                    -            It is 1 to 5 inside values found.

# if "jack" in list:
#     print("yes")                                    -            (If) statement to working lists:

# else :
#     print("no")


# list[1]="jd"                                        -            It has change to replace the value from list.
# print(list)

# list.append("orange")                               -            It is automatically add from last.
# print(list)

# list.extend(newlist)                                -            It is two list in one list adds.
# print(newlist)

# list.insert(4,"Heart")                              -            It is add extra value inside.
# print(list)

# list.remove("master")                               -            It is remove from list any words.
# print(list)

# list.pop(2)                                         -            It is same as remove but enter as number to remove.
# print(list)

# del list[2]                                         -            It is same as remove model.
# print(list)

# list.clear()                                        -            It is clear all list.
# print(list)                                        
 
# for i in list:                                      -            loop concept to one by one.
    # print(i)

# for i in range(len(list)):                          -            It is loop used as length of range.
#    print(list[i])

# list.sort()                                         -            It is ascending order followed.
# print(list)

# list.sort(reverse=True)                             -            It is decending order(reverse) It is true condition to followed.
# print(list)

# newlist = list.copy()  # OR  [:]                    -            It is copy from another newlist.
# print(newlist)


# list3 = list + list2                                -            It is already lists are sharing new list.
# print(list3)

# for i in list2:
    # list.append(i)                                  -            It is other method of addition and for loop used.
# print(list)


                                                    #task

# 1-in a list of array store even or odd numbers in new list and print

# mylist=[1,2,3,4,5,6,7,8,9]
# even_number=[]
# odd_number=[]
# for i in mylist:
#     if i%2==0:
#         even_number.append(i)
#     elif i%2!=0:
#         odd_number.append(i)
# print(odd_number,"odd number")
# print(even_number,"even number")


# 2-print sum of list

# mylist=[1,2,3,4,5]
# sum=0
# for i in mylist:
#          sum=sum+i
#          print(sum)
        

# 3-product of list when zero in list it cant product that number

# mylist=[1,2,3,0,4,5,8]
# product=1
# for i in mylist:
#     if i==0:
#         continue
#     else:
#         product*=i
#     print(product)


# 4-find duplicate element in a array and print in new array

name=["apple","orange","graphs","apple","banana"]
new=[]
for i in name:
    if name.count(i)>1:
        new.append(i)
print(new)


#6      -    reverse a list.

# list=[2,3,5,12,99,76,43,23,65,24]
# list.sort(reverse=True)
# print(list)




   
