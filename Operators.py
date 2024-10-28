# #Arithmetic Operators
x=13
y=8
add=x+y
print("ADDITION",add)
print("SUBTACTION",x-y)
print("MULTIPLICATION",x*y)
print("DIVISION",x/y) #It is above value
print("MODULUS",x%y)  #It is remainder value
print("EXPONENTIATION",x**y)#Its called as Square or power value.
print("FLOOR DIVISION",x//y)#Its called as remainder value only point inside.

#Assignment Operators
x=13
y=8
x+=5
print(x,"ADD")

x=13
y=5
y-=10
print(y,"SUB")


x=13
y=5
x*=8
print(x,"MULTI")

x=13
y=5
x/=7
print(x,"DIVI")

x=13
y=5
y%=5
print(y,"MODULE")

x=13
y=5
y**=5
print(y,"EXPONENT")

x=13
y=5
x//=2
print(x,"FLOOR DIV")

#comparison operater
x=6
y=7
print(x==y,"EQUAL TO")

x=5
y=9
print(x!=y,"NOT EqUAL TO")

x=6
y=7
print(x>y,"GREATER THAN")

x=45
y=59
print(x<y,"LESSER THAN")

x=99
y=79
print(x<=y,"LESSER EQUAL")

x=77
y=97
print(y>=x,"GREATHER EQUAL")

# #logical operator
x=56
y=78
print(x>5 and y==x)#Its only true true is = true

x=58
y=43
print(x!=y or y<x)#Its true anyline ,also use True answer

x=66
print(not (x!=56, 59<x))#Its full of opposition.

# #Identity operator
x=10
y=10
print(x is y,"SAME")#Its also same as equal to is called as IS.

x=78
y=78
print(x is not y)#Its also same as not eual to called as IS NOT.

#Membership operator
x="apple", "orange","mango"
y="orange", "strawberry"
print( "orange" in x)   #Its is two variables are same num or alphabet is called as IN.

x=56,87,77,90
y=88,10,77,100
print(77 not in y) #Its is two variables are not same or num or albhabet is called as NOT IN.

#Bitwise Operator

number=int(input("Enter a number"))
number2=int(input("Enter a number"))
number=55
number2=71
result=number & number2   # 9 & 13            It hads used as binary numbers
print(result,"bitwise and")

number1=int(input("Enter a number"))
number3=int(input("Enter a number"))
result=number1 | number3
print(result,"bitwise or")  # 15 & 6


