#Match case defined to use match and case condition.

#check a day as weekday or weekend.
# day=input("Enter a day :")
# match day.lower():
#       case "monday" | "tuesday" | "wednesday" | "thursday" | "friday" :
#            print("It is week day")
#       case "saturday" | "sunday" :
#            print("It is weekend day")
#       case _:
#            print("Write the correct day")


#print a no of days in month.

# month=input("Enter a month : ")
# match month.upper():
#     case "JANUARY" | "MARCH" | "MAY" | "JULY" | "SEPTEMBER" | "OCTOBER" | "DECEMBER" :
#         print("It is 31 days of the month")
#     case "APRIL" | "JUNE" | "AUGUST" | "NOVEMBER" :
#         print("It is 30 days of the month")
#     case "FEBRUARY" :
#         print("It is 28 days or 29 days of the month")
#     case _:
#         print("Write the correct month")


# #enter the vowels or consonent.
letter=input("Enter the letter :")
match letter.lower():
    case "a" | "e" | "i" | "o" |"u" :
        print("It is vowels")
    case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z" :
        print("It is consonent")
    case _:
        print("Enter a correct letter")


#grade by marks
# num=int(input("Enter a number:"))
# match num:
#     case num if num>=90 and num<=100 :
#         print("It is A grade")

#     case num if num>=70 and num<=89 :
#         print("It is B grade")

#     case num if num>=60 and num<=69 :
#         print("It is C grade")

#     case num if num>0 and num<=59 :
#         print("It is Fail ")
#     case _:
#         print("Enter your correct mark")

#season name based on month name.

#december, January, February (winter), March, April, May (spring), June, July, August (summer), September, October, November (autumn).
# season=input("Enter a seson :")
# match season:
#     case "december" | "january" | "february" :
#         print("IT is WINTER season")
#     case "march" | "april" | "may" :
#         print("It is a SPRING season")
#     case "june" | "july" | "august" :
#         print("It is SUMMER season")
#     case "september" | "october" | "november" :
#         print("It is a AUTOMN season")
#     case _:
#         print("Please enter correct month")


#Positive or negative.
# num=int(input("Enter a number: "))
# match num:
#     case num if num>0:
#         print("IT is positve")
#     case num if num<0:
#         print("It is negative")
#     case _:
#         print("It is as Zero")


#range of number.

# number=int(input("Enter a number : "))
# match number:
#     case number if number>10 and number<=50:
#         print("It is range number between 11 - 50 ")
#     case _:
#         print("It is not range number between 11-50")




