# The regular expression is a module use.
import re

obj="The life is full of miracles"
# Meta characters

# []- It is set of characters ,for example[a-z1-9]. 
# \d - It is digits that means all numbers
# .  - It is worked as (.) ex (hel.o) only one characterrs used in the dotter line
# ^ - It is worked as start with (^The) Then if condition to write this method and print
# $ - It is worked as End with with ($miracles) Then if condition to write this method and print
# * - It is working with * example(he.*o) hellllloo any characters to add and it is also using (heo)
# + - It is on or more adding characters but not use(he.+o)heo.
# ? - It is one character or zero characters only using.
# {} - It is exactly how many letter used called used it (he.{2}o)
# | - It is ( or )used method with if condition.

#Special sequences 
# \A - It is used as same way start method.
# \Z - It is same as end with method 
# r\bcat - It is begining word find out the sentences.
# r"cat\b" - It is end word find out the sentences.
# r"\Bcat" - It is not begining word used there
# r"cat\B" - It is not ending word used there.
# \D - It is not accept the numbers and blank it then one by one letter used it.
# \s - It is find the space and condition write.
# \S - It is not find the space and remove and condition write.
# \w - It is only using 0-9 a-z and _underscore
# \W - It is (a-z or 1-9) without using all using symbols and space etc..

# set 
# [arn]- It is acces only arn in the sentences using
# [a-i] - It is only access a to i characters
# [^arn] - It is start with arn letter remove it
# [1-9] - It is only using 1 to 9 numbers using
# [12345] - It is correct only 1 2 3 4 5 numbers.
# [0-6][0-7] - It is 67 used as combine and double numbers are accepted ex.11:45
# [a-zA-Z] - IT is uppercase and lowecase also accept it
# +  - It is + symbol used in the sentence right