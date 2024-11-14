# closure function is called as inner and outer function that means nested function

# def outer():
#     def inner():
#         print("hi")
       
#     return inner
# print(outer())


# decoraters function

# def decor_outer(students):
#     def decor_inner():
#        print("Welcome to the raak college")
#        students()
#        print("Thanking you for your wonderful joining this college")
#     return decor_inner
    

# @decor_outer
# def college():
#     print("The college is very strict and enjoyful")
# college()


# task-1

# review=int(input("enter The review of rating "))

# def outer(follow):
#     def inner():
#         print("welcome mohamed !")
#         follow()
#         if review<=10 and review>0:
#           print("Rating for our company :",review)
#         print("Congratulation ,Mohamed all the best for your future endoverous from Zoho")
#     return inner

# @outer
# def company():
#     print("Thanks for entering the Zoho company ")
# company()