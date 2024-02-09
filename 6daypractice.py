'''INHERITANCE CONCEPT PROGRAMMING IN PYTHON'''

'''SINGLE LEVEL INHERITANCE'''

# class Faulty:
#     def __init__(self, f_name, department, f_id):
#         self.f_name = f_name
#         self.department = department
#         self.f_id = f_id
        
#     def print_info(self):
#         print('faulty information=', self.f_name, self.department, self.f_id)

# obj = Faulty("Ashish", "computer_science",1001)
# obj.print_info() 

# class CSE(Faulty):
#     pass
# obj = CSE("Jyoti_mam","computer_science",1002)
# obj.print_info

# class Me(Faulty):
#     pass
# obj.Me("xyz","computer_science",1003)
# obj.print_info

'''Multi-level inheritance'''

# class college:
#     def college_name(Self):
#         print("Modern college")

# class student(college):
#     def student_info(Self):
#         print("Nmae: Prashant Jha")
#         print("Branch: Mechanical")
        
# class exam(student):
#     def subject(self):
#         print("Subject1: Design enigneering")
#         print("Subject2: Maths")
#         print("Subject3: C-language")
        
# obj = exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

'''Multiple inheritance'''

# class subjectmarks:
#     Maths = int(input("Enter the paper marks of math: "))
#     DE = int(input("Enter the paper marks of DE: "))
#     C = int(input("Enter th esunject marks of C: "))
#     English = int(input("Enter the subject marks of english: "))
    
# class practicalmarks:
#     Cpartical = int(input("Enter practical marks of C Language: "))
    
# class result(subjectmarks,practicalmarks):
#     def total(self):
#         if self.Maths>=40 and self.DE>=40 and self.C>=40 and self.English>=40 and self.Cpartical>=20:
#             print("PASS")
#         else:
#             print("FAIL")
            
# obj = result()
# obj.total()

'''WAP to get below output - class, object, constructor, static/instance variable (concept should include in code)

# enter username : prashant
# enter password : prashant

# logic successfully

# enter the name : prashant
# enter the college name : DU
# enter the clss name : final year
# enter the roll no : 1001

# choose any branch for giving exam

# 1. mechnical Eng 
# 2. it 
# 3. cs 
# 4. civil 

# enetr ypu choice 

# 1. 1st sem 
# 2. 2nd sem 
# enter ypur sem nuber 
# enter you choice 
# math 

# do you want to put examination marks enter yes/no 

# enetr yes/no : yes '''

# class login:
#     username = input("Enter your USERNAME: ")
#     password = input("Enter your PASSWORD: ")
#     print("\nYou have LOGIN successfully\n")
#     print("################################\n")
    
# class studentdetails:
#     studentname = input("Enter your name: ")
#     collegename = input("Enter your college name: ")
#     branch = input("Enter your branch name: ")
#     rollno = int(input("Enter your rollno: "))
#     print("\n################################")
    
# class branchselection:
#     def computer_engineering (self, MATHS, PHYSICS, CHEMISTRY, CPP, PCE, ED):
#         self.MATHS = MATHS
#         self.PHYSICS = PHYSICS
#         self.CHEMISTYR = CHEMISTRY
#         self.CPP = CPP
#         self.PCE = PCE
#         self.ED = ED

#     def switch_operation(self, operators, MATHS, PHYSICS, CHEMISTRY, CPP, PCE, ED):
#         operators = {
#             'computer_engineering' : self.computer_engineering
#         }    

######################################################################################################################

'''POLYMORPHISM IN PYHTON'''
# Compile time - TYPE of POLYMORPHISM
# operator , method and constructor overloading (python dont support all of them, ONLY SUPPORT OPERATOR OVERLAODING)

# RUNTIME - TYPE of POLYMORPHISM
# overloading can be acheived theought functin and contruction overloading (support - function and constructor)

# Example of POLYMORPHISM

# class principle:
#     def role(self):
#         print("I am managing all activity of college")
        
# class dean:
#     def role(self):
#         print("dean = i am decision person")
        
# class hod:
#     def role(self):
#         print(" hod = i have the responsibility of teachers and student")  
        
# class faculty:
#     def role(self):
#         print("faculty = i have to complete syllabus successfully")
        
# def function(obj):
#     obj.role()
# campus = [principle(),dean(),faculty()]
# for obj in campus:
#     function(obj)

###############################################################

'''hasattr() is FUNCTION solve ATTRIBUTE ARROR - notes''' 

###############################################################

# class deposit:
#     def __init__(self, cash):
#         self.cash = cash

# d1 = deposit(1000)
# d2 = deposit(2000)
# print(d1+d2)                      #TypeError: unsupported operand type(s) for +: 'deposit' and 'deposit'


# class deposit:
#     def __init__(self, cash):
#         self.cash = cash
        
#     def __add__(self,other):             # __add__ - (used function to addition)
#         return self.cash + other.cash

# d1 = deposit(1000)
# d2 = deposit(2000)
# print(d1+d2) 

###############################################################

# class arithmetic:
#     def add (self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add (self,a,b,c):     #TypeError: arithmetic.add() missing 2 required positional arguments: 'b' and 'c' 
#         print(a+b+c)
        
# obj = arithmetic()
# obj.add(10)
# obj.dd(10,20)
# obj.add(10,20,30)

'''OVERLOADING EXAMPLE PROGRAM'''

# class rbi:
#     def homeloan_ROI(self):
#         print("home loan rate of interest = 7.5%")
        
#     def carloan(self):
#         print("car loan rate of interest = 8%")
    
# class sbi(rbi):
#     def homeloan_ROI(self):
#         print("home loan of rate of interest = 6.5%")

# obj = sbi()
# obj.homeloan_ROI()
# obj.carloan()

###############################################################

'''SUPER METHOD'''

# class rbi:
#     def homeloan_ROI(self):
#         print("home loan rate of interest = 7.5%")
        
#     def carloan(self):
#         print("car loan rate of interest = 8%")
    
# class sbi(rbi):
#     def homeloan_ROI(self):
#         super().homeloan_ROI() # by super method we ca access the parent class property
#         print("home loan of rate of interest = 6.5%")

# obj = sbi()
# obj.homeloan_ROI()
# obj.carloan()

###############################################################

'''ABSTRACTION IN PYTHON'''

# Python does not support default abstraction
# a class which contains one or more abstract methods is called an abstract class.
# an abstract method is method that has a declearation but does not have an implementation
# when to use - while we are designing large funtion units we use an abstract class
# you ca define a common application program API for a set of sub-classes

# EXAMPLE 

# from abc import ABC, abstractmethod
# class irctc(ABC):
#     @abstractmethod
#     def bookticket(self):
#         pass

# class makemytrip(irctc):
#     def bookticket(self):
#         print("================================================")
#         print("             welcome to makemytrip.com          ")
#         source = input("        Enter a source station name        ")
#         destination = input("Enter a source station name:       ")
#         date = input("             Enter date: ")
#         print("=================================================")
        
# class goibibo(irctc):
#     def bookticket(self):
#         print("=================================================")
#         print("             welcome to goibibo             ")
#         source = input("       Enter a source station name     ")
#         destination = input("Enter a source station name: ")
#         date = input("             Enter date:            ")
#         print("=================================================")

# class yatra(irctc):
#     def bookticket(self):
#         print("=================================================")
#         print("             welcome to yatra             ")
#         source = input("       Enter a source station name     ")
#         destination = input("Enter a source station name: ")
#         date = input("             Enter date:            ")
#         print("=================================================")

# m = makemytrip()
# m.bookticket()       

# g = goibibo()
# g.bookticket()
   
# y = yatra()
# y.bookticket()