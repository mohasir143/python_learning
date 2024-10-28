# it is all about built in function
#Mapping()
# map(fun,iter)
# list=[2,5,67,78,93]
# def add(n):
#     return n**2
# result=map(add,list)
# print(list(result))

# 1.Square all numbers in a list

                     
# mylist=[7,42,90,54,55,2,15]
# def sum(x):
#     return x*x
# result=map(sum,mylist)
# print(list(result))                          


# 2. Convert all strings in a list to uppercase

# name="mohamed mohasir"
# def upper(x):
#     return x.upper()
# result=map(upper,name)
# print(list(result))


# 3.Add 10 to each number in a list

# mylist=[55,67,84,8,1,75,86]
# def add(y):
#     return y+10
# result=map(add,mylist)
# print(list(result))

# 4. Double each number in a list

# mylist=[68,89,5,2,32,77,90]
# def double(t):
#     return t*2
# result=map(double,mylist)
# print(tuple(result))

# 5. Capitalize the first letter of each string in a list

# name=("mohamed","mohasir","aravinth","kumar")

# def capital(r):
#     return (r.capitalize())
# result=map(capital,name)
# print(list(result))


# 6.Filter out even numbers from a list

# mylist=[78,36,10,35,78,66]

# def even_num(s):
#     return s%2==0
# result=filter(even_num,mylist)
# print(list(result))


# 8.Filter out numbers greater than 10 in list

# mylist=[77,84,2,8,56,65,78]
# def great(u):
#     return u>=10
# result=filter(great,mylist)
# print(list(result))



# 9.Filter out strings containing the letter 'a'

# mylist=["Aravinth","Mohasir","monkey","boy","jackie"]
# def letter(a):
#     return "a" in a
# result=filter(letter,mylist)                                    
# print(list(result))


# 10. Filter out numbers that are not divisible by 3

# mylist=[3,23,10,30,7,9]
# def divisible(g):
#     return g%3!=0
# result=filter(divisible,mylist)
# print(list(result))

# 11.Filter out negative numbers from a list

# mylist=[-55,67,0,84,-8,-1,75,86,-67]
# def negative(c):
#     return c<=0
# result=filter(negative,mylist)
# print(list(result))

# 12. Filter out numbers that are not divisible by 3

# mylist=[3,56,19,30,49,9]
# def divisible(g):
#     return g%3!=0
# result=filter(divisible,mylist)
# print(list(result))

# 13. Find the product of all numbers in a list


# mylist=[2,6,10,22,60]
# def product_id(f):
#     return f*f
# res=map(product_id,mylist)
# print(list(res))

# 14.Concatenate a list of strings

# import functools

# mylist=["Harish","Sanjay","raju","Rocky"]
# def insert(q,p):
#     return q+" "+p
# result=functools.reduce(insert,mylist)
# print(result)


# 15.Find the maximum number in a list
# import functools
# mylist=[3,56,19,30,49,9]
# def max(i,j):
#     if i>j:
#         return i
#     elif j>i:
#         return j
# res=functools.reduce(max,mylist)
# print(res)

# # 16.Compute the sum of squares of numbers in a list
# import functools
# mylist=[2,6,10,22,60]
# def add(a,b):
#     return a+b**2
# res=functools.reduce(add,mylist)
# print(res)

# 17.Compute the factorial of a number using reduce

# n=5
# factorial=1
# def maths(v,n):
#     return v*n
# res=functools.reduce(maths,range(1,n+1))
# print(res)

# 7.Filter out words shorter than 4 characters


# string=("re","mohamed","apsal","raju","jgf")
# def short(f):
#     return len(f)<4
# result=filter(short,string)                                     
# print(list(result)) 

