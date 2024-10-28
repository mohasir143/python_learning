#Tuple
#it is ordered and unchangeble and allow duplicates.

# Constructor - mytuple=tuple(("mohasir","fahad","apsal",245,8,"umar"))

# mytuple=("mohasir","fahad","apsal",245,8,"umar")
# print(mytuple)

# print(mytuple[5:])            -             index
# print(mytuple[-6:-2])         -             negative index

# mylist=list(mytuple)
# print(mylist)                # -             Its change to list
# mylist.append("Deva")
# print(mylist)                    
# mytuple=tuple(mylist)     #    -             It is change to tuple
# print(mytuple)




# mytuple=("mohamed","aravinth",1,3,True, False)
# mylist=[]

# for i in mytuple:
#     mylist.append(i)            -             It is tuple to change new folder of list

# print(mylist)

#updating

# mytuple=("mohamed","aravinth",1,3,True, False)
# newtuple=("aashik","syed")
# result=mytuple+mytuple             -            It is upddate of two tuples combines in 1 concept
# print(result)


# unpacking

# mytuple=("sanjay",78,"java","python","java","fullstack")
# (*name,age,course)=mytuple
# print(name)                         -         it is full of pairing to printing the problem and * from use - full line.
# print(age)
# print(course)

# loop

# Index
# for i in mytuple:
#     print(i)

# Length

# for i in range(len(mytuple)):
#     print(mytuple[i])

# result=mytuple.count("java")                       -      It is count value
# print(result)


# result=mytuple.index(78)
# print(result)                                      -     It is index value 0 to start
  

                                #    Task


# 1.add a new elements in tuple without using list constructor. I/P = (1,2,3,4,5)  O/P =(1,2,3,4,5,6,7,8,9,10).

# 2.add a new elements in tuple without using list constructor . I/P =(“python”,”C”,”C++”)
# O/P = (“python”,”C”,”C++”,”java”,”java script”,”node js”).

mytuple=(1,2,3,4,5)
mylist=list(mytuple)
print(mylist)

mylist=[]

for i in mylist:
    mylist.append()
    print(mylist)
mylist.append(6)
mylist.append(7)
mylist.append(8)
mylist.append(9)
mylist.append(10)
print(mylist)

result=mylist+mytuple
print(mylist)


