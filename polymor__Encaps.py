# Polymorphism
# The Polimorphism has many Forms


# def Multi (a,z):
#    return a*z                                            # It is only single attribute used
# print(Multi(2,2))

# def Multi (a,z,e=5):
#    return a*z*e                    
# print(Multi(2,2,2))                                      # It has one function to extra form


# class Private_College:
#     def Facilities(self):
#         print("It has high facilities....")
#     def Percentage(self):
#         print("All Students are Full Percentage Marks....")
#     def Extra_activity(self):
#         print("College Has Extra games are provided....")

# class Government_College(Private_College):
#     def Facilities(self):
#         print("It has low facilities....")
#     def Percentage(self):
#         print("They Only 50 percent Pass Mark.....")

# College_1=Government_College()
# College_1.Facilities()                                  # It has calling but working the current function method only printed
# College_1.Percentage()
# College_1.Extra_activity()



# Encapsulation

# It has using the function in three method
# Public ,Protected "_" ,Private "__" 


# Public is normal function to write
# Public

# class Company:
#     def __init__(self,name,id,subject):
#         self.name=name
#         self.id=id
#         self.subject=subject

#     def getfun(self):
#         print("Name =",self.name)
#         print("Id =",self.id)
#         print("Subject =",self.subject)

# Job=Company("Rogan",25,"Science")
# Job.getfun()



# # Protected is same as set concept to access the value
# # Protected

# class Company:
#     def __init__(self,name,id,subject):
#         self._name=name
#         self._id=id
#         self._subject=subject

#     def getfun(self):
#         print("Name =",self._name)
#         print("Id =",self._id)
#         print("Subject =",self._subject)

# Job_1=Company("Mohasir",20,"Python")
# Job_1._subject="Maths"                          #It is same as Set Method But Using "_"underscore method in self._ used it.
# Job_1.getfun()                            



# # Private
# # Not Access Anyone

# class Company:
#     def __init__(self,name,id,subject):
#         self.__name=name
#         self.__id=id
#         self.__subject=subject

#     def getfun(self):
#         print("Name =",self.__name)
#         print("Id =",self.__id)
#         print("Subject =",self.__subject)
    
# Job_2=Company("Aravinth",22,"Statistics")
# Job_2.__name="Aravindh"                                  #It is private so not access anyone only they use already function method
# Job_2.getfun()



# Task - 1
# Create a function which acts as two arguments function and also three arguments function

# def Addition(e,f,g=5):
#    return e+f+g               
# print(Addition(2,2,2))   


# Task - 2
# Create a base class called shape withe method area that return 0 .
# create a derived class called rectangle that inherit from shape and overrides the area method to 
# calculate and return the area of a rectangle.


# class shape:
#     def area(self):
#         return 0
    
# class rectangle(shape):
#     def area(l,b):
#         return l*b
# Obj=rectangle() 
# Obj.area() 


# 2.create a base class called person with constructor that takes a name as a parameter .
#  Create a derived called student that inherits from  person has constructor that takes a parameter called grade. 
# Write a method in student to display name and grade of student . Use super keywords to achieve this.





# 3..create a base class called vehicle with a method start that print " vehicle started" 
# create a derived class called car that inherits from vehicle and overrides the start method to print " car started”.

# class vehicle:
#     def start(self):
#         print("vehicle started.....")

# class car(vehicle):
#     def car(self):
#         print("car started.....")

# objve=car()
# objve.start()

# 4.create a base class called employee with properties name and salary . 
# Create a derived class called manager that inherits from employee and adds a property department .
#  Write a method in manager to display the name , salary , and department of the manager.


# class employee:
#     def _init_(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def getfunc(self):
#         print("name:",self.name)
#         print("salary:",self.salary)

# class manager(employee):
#     def _init_(self,name,salary,department):
#         super()._init_(name,salary)
#         self.department=department

#     def getfunc(self):
#         super().getfunc()

# obj_1=manager("mohasir",1000",java")
# obj_1.getfunc()


# 5.Create a class called animal with a sound function that prints "Animal makes sounds" .
# create a derived class called dog that inherits from animals and overrides the sounds methods to print "dog barks " .
# create a another function derived class bird that inherits from animal and overrides sound method to print " birds print"


# class animal:
#     def sound(self):
#         print("animals make sound..")

# class dog(animal):
#     def sound(self):
#         print("dog barks..")

# class bird(animal):
#     def sound(self):
#         print("birds print")

# # obj_2=dog()
# # obj_2.sound()


# obj_3=bird()
# obj_3.sound()



