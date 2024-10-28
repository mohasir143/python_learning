# dictionary
# It is ordered , changebale and not allowed duplicate and key pair value items

mydict={"name":"mohasir","Age":19,"course":"python",}
# print(mydict)

# constructor - dict

# mydict=dict(name="mohasir",age=19,,course="python")
# print(mydict)


# print(mydict["name"])                 -        It is key name of found the value name.             
        
# print(mydict.get("course"))           -        It is also same becausee it has find out get name(eg)mohasir,19,python.

# print(mydict.values())                -        It is provide all values in single print is called as value.

# print(mydict.keys())                  -        It is finding key name(eg)name,age,course

# print(mydict.items())                 -        It is full of working key values pair pair of output there


# mydict["course"]="ai"                 -        It is change easily method    
#                
# mydict["interset"]="cricket"          -        It is add extra dictionary

# mydict.setdefault("sno",2)            -        It is automatically add items in last.

# mydict.update({"class":bca})          -        It is update easily or insert(same method)
# print(mydict)


# mydict.pop("name")                    -        It is remove a item with single pop.

# mydict.popitem()                      -        It is automatically remove last one item.
# print(mydict)

 
# for i ,j in mydict.items():           -        It is use teo varriables and items is used as called pair value output.
    # print(i,j)



# nested dictionary

student={"student1":{"name":"umar","age":19, "course":"b.com"  },
         "student2":{ "name":"mohamed", "age":21,  "course":"python" },
         "student3":{"name":"apsal",  "age":20, "course":"bunk"}}

# print(student)                        -         It is full of student dictionaries in differntiate in one student variables.

# print(student["student3"])            -         It is student inside find out and one student only output there.
 
# for i ,j in student.items():
#     print(i)
#     for l in j:
#         print(l,j[l])

# student1={
#         "name":"aravinth",
#         "age":20,
#         "course":"python"
#     }

# student2={
#         "name":"mohamed",
#         "age":21,
#         "course":"python"
#     }
# student3={
#         "name":"selena",
#         "age":20,
#         "course":"music"
#     }

# student={
#     "student1":student1,
#     "student2":student2,
#     "student3":student3
# }

# print(student)
# for i ,j in student.items():
#     print(i)
#     for l in j:
#         print(l,j[l])