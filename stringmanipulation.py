# manipulation

# college="raak arts and science"

# print(college[5])                           #index number start with 0.  (Slicing)

# print(len(college))                         #length number is start with 1.


                       # Positive number

# print(college[0:4])                         #It is start to end used as number index.

# print(college[14:])                         #It is colomn to accces to full letters.


                       # Negative number 
 
# print(college[-8:])                         #It is reverse to work on it .

# print(college[-21:-18])                     #It is reverse to easily finding.


                      #python format and concate

# fname="mohamed"
# lname="mohasir" 
# result=fname+" "+lname                          #It is string + string add.
# print(result)


# name="The world is calculated by {know} Age"    # #It is string to change particular word to integer with {=}
# print(name.format(know = 18))                   


                       #Python string concept

# print(college.capitalize())       #It is used as uppercasease(capital letter) first characters Or using upper().

# print(college.casefold())         #It is used as lowercase(small letter) all characters Or using lower().

# print(college.strip())            #It is remove in front space gap.

#print(college.center(50))          #It is move in front space gap.    
 
# print(college.count("s"))         #It is find out letter how many times used there letters.

# print(college.find("k"))          Z#It is count the words/letter using string quotation Or it using index().

# print(college.startswith("r"))    #It is starting word/letter True or False to find out.
 
# print(college.endswith("e"))      #It is ending word/letter True or False to find out.

# print(college.replace("r","p"))   #It is replace letters/word with comma and easil;y change it. 1st letteer type to change comma 2nd letter execute.

# print(college.split())            #It is single single words to describe with string .

# print(college.isalnum())          #It is only numbers and alphabets and not space include used as True.

# print(college.isalpha())          #It is only use alphabets and not space include used as True.
 
# print(college.isascii())          #It is always True because keyboard full of ascii values.

# print(college.isdecimal())        #It is only used as numbers Or isdigit() Or isnumeric().

# print(college.isspace())          #it is only space found as called True.

# print(college.isidentifier())     #It is only start with Capital Or Small letter Or underscore only and dont space using is called True.   

# print(college.title())            #It is heading all first letter using capital letter is called True.


# mytuple=("mohamed","college","coder")
# result="to".join(mytuple)         #It is used to join full words using string and dott with full value.
# print(result)
 

# num="56"  
# print(num.zfill(3))               #It is add extra zero from behind the number and also count values and add zero.   


# my_dict={65: 68}
# result="hello bysa"               #dowth
# print(result.translate(my_dict))



                                                   #project



#1             -           In a paragraph replace a “is” with “was” . then count no of “a” in a paragraph.


# para="There is something timeless about the natural world that connects deeply with our sense of self and place"

# print(para.replace("is","was"))
# print(para.count("a"))


#2             -           Get a input from user check its a Email Id

# name=input("Enter a name: ")
# print(name.endswith("@gmail.com"))


#3             -           Get a input from user also check  its valid password.

# password=input("enter a password")
# print(password.isalnum())


#4             -           Get input from user name & password its align with your previous data.throw a login successful message.otherwise its a Invalid input.

# name1="mohamed mohasir"
# password1="smileboy143"

# name=input("Enter a Name : ")
# password=input("Enter a password")

# if name==name1 and password==password1:
#     print("Login succesfull")
# else:
#     print("Invalid Input")


#escape characters - to hightlight specific string
# greeting="Welcome To  \"Ocean Academy\""                     #It is particular splitting words with marking with string using    { \"mohamed\" }
# print(greeting)






























