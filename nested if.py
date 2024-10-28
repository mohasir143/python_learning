num1=int(input("Enter a number :"))
num2=int(input("Enter a number :"))
num3=int(input("Enter a number :"))

if num1>num3:
    if num1>num2:
        print("num1 is the largest number")
    else:
         print("num2 is the largest number")
elif num2>num1:
    if num2>num3:
        print("num2 is the largest number")
    else:
         print("num3 is the largest number")
elif num3>num2:
    if num3>num1:
        print("num3 is the largest number")
    else:
         print("num1 is the largest number") 

else:
    print("All numbers are equal")



# Check if a number is divisable by both 5 and 11

num1=int(input("enter a number:"))
if num1%5==0 :
    if num1%11==0 :
         print("num1 is divisable by both 5 and 11")
    else :
          print("num1 is divisable by 5 ")
elif num1%5!=0:
     if num1%11!=0:
          print("num1 is not devisable by 5 and 11")
     else:
          print("num1 is devisable by both 5 and 11")





# check if a number lies in the range 10 - 50

num1=int(input("Enter a number :"))
if num1>=10:
     if num1<=50:
          print("The number lies in the range of 10 and 50")
     else :
          print("The number not lies in the range of 10 and 50")

elif num1<=10:
     if num1<=50:
          print("The number is not lies in the range of 10 and 50")

# Check if a year is leap year

leap_year=int(input("Enter the year :"))
if leap_year%4==0: 
    if leap_year%100!=0:
       print("It is leap year")
    else :
        print("It is not a leap year")
elif leap_year%4!=0:
     if leap_year%100!=0:
        print("It is not leap year")




# Check check if a number is popsitive and even
num=int(input("Enter a number : "))
if num>=0:
      if num%2==0:
            print("a number is positive and even")
      else :
            print("a number is not positive and even")
elif num<=0:
      if num%2==0:
            print("a number is not positive and even")
     







