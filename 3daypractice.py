'''FILE HANDLING IN PYTHON'''

# f = open("myfile.text","w")
# print("name of the file",f.name)
# print("file mode",f.mode)
# print("readable",f.readable())
# print("writable",f.writable())
# print("file had closed0",f.closed)
# f.close()
# print("file has closed", f.closed)

# f = open ("file.txt","a")
# f.write("\n Mumbai is the smart city")
# f.close
# print("file operation is done")

# f = open ("file.txt","a")
# f.write("\n dubai is the smart city")
# f.close
# print("file operation is done")

# print the data from the textfile using the print functions
# f = open ("file.txt","r")
# print(f.read())
# print("file operation is done")

# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# a.writerow(["studentid","rollno","name","mobileno"])

# howmany = int(input("How many times you have to enter the values in csv FILE: ")
# studentid = int(input("ENter the student ID:"))
# rollno = int(input("Enter your roll number: "))
# name = input("Enter your name: ")
# mobileno = int(input("Enter the mobile number: "))
# a.writerow([studentid,rollno,name,mobileno])
# print("STUDENT RECORD IS SAVED")


# import csv
# f = open("examresult.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["studentname","studentbranch","studentrollno","Percentage","result"])

# studentname = input("Enter the student name: ")
# studentbranch = input("Enter the student branch: ")
# studentrolllno = int(input("Enter the student Roll No: "))
# paper1 = int(input("Enter the paper 1 marks: "))
# paper2 = int(input("Enter the paper 2 marks: "))
# paper3 = int(input("Enter the paper 3 marks: "))
# paper4 = int(input("Enter the paper 4 marks: "))
# paper5 = int(input("Enter the paper 5 marks: "))
# backendadding = sum([paper1,paper2,paper3,paper4,paper5])
# backendpercentage = (backendadding/500 * 100)
# Percentage = (backendpercentage)
# a.writerow([studentname,studentbranch,studentrolllno,Percentage])
# print("Value is being entered")
# result = print()


'''QUESTION'''
# WAP to find anagrams by taking 2 word and find wheather the 2 word are anagram or not

# wordone = input("Enter the word one: ")
# wordtwo = input("Enter the word two: ")

# if len(wordone) == len(wordtwo):
#     if sorted(wordone) == sorted(wordtwo):
#         print("IT IS ANAGRAM")
# else:
#     print("IT IS NOT THE ANAGRAM") 


'''QUESTION'''
# given a string can i re-arrenage the string to form a palindrome.

# sample input - ""the sun rises in the east"" expected output - ""eht snu ni eht stea"".
"""s = "the sun rises in the east"

words = (s.split())

for i in words:
    print(i)   
    

for i in s:
    if i in "aeiouAEIOU":
        vow = vow + i
    else:
        con = con + i
print( con + vow)
"""

# check for palindrom

# a = "education"
# b = reversed(a)
# print("".join(reversed(a))) # use this to avoid the hex decimal value in output

''' LAMBDA CONCEPTS IN PYTHON'''

# a = lambda x: x*x

# print(a(5))

'''square root question implementation using 2 parameter'''
# root = lambda x , y : (x*x*y*y)**(1/2)
# print(root(5,6))

# take nay number of parameter ; return their average

# ls = [1,2,3]
# print(sum(ls)/len(ls))

# avg = lambda *x: sum(x) / len(x)
# print(avg(4,5,6,87,8,))

'''img noted function'''
# d = lambda s: "".join(set(s))
# print(d("rgfgfgdfgfgfgd"))

'''FUNCTIONAL PREGRAMMING'''
# map(function, iterable)
# filter (function, iterable) 

# print(list(map(int, ["1","2","3","4"])))

# uppercase = lambda x : chr(ord(x) -32)
# list(map(uppercase,"computer"))

'''dictionary'''

# d = {}
# d["name"] = "nameone"
# d["age"] = "age10"
# d["branch"] = "cs"
# print(d.items())

# d = {}
# d["name"] = "nameone"
# d["age"] = "age10"
# d["branch"] = "cs"
# for i, j in d.items():
#     print(i,j)


''''INTERVIEW OUTPUT PREDICTION QUESTION in MCQ'''

'''1'''
# for i in range (1,5):
#     for j in range(1,5):
#         print(i, end=" ")
#     print()
###############################################################
'''2'''
# container = [2,1,4,5,5,4,4,1,1]
# count=0
# even=0
# odd=0
# for i in container :
#     if i ==4:
#         count==count+1
#     elif i==2:
#         even=even+1
#     elif i==5:
#         odd=odd+1
# print(count-even)
# print(count-odd)
###############################################################
'''3'''
# for ch in 'prashantjha':
#     print(ch)
#     if ch=='h' or ch=='j':
#         break
#     print('current letter:',ch)
###############################################################
'''4'''
# count =0 
# odd = 0
# for i in range(1,20):
#     if i%2==0:
#         count = count+1
#     else:
#         odd = odd +1
        
# print("count=",count)
# print("count number=",odd)
###############################################################
'''5'''
# count = 0
# for i in range(9):
#     if i%2 ==0 :
#         print(i)
#     else:
#         print(i)
#         count +=1
# print("count=",count)
###############################################################

'''CODE THE PROGRAM OF THE GIVEN OUTPUT'''

'''1'''
# for i in range(1,6):
#     print(i,i)

# for i,j in zip (range(1,6),range(5,0,-1)): #zip can hold multiple fucntion
#     if i==3 and j==3:
#         continue
#     print(i," ",j)

###############################################################

'''HARD LEVEL QUESTION'''

# def add_student():
#     studentID = input("Enter the student ID: ")
#     studentrolllno = input("Enter the student roll_no: ")
#     studentname = int(input("Enter the student NAME: "))
#     studentcity = int(input("Enter the student CITY: "))


# def show_student():
#     print()
        
    
# def update_student():   


# switcher = {
#     1: add_student,
#     2: show_student,
#     3: update_student,
#     4: delete_student,
#     5: exit
# }