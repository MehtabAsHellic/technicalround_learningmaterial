'''CLASSS (OOPL) - CONCEPTS'''

# class Student:
#     roll_number = 101
#     num1 = 50
#     num2 = 100
    
#     def add(self):
#         print(self.num1+self.num2)
#         self.name = input ("Enter name: ")
#         print(self.name)

# obj = Student()
# obj.add()
# print(obj.roll_number)

'''object creation and assign memeory through constructor'''

# class Hod:
#     def __init__(self) -> None:
#         self.name='salman khan'
#         self.age = 53
#         self.empid = 1001
        
#     def info(self):
#         print("My name is: ",self.name)
#         print("My name is: ",self.age)
#         print("My emp id: ",self.empid)

# obj = Hod()
# obj.info()

'''parameterized constructor'''

# class Hod:
#     def __init__(self,name,age,rollno) -> None:
#         self.name=name
#         self.age = age
#         self.empid = rollno
        
#     def info(self):
#         print("My name is: ",self.name)
#         print("My name is: ",self.age)
#         print("My emp id: ",self.empid)

# obj = Hod('Arjun',45,101)
# obj.info()

'''INSTANCE variable'''

# class New:
#     def __init__(self):
#         self.a=10

# obj1 = New()
# obj2 = New()
# obj3 = New()


# class NewClass:
#     def __init__(self) -> None:
#         print("my name is contructor and i always execute first")
        
#     def show(self):
#         print("welcome to class level programming")
        
# obj = NewClass()
# obj.show()
# obj2 = NewClass()
  
'''declaring instance variable inside a constructor by using self variable'''
    
# class Student:
#     def __init__(self):
#         self.s_name = 'prashant'
#         self.l_name = "jha"
#         self.s_rollno = 101 
#         self.branch = 'CS'
#         self.s_mb = 0000000000000

# obj = Student()
# print(obj.__dict__)  

'''getdata concept program'''
   
# class Student:
#     def __init__(self):
#         self.s_name = 'prashant'
#         self.s_rollno = 101 
#         self.branch = 'CS'
    
#     def getdata(self):
#         self.s_mb = 2828282828

# obj = Student()
# obj.getdata()
# print(obj.__dict__)
     
'''declaring instance variable outside a class by using object'''

# class Student:
#     def __init__(self):
#         self.s_name = 'prashant'
#         self.s_rollno = 101 
    
#     def getdata(self):
#         self.s_mb = 2828282828

# obj = Student()
# obj.getdata()
# obj.s_branch = 'CS'
# print(obj.__dict__)
        
'''accessing and deleting instance variable from the class'''

# class Student:
#     def __init__(self):
#         self.s_name = input("Enter your name: ")
#         self.s_rollno = 101 
    
#     def getdata(self):
#         self.s_mb = 2828282828

# obj = Student()
# obj.getdata()
# obj.s_branch = 'CS'
# del obj.s_rollno
# print(obj.s_name)
# print(obj.__dict__)       
       

# class Dog:
#     def __init__(self,name,height,weight,color):
#         self.name = name
#         self.height = height
#         self.weight = weight 
#         self.color = color
        
#     def barking(self):
#         print(self.name,"Dog is barking")

# d = Dog("dogname",12,20,"white")          
# print(d)
# d.barking()                                                              

###############################################################

'''Bank Account program'''

# class BankAccount:
#     def __init__(self, accountnumber, ownername, balance):
#         self.accountnumber = accountnumber
#         self.owername = ownername
#         self.__balance = balance #private information / data, by using __ (2 underscoll)
        
#     def depsitefunction(self,amount):
#         self.__balance = self.__balance + amount
        
#     def withdrawfunction(self,amount):
#         self.__balance = self.__balance - amount
#         if amount > self.__balance:
#             print("INSUFFICIENT AMOUNT")
#         else:
#             self.__balance -= amount
            
# account = BankAccount(6056,"useraccountname",10000000000000000)  
# account.depsitefunction(5000)
# account.withdrawfunction(5000) 
# print(account.owername)
# print(account.__balance) #AttributeError: 'BankAccount' object has no attribute '__balance'

###############################################################

'''Pokemon concept using program'''

# class Pokemon:
#     def __init__(self, name, health, level, attack, defence):
#         self.name = name
#         self.__health = health
#         self.level = level
#         self.__attack = attack
#         self.__defence = defence
        
#     def leveluppokemon(self):
#         self.level+=1
#         return self.level

# p = Pokemon("pokemonname",100,100,"fire and water","shield")
# print(p.leveluppokemon())

###############################################################

'''Question : 
MAKE A HUMAN CLASS
attributes : name, age, address
TRY TO ADD A PRIVATE PROPERTY 
also creae the methods'''

# class human:
#     def __init__(self, name, age, address,retionsstatus):
#         self.name = None
#         self.age = None
#         self.__address = address
#         self.__relationstatus = retionsstatus
        
#     def set_name(self, name):
#         self.name = name
    
#     def set_age(self,age):
#         self.age = age    
    
#     def set_status(self,status):
#         return self.__relationstatus = "status"
        
#     def greet(self,message = "HI"):
#         return self.name,"say",message
    
#     def get_status(self):
#         return self.__relationstatus
    
# h = human("nameone",20,"Mumbai City","status")
# h.set_name("nameone")
# h.set_age(26)
# h.greet()
# h.get_status()

###############################################################

'''STATIC AND INSTRANCE VARIABLE'''

# class college:
#     collegename = "Modern college"
#     def __init__(self):
#         self.studentname = 'studentname'
        
# principal = college()
# teacher   = college()
# accountant= college()

# print("principal = ",principal.collegename,"....",principal.studentname)
# print("teacher  = ",teacher.collegename,"....",teacher.studentname)
# print("accountant = ",accountant.collegename,"....",accountant.studentname)

# college.collegename="HBD"
# principal.studentname="newstudentname"

# print("principal = ",principal.collegename,"|",principal.studentname)
# print("teacher = ",teacher.collegename,"|",teacher.studentname)
# print("accountant=",accountant.collegename,"|",accountant.studentname)

###############################################################

'''THORY NOTES OF CONCEPTS'''

''''how do we access static variable ?'''
# inside instance method using self or class name 
# in a constructor using self or class name 
# in a class method using cls variable or class name 
# in a static method usign class name 
# outside of the class using ibject or class name 

'''how do we delete the static variable ?'''
# delete classname.staticvariablename
# inside classmethod we can use cls variable:
# del cls:staticvariablename
        
'''types of method inside a class '''
# 1. static method 
# 2. instance method 
# 3. class method

'''garbage collector program'''

# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())

###############################################################

# x1 = 1
# x2 = 2
# x3 = 3
# y1 = 1
# y2 = 4
# y3 = 6

# distance = ((x2-x1)*2+(y2-y2)*2)*2
# print(distance)