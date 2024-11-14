# oops - object ooriented language 
# class & object

# class

# class goa:
#     name=""
#     age=0
#     travel=""

#     def beach(self):                                          #Class is a blueprint of object used for eg. tyres,door,engine(car)
#         print("Enoy your Day ......")
#     def park(self):
#         print("Play with childrens with happiely")

# # object

# objgoa=goa()
# objgoa.name="mohamed"                                       #Object is a features eg(brand)
# objgoa.age=20
# objgoa.travel="Bike"
# print(objgoa.name)                              #It is only one object class are reviewed


# self- It is current value represented
# object used with constructer method to used it full access

# class goa:
#     def __init__(self,name,age,travel):
#         self.name=name
#         self.age=age
#         self.travel=travel
#     def getfun(self):
#        print("Name:",self.name)
#        print("Age:",self.age)
#        print("Travel:",self.travel)
#     def setage(self,age):
#        self.age=age
#     def setAll(self,Name,Age,Travel):
#         self.name=Name 
#         self.age=Age
#         self.travel=Travel

# object1=goa("mohasir",24,"bike")
# object1.getfun()
# object2=goa("Aravinth",19,"flight")
# object2.getfun()
# object1.age=21
# object1.getfun()

# object2.setAll("aashik",19,"cycle")
# object2.getfun()



# Task -1

# class college:
#     def __init__(self,name,id,subject,marks):
#         self.name=name
#         self.id=id
#         self.subject=subject
#         self.marks=marks

#     def getfun(self):
#         print("Name =",self.name)
#         print("Id =",self.id)
#         print("Subject =",self.subject)
#         print("Marks =",self.marks)
#     def setmarks(self,marks):
#       self.marks=marks


# student1=college("Mohasir",20,"maths",49)
# student1.getfun()

# student1.setmarks(22)
# student1.getfun()


# student2=college("Aravinth",21,"maths",80)
# student2.getfun()


# student3=college("Lavanya",29,"maths",98)
# student3.getfun()

# student4=college("Rogan",26,"maths",60)
# student4.getfun()

# student5=college("Sumithra",23,"maths",45)
# student5.getfun()


# Task -2



# class laptop:
#     def __init__(self,price,processor,ram):
#         self.price=price
#         self.processor=processor
#         self.ram=ram
      

#     def getfun(self):
#         print("price=",self.price)
#         print("processor =",self.processor)
#         print("ram =",self.ram)
#     def setram(self,ram):
#       self.ram=ram


# Lenovo=laptop(45000,"Intelcore i9",128)
# Lenovo.getfun()

# HP=laptop(85000,"Apple M3",64)
# HP.getfun()

# Dell=laptop(98000,"AMD ryzen 5",8)
# # Dell.getfun()

# Dell.setram(16)
# Dell.getfun()

# Task -3

# class Kodaikanal:
#     def __init__(self,budget,members,place):
#         self.budget=budget
#         self.members=members
#         self.place=place
      

#     def getfun(self):
#         print("Budget =",self.budget)
#         print("Members =",self.members)
#         print("Place =",self.place)

#     def setAll(self,budget,members,place):
#       self.budget=budget
#       self.members=members
#       self.place=place
# Gt_Holidays_1=Kodaikanal(2000,1,"Pain falls")
# Gt_Holidays_1.getfun()

# Gt_Holidays_2=Kodaikanal(10000,5,"Waterfalls")
# Gt_Holidays_2.getfun()

# # Gt_Holidays_2.setAll(8900,6,"Munnar")
# # Gt_Holidays_2.getfun()

# Gt_Holidays_3=Kodaikanal(6000,3,"Guna Cave")
# Gt_Holidays_3.getfun()


