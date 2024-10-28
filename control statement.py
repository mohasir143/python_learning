#1      -      1 to 10   - when the number is stop at 5.

# for i in range(1,11):
#     if  i%6==0:
#      break
#     print(i)
    

#2      -       first negative number in list.

# my_list=[-8,8,45,-36,5,-2,6,-9,-66,1]

# for i in my_list:
#     if i<0:
#       print(i)
#     break
  

#4       -       print number 1 to 10,skipping 5.

# for i in range(1,11):
#     if i%5==0:
#       continue
#     print(i)


#5       -       print only even numbers from 1 to 10.

# for i in range(1,11):
#    if i%2==0:
#       print(i)
     

#6       -        use list and skip negative numbers.    

# my_list=[-45,8,90,-5,-1,90,54,-60]
# for i in my_list:
#    if i<0:
#       continue
#    print(i)


#7       -          Print characters of a string, skipping vowels
# name="birthday party"
# for i in name:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#        continue
#     print(i)


#8       -            numbers from 1 to 20, but skip multiples of 3.

# for i in range(1,21):
#     if i%3==0:
#      continue
#     print(i)
   

#9        -           Iterate over a list and use pass for future implementation.

# my_list=[8,88,-12,54,7,-81,53]
# for i in my_list:
#     if i<=0:
#         pass
#     print(i)

#10        -          Iterate over numbers from 1 to 10, skip 5 and stop at 8.

# for i in range(1,11):
#     if i%5==0 :
#        continue
#     elif i%8==0:
#        break
#     print(i)


#11       -         print only even number 1,10 and odd number in pass method.

# for i in range(1,11):
#    if i%2!=0:
#       print(i)
#    elif i%2==0:
#      pass
   

#12        -        iterate the over list print positive or negative ,stop at 0.

# my_list=[-9,8,9,24,0,14,-67,-75,100] 
# for i in my_list :
#    if i<0:
#        continue
#    elif i==0:
#     break
#    print(i)


#13        -         skip the first half of a list and process the second half use pass.

# my_list=[89,33,76,91,25,87] and [78,45,76,12,67]
# for i in my_list:
#     print(i)
#     pass

#14        -         input from user like number untill user enter zero after that have to print the product of numbers.

product=1
while True:
    number=int(input("Enter a number : "))
    if number!=0:
        product=product*number
    else:
       break
print(product)



#15       -          input from user like number untill enter negative number after that have to print the sum of numbers.


# sum=1
# while True:
#    number=int(input("Enter a number : "))
#    if number<0:
#       break
#    sum=sum+number
# print(sum)