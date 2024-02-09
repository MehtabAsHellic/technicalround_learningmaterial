'''WITH STATEMENT - CONCEPTS'''
# with open ("mufile.text", "w") as f:
#     f.write("amit\n")
#     f.write("amish\n")
#     f.write("prashant\n")
#     print("file closed: ",f.closed)
    
# print("file closed: ", f.closed)

'''Data copying of image and creating new file and copying the data from the previous one to the new one - IMAGE'''
# f1 = open("pythonlogo.jpg","rb")
# f2 = open("newpythonlogo.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("New Image is availalbe with the name: ")

'''EXCEOTIONAL HANDLING PROGRAM/CODE'''

'''1'''
# a = int(input("number one: "))
# b = int(input("number one: "))
# print(a/b)

'''2'''
# Try: 
#     #statment
# Except:       (exceptional handling statment)
#     #statment

'''3'''
# a = int(input("number one: "))
# b = int(input("number one: "))
# try:
#     print(a/b)
# except:
#     print("can't divided by ZERO")

'''4'''
# try:
#     print(2/0)
# except ZeroDivisionError as message:
#     print("The description exception:", message)


'''5''' # ERROR ------ ValueError: invalid literal for int() with base 10: '*'
# a = int(input("number one: "))
# b = int(input("number one: "))
# print(a/b)

'''6 - MULTIPLY EXCEPT BLOCK CAN BE TAKEN''' # ERROR ------ ValueError: invalid literal for int() with base 10: '*'
# try:
#     a = int(input("number one: "))
#     b = int(input("number one: "))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("please ensure that you cant divide any number by zero:",message)
# except ValueError as message:
#     print("Enter only integer noumber=>",message)

'''7''' # ERROR ------ SyntaxError: default 'except:' must be last (FOR THE THIS ERROR used below method)
# try:
#     a = int(input("number one: "))
#     b = int(input("number one: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

'''8''' # ERROR ------ SyntaxError: default 'except:' must be last (INTERVIEW SOMETHING BE CLEAR)
# try:
#     a = int(input("number one: "))
#     b = int(input("number one: "))
#     print(a/b)
# except:
#     print("please ensure that you cant divide any number by zero:",message)
# except (ValueError , ZeroDivisionError ) as message:
#     print("Enter only integer noumber=>",message)

'''9''' 
# try:
#     a = int(input("number one: "))
#     b = int(input("number one: "))
#     print(a/b)
# except (ValueError , ZeroDivisionError ) as message:
#     print("Enter only integer noumber=>",message)
# else:
#     print("Everything is ok")

'''10''' 
# try:
#     a = int(input("number one: "))
#     b = int(input("number one: "))
#     try:
#         print(a/b)
#     except (ValueError , ZeroDivisionError ) as message:
#         print("Enter only integer noumber=>",message)
# except ValueError as msg:
#     print("msg")


'''QUESTION'''
# addvectors ([4,5],[1,2,3])
# [5,7,3]
# addvectors ([],[])
# []
###############################################################
# answer

# def addvectors(a,b):
#     for i in a :
#         print(12.index(i))

# addvectors([1,3,5],[2,4,6])        
    
# def addvector(l1,l2)->list[:]:
#     result = list()
#     for i in range(len(l1)):
#         result.append(l1[i]+l2[i])
#     return result                                       print(b[:5])

            
# print(addvector([1,3,5],[2,4,6]))
# print(addvector([],[]))    

###############################################################

# def sliptlist(list,numberoflist):
    
#     for i in range(numberoflist):
#         print(list[:numberoflist])
        
#     return list

# print(sliptlist([1,2,3,4,5,6,7,8,9,0],4))

###############################################################

# def pair(word1,word2):
#     if len(word1) == len(word2):
#         print(word2)

# print(pair("hello","hwllllllo"))
    
###############################################################

'''LIST QUESTION - 1'''

# def findmax(a):
#     x = max(a)
#     return(x)

# print(findmax([4,6,8,4,2,7,9,0,10]))

###############################################################

'''LIST QUESTION - 7'''

# def sumofallelement(a):
#     b = sum(a)
#     return(b)
# print(sumofallelement([2,3,4,5,6,2]))

###############################################################

'''LIST QUESTION - 9'''

# def findlarge(a):
#     a.sort()
#     return(a[-2])
# print(findlarge([4,6,8,4,2,7,9,0,10]))

###############################################################

'''LIST QUESTION - 13'''

# def findlarge(a):
#     a.sort()
#     return(a[-3])
# print(findlarge([4,6,8,4,2,7,9,0,10]))

###############################################################

'''LIST QUESTION - 10'''

# def primenumber():
#     for i in range(1,21):
#         if (i % 2 == 1):
#             print(i)            
# print(primenumber())

###############################################################

'''LIST QUESTION - 12'''

def removevalue(valueinlist,removeval):
    valueinlist.remove(removeval)
    
print(removevalue([1,2,3,4,5,6,7,8,9,0],6))