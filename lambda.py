#lambda
#The lambda means a single line to finsh our code.
#                              Task

# 1. Add Two Numbers

# result= lambda i,j:print(i+j,"addition") 
# result(5,5)

# 2.Find the Maximum of Two Numbers

# me= lambda i,j:print("i is the maximum number",i) if i>j else print("j is the maximum number",i)
# me(59,55)


# 3.Square a Number
# ocean= lambda z:print(z**2)                     #Is is directly used in the lambda series.
# ocean(8)


# 4.Reverse a String
# academy= lambda y:print(y[::-1])                #It is print to working this concept
# academy("mohamed mohasir")

# 5.Check if a Number is Even
# rajan= lambda r: print("even number : ",r)if r%2==0 else print("add number :",r) 
# print(rajan(666))
# print(rajan(777))



#                                       Recursive

# def func3():
#     print("func3...")

# def func2():
#     func3()
#     print("func2...")

# def fucn1():
#     func2()
#     print("fucn1...")


# fucn1()

# recursive function - a func call itself directly or indirectly

# def sayHI():
#     print("hi.....aravainth..mohamed..")
#     sayHI()

# sayHI()



# 1.print 10 to 1.


# def variable(x):
#   if x>0:
#      print(x)
#      variable(x-1)
# variable(15)

# 2. Print 1 to 10.

# def xerox(j):
#    if j<=15:
#       print(j)
#       xerox(j+1)
# xerox(1)


# 3. Fibonacci 

# def fibonacci(x):
#     num = 0
#     num1 = 1
#     next_num = num1
#     count = 1

#     while count <= x:
#         print(next_num, end=" ") 
#         count +=1
#         num, num1 = num1, next_num
#         next_num= num + num1

#     print()
# fibonacci(5)


# 4. Sum of list

# mylist = [1, 2, 3, 4, 5]

# def list(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i
#     return sum

# result = list(mylist)
# print(result)


# 5.Get a input from user as number. If user entered negative number. Throw message as invalid. 
# If user entered  0 throw factorial of 0.  Else it has to act as recursive factorial function.

def num(n):
   factorial=1
   if n==0:
     print("It is invalid")
   for i in num:  
     factrial=factorial*i
     print("factorial")
num(5)




