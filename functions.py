#Functions

# def even_number(i):                #The def is function and it used return use and return read benifits.They ()inside values create.It is called as parameters
#    if i%2==0:
#       print("Even number",i)
#    else :
#       print("add number",i)
# even_number(2)                    #It is argument values . the parameters and arguments are (eg)twins    

# The types of parameters and argument

# It is default argument

# def add(x=3,y=5):                  #It is parameteres used to output there is called as default argument
#      print("add:",x+y)

# add()

#It is keyword argument

# def add(x,y):
#      print("add:",x+y)              #It is argument used as output there is called as keyword argument
# add(x=5,y=5)


# def add(x,y):
#     print("Ocean academy")
#     return x+y                        
#     print("Thank you")               #The return value used after not worked print vale=ue
# print(add(2,4))

#                                          task    
# 1.Calculate Square

# def square(a): 
#     print("square:",a**a)                   -            #It is square symbol to finding them  (2x,2x,2x=8)
# square(3)


# 2.Calculate Area of Rectangle


# def area_of_rectangle(length,width):
#     return length * width                                #It is also mutiply with length into breadth of rectangle
# print(area_of_rectangle(length = 5, width = 3))


#3.Even or Add

# def even_add(i):
#     if i%2==0:
#         print("even number",i)
#     else:
#         print("add number",i)                            #It is even and add number find out concept
# even_add(4)


# 4.Calculate Factorial


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)                      #The factorials means multiply,return use and automatically clear next print condition
# print(factorial(5))


# 5.Check Prime Number

# def prime_number(j):
#        if j%2==0 or j%3==0 or j%5==0:
#          print(j,"it is not prime number")
#        else :
#          print(j,"it is prime number")
# print(prime_number(12))
    

# #6.Reverse string

# def reverse_string(i): 
#    return i[::-1]
# print(reverse_string("Mohamed mohasir"))

# 7.Count Characters

# def characters(x):                  
#     return len(x)                                  #   It is count with length
# print(characters("Mohamed mohasir"))

# # 8.list in Sum of Squares

# def list(square):
#     sum=0
#     for i in square:
#         sum=sum+i**2
#     print(sum)
# list([1,2,3])



# 9.Check Palindrome
#The palindrome meanse same number reverse it.

# def palindrome(me):
#     rev=me[::-1]
#     if rev==me:
#        print("palindrome")
#     else:
#         print("not palindrome")
# palindrome("madam")
# palindrome("mohah")

  

# 10.Calculate Fibonacci

#It has 0 and 1 is main using o add the next one
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


# 11.Check Armstrong Number:

# def armstrong(n):
#     sum=0
#     temp=n
#     while temp>0:
#         num=temp%10
#         sum=sum+num**3
#         temp=temp//10
#     if n==sum:
#         print("it is armstrong number.")
#     else:
#         print("not a armstrong number.")
# print(armstrong(153))


# 12.leap year.

# def leap_year(x):
#     if x%4==0 or x%100==0:
#         print("leap year")
#     else :
#         print("not leap year")
# print(leap_year(2040))
# print(leap_year(2025))



                                   #task

#  1: Sum of all arguments

# def sum(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# sum(5,5)

#  2: Multiply all arguments

# def multi(*args):
#     sum=1
#     for i in args:
#         sum=sum*i
#     print(sum)
# multi(5,5)


# 3. Concatenate all arguments

# def concatenate(*args):           
#      for i in args:                                                      -                 #It is adding splitting words used
#         print(i,end="")
# concatenate("mohamed","mohasir","sai","kailash")

# 4.Print arguments and keywords.

# def arg_key(**args):
#     for i,j in args.items():
#         print(i,j)
# arg_key(name="kailash",age="12",place="villianur")



