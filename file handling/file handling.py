# The file handling is using with 4 types 
#  MODE -   create(x) , write(w) , append (a), read (r)  and it is addition of txt(t) and binary number(b)images.
#  The parametres is two types(filename and mode)

import os

# file=open("new.txt","x")          #It is create method open file Using Create(x)

file=open("new.txt","w")
file.write("Hi everyone, welcome to the Ocean Academy \n")
file.write("So, we are all are very specially trained \n")               #It is write the words in new file used with write(w).
file.close()


file1=open("new.txt","a")
file1.write("Why we choose full stack? \n")
file1.write("Because it may very helpful of the future generation \n")     #It is append method used (a) and using with the help of write method 
file1.write("Mostly working companies do it in the full stack \n")         #It is  used ( \n - next line moving) 
file1.write("so all are learning full stack web develpoment \n")
file1.close()


file3=open("new.txt","r")
# file3.read()
print(file3.read())                                                      #It is just read only
print(file3.readline())

for i in file1():
    print(i)


