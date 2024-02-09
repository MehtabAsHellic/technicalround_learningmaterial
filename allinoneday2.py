# '''
# #1 PROBLEM 

# def function(x):
#     if len(x) < 3:
#         return(x)
#     elif x.endswith('ing'):
#         return(x + "ly")
#     else:
#         return(x + "ing")
    
# x = input("Enter the words : ")
# print(function(x))

# '''
# '''
# def count_digits_letter(sentence):
#     alpha_count = 0
#     dig_count = 0
#     result_list = []
    
#     for character in sentence:
#         if character.isalpha == True:
#             alpha_count = alpha_count + 1
#         elif ord(character) in range(48,58):
#             dig_count = dig_count + 1
        
#     result_list.append(alpha_count)
#     result_list.append(dig_count)
    
#     return result_list

# sentence="12345"
# print(count_digits_letter(sentence))

# '''


#PROBLEM 25

# def list_of_count(word_list):
#     count_list = []
#     for i in word_list:
#         count_list.append(len(i))
    
#     return count_list

# word_list=["COme","here"]
# print(list_of_count(word_list))
    

# text = "Python"
# print(text[0:2])
# print(text[-2:7])


# x = input("ENTER THE CHRACTER : ")
# if len(x) < 1:
#     print("-1")
# elif len(x) >= 2:
#         print(x[0:2]) + print(x[-2:])


# def calculate_net_amount(trans_list:list):
#     net_amount:int = 0;
#     for i in trans_list:
#         if i[0] == 'D':
#             net_amount = net_amount + int(i[2:])
#         else i[0] == 'W':
#             net_amount = net_amount - int(i[2])
        
#     return net_amount
            
# trans_list=["D:300","D:200","W:200","D:100"]
# print(calculate_net_amount(trans_list))

''' RANGE IN Python

DEFAULT - 0,5 '''

# print(list(range(1,15)))

# gen even number from 1 to 10
# print(tuple(range(2,10,2)))

# gen odd number from 3 to 20
# print(tuple(range(3,21,2))) 

# for i in range(3,21,2):
#     print(i)
    
# print multiplication table of 5

# print(tuple(range(5,55,5)))

# print reverse multiplication of 5

# print(tuple(range(50,4,-5)))

# print(tuple(range(-10,-71,-30)))

# use end for single line output
# for i in range(-10,-71,-30):
#     print(i, end= " ")

# s= "EUAIN" [:: -1]
# print(s)

# x = "EDUCATION"
# for i in range (0,len(x),2):
#     print(x[i], end = " ")

# s = "EDUCATION"
# for i in range (len(s)-1,-1,-1):
#     print(s[i], end = " ")

#square in all number in a list ([1,2,3,4,5,6,7,8,9]) [1,4,9,...........,81]

# s = "EDUCATION"
# for i in range (len(s)-1,1,-1):
#     print(i*i, end = " ")


# for i in number: 
#     squares.append(i**2) 
# print(squares) 
 

# ''' LIST COMPREHENSION '''

# [body-of-for- for-condition]

# print([i**2 for i in range(1,10)])


# DOUBLE EACH THE NUMBER IN A LIST COMPREHENSION

# print([2*i for i in range (1,10)])

# import math
# print([ round(math.pi, i) for i in range(1,6)])


#function and types of arguments 
# def findvoloum(length =1, width = 2, depth = 3):
#     print("length = ",length)
#     print("Width = ",width)
#     print("Depth = ",depth)
#     return length * width * depth
    
# positional arguments
# print(findvoloum(1,2,3))

# print(findvoloum(width=6,length=2,depth=7))  #if you give the value of the pre-define value above it updates to the given values.

# def func(fname, lname): #called function
#     print("hi",fname)
#     print("hi",lname)
# #func(fanme="firstname",lname="lastname") #calling function
# fname = input("enter first name")
# lname = input("enter the last name")
# func(fname,lname) #calling function

    
'''interview question'''

# what is function, types
# logic in project - function base logic - class base logic 
# argument - values that pass in funtion is argument
# work from office for better networking and shifting toward company
# project - application, role of your role, future perspective , logic design (in interview check your PROJECTS)
# tech citi - banglore, gurgam (cyfer citi)
# difference in list and tuple, when to choose list or tuple data-type
# unknow argument - interview / technical round
# degorator and generator - advance topic - started asking now in interview
# dynamic type language - but why ? (interview questions)
# 5/10 answering also good but quality of answering in interview matters, dont be slient just say "no" and go-forward
# RESUME - important for technical jobs - project, skill, internship
# good TECHNICAL ROUND always have a good chance to selection, (aptitude, english sometimes does not matter much)
# project is the learing in the JOB - best in product base company
# MODULE, PACKAGE, FUNCTION - IMPORTANT topics in DATA SCIENCE jobs
# HOW many way to export the fucntion,class,variable etc from one file to another in python or any language (interview questions)
# ( control statment in DSA is ALL ) nested for-loop, list, dictionary
# 1000 PROBLEM - different types












