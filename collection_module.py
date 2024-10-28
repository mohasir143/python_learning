# The collection module is both of packages,this means library
# It is full using with dictionaries e.g{a:1,b:2,c:3}key pair values
import collections

#1:(counter dictionary)
# mylist=["a","b","z","meow",2,2,2,"a","b","a","meow"]
# print(collections.Counter(mylist))                           It is set of key values

#2:(ordered dictionary)
# mylist=collections.OrderedDict()
# mylist["a"]=1
# mylist["b"]=2                                                 #It is set of ordered using this function
# mylist["z"]=3
# mylist["meow"]=4        
                                                                
# for i,j in mylist.items():                                    #Then iterate one by one key pair values
#     print(i,j)

# mylist.pop("b")                                                #The pop is remove method 
# print(mylist)

# mylist["b"]=2                                                 #It is not change anything ,extra add is last come
# print(mylist)                                                 #([('a', 1), ('z', 3), ('meow', 4), ('b', 2)])

#3:(default dictionary)

# res=collections.defaultdict(int)
# mylist=[66,5,75,32,4,53,53,5,5,5,66,"mohasir"]
# for i in mylist:
#   res[i]+=1                                                       #This is also same as counter method
# print(res)

#4:(chainmap dictionary)

# emp_1={"name":"sanjay"}
# emp_2={"name":"racky"}
# emp_3={"name":"danish","age":52}
#                                                              #It is many set divided into one set and sepearate in one set
# chainmap=(emp_1,emp_2,emp_3)                                 #({'name': 'sanjay'}, {'name': 'racky'}, {'name': 'danish', 'age': 52})
# print(chainmap)

#5:(namedtuple dictionary)

# employee=collections.namedtuple("employee",["name","age","course"])
# res=employee("mohasir",55,"Bca")                              #It is used with set of key and value to used it this module
# print(res)

#6:(deque module)

# solve=collections.deque([45,2,12,7,90])                        #It is add left and right ,remove left right is used module                                               
# solve.appendleft(45)
# solve.popleft()
# print(solve)

