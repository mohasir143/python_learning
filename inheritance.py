# The inheritance is a two structures - Parent Class(Base) and Child Class(Derived).

# The inheritance as many types :  Single , Multiple , Multilevel , hierarchical and Hybrid Inheritance.


# Single Inheritance

# class Dad:
#    def Money(self):
#       print("Dad have Lot of Money.....")
# class Son(Dad):
#    def Bike(self):                                            #It is base to derived is called as single level Inheritance
#       print("Son have small Bike....")

# Family=Son()             
# Family.Bike()                            
# Family.Money()


# Multiple Inheritance

# class Dad:
#    def Money(self):
#       print("Dad have Lot of Money.....")

# class Mom:
#    def Food(self):
#       print("Mom have many foods....")                          #It has  Many Base class using One derived class use it.

# class Son(Dad,Mom):
#    def Bike(self):
#       print("Son have small Bike....")

# Family_1=Son()
# Family_1.Food()
# Family_1.Money()
# Family_1.Bike()    


# Multilevel Inheritance

# class Dad:
#    def Money(self):
#       print("Dad have Lot of Money.....")

# class Grandmother:
#    def Photos(self):
#       print("Grandmother have old photos")

# class Mom(Dad,Grandmother):
#    def Food(self):
#       print("Mom have many foods....")                            #It has Not linked with 1s base class but Working  with Derived class include 1base class also.

# class Son(Mom):
#    def Bike(self):
#       print("Son have small Bike....")

# Family_2=Son()
# Family_2.Food()
# Family_2.Photos()
# Family_2.Bike()
# Family_2.Money()


#Hierarchical Inheritance

# class Teacher:
#    def All_Books(self):
#       print("Teacher have many Books....")                    

# class Stud_1(Teacher):
#    def Book1(self):
#       print("Stud_1 have only Tamil Book ....")


# class Stud_2(Teacher):
#    def Book2(self):
#       print("Stud_2 have only English Book ....")                    #It is one Base class with many derived class used it.


# class Stud_3(Teacher):
#    def Book3(self):
#       print("Stud_3 have only Maths Book ....")


# Incharge=Stud_1()
# Incharge.Book1()
# Incharge.All_Books()

# Incharge=Stud_2()
# Incharge.Book2()
# Incharge.All_Books()

# Incharge=Stud_3()
# Incharge.Book3()
# Incharge.All_Books()



# Hybrid Inheritance


# class Teacher:
#    def All_Books(self):
#       print("Teacher have many Books....")                    

# class Stud_1(Teacher):
#    def Book1(self):
#       print("Stud_1 have only Tamil Book ....")
#                                                                      # It is All Inheritance has Used it

# class Stud_2(Teacher,Stud_1):
#    def Book2(self):
#       print("Stud_2 have only English Book ....")        


# class Stud_3(Stud_2):
#    def Book3(self):
#       print("Stud_3 have only Maths Book ....")


# #Task - 1
# # 1.Create a Person class and a Student class that inherits from Person.

# class Person:
#    def Job(self):
#       print("Person have Job...")

# class Student(Person):
#    def Degree(self):
#       print("Student have Degree Certificate...")

# Life=Student()
# Life.Degree
# Life.Job

# Task - 2
# 2.Create a class Animal, a Mammal class that inherits from Animal, and a Dog class that inherits from Mammal.


# class Animal:
#    def Food(self):
#       print("Animal have Many Foods.....")

# class Mammal(Animal):
#    def Swimming(self):
#       print("Mammal has Swimming.....")

# class Dog(Mammal):
#    def Running(self):
#       print("Dog has Running.....")

# Animals_1=Dog()
# Animals_1.Running()
# Animals_1.Swimming()
# Animals_1.Food()

# Animal_2=Mammal()
# Animal_2.Food()
# Animal_2.Swimming()

# Task - 3
# 3.Create a class Vehicle and two classes Car and Bike that inherit from Vehicle.

# class Vehicle:
#    def Petrol(self):
#       print("Vehicle have Petrol.....")
# class Bike(Vehicle):
#    def Long_Distance_Miloege(self):
#       print("It has Long Distance Miloege  .....")
# class Car(Vehicle):
#    def Short_Distance_Miloege(self):
#       print("It has Short Distance Miloege")

# Vehicle_1=Bike()
# Vehicle_1.Petrol()
# Vehicle_1.Long_Distance_Miloege()

# Vehicle_2=Car()
# Vehicle_2.Petrol()
# Vehicle_2.Short_Distance_Miloege()

# Task - 4
# 4.Create a Teacher class, a Student class that both inherit from Person, and an Assistant class that inherits from both.

# class Teacher():
#    def Lesson(self):
#       print("Teacher has Take Life of Lessons.....")

# class Student():
#    def Education(self):
#       print("Student have Education Knowledge.....")

# class Person(Student,Teacher):
#    def Idea(self):
#       print("Person have some great ideas.....")  

# class Assistant(Person):
#    def Helping_to_understand(self):
#       print("Assistant Have helping To understand easy method .....")


# Work_1=Person()
# Work_1.Lesson()
# Work_1.Education()
# Work_1.Idea()

# Work_2=Assistant()
# Work_2.Lesson()
# Work_2.Education()
# Work_2.Idea()
# Work_2.Helping_to_understand()

# Work_3=Student()
# Work_3.Education()


# SuperClass Keywords

# Task - 1

# 1.Class a having  display function and Constructor class b having  display function create obj for a. 
# Create a obj for b and access a constructor by using super keywords.

# class a:
#    def __init__(self,name,salary,place):
#         self.name=name
#         self.salary=salary
#         self.place=place

   # def getfun(self):
   #    print("Name : ",self.name)
   #    print("Salary : ",self.salary) 
   #    print("Place : ",self.place)      

# class b(a):
#    def __init__(self,name,salary,place,job):
#        super().__init__(name,salary,place)
#        self.job=job
   
#    def getfun(self):
#        super().getfun()
#        print("Job : ",self.job)

# object_1=b("Mohasir",1000,"Ooty","Cricket")
# object_1.getfun()

# Task - 2
# 2. Class c having display function have to inherit class a and class b constructor.

# class a:
#    def __init__(self,name,age,place):
#       self.name=name
#       self.age=age
#       self.place=place

#    def getfun(self):
#       print("Name : ",self.name)
#       print("Age : ",self.age)
#       print("Place : ",self.place)

# class b:
#    def __init__(self,name,size):
#        self.name=name
#        self.size=size

#    def getfun(self):
#       print("Name : ",self.name)
#       print("Size : ",self.size)

# class c(a,b):
#    def __init__(self,name,age,place,size,work,members):
#       super().__init__(name,age,place)
#       b.__init__(self,name,size)
#       self.work=work
#       self.members=members
   
#    def getfun(self):
#       super().getfun()
#       print("Size : ",self.size)
#       print("Work : ",self.work)
#       print("Members : ",self.members)

# object_2=c("mohasir",21,"Chennai","L_Size","IT Field",10)
# object_2.getfun()















