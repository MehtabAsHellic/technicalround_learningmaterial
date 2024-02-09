import time
time.sleep(2)
n=int(input("Enter the number of rows: ")) 
for i in range(1,n+1): 
    print("* "*n)  

#------------------------------------------------

time.sleep(2)
n=int(input("Enter the number of rows: ")) #n=5
for i in range(1,n+1): #i=1  , n=6
    for j in range(1,n+1): # j=1
        print(i,end=" ")
    print()

#------------------------------------------------
time.sleep(2)
n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1): #i=1
    for j in range(1,n+1): #j=2
        print(chr(64+i),end=" ")
    print()

#-------------------------------------------------
time.sleep(2)
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()
time.sleep(2)

#-------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i): 
        print("*",end=" ")
    print()
time.sleep(2)

#-------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print("*"*i)
time.sleep(2)
#-------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(i,end=" ")
    print()
#-------------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(j,end=" ")
    print()
#-------------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(chr(64+i),end=" ")
    print()
#-------------------------------------------------


import time
n=int(input("Enter the number of rows: "))
for i in range(3,n+1):
    time.sleep(1)
    for j in range(1,n+2-i): 
        time.sleep(1)
        print("*",end=" ")
    print()

#-------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    print()

#------------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end=" ")
    print()
time.sleep(2)
#------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end=" ")
    print()

#-----------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-i),end=" ")
    print()

#----------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),"*"*i,end=" ")
    print() 

#-----------------------------------------------

import time
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):   #i=1
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):#3
        time.sleep(1)
        print("*",end=" ")
    print()
#----------------------------------------------


''' y-axis
    |
    |          ^                   "
    |    1 2 3 4     (col=j)
    1          *   
   -2        *   *    
    3         
    4       
    ====================x-axis (i,j)=(2,2)
(row=i)
i=2
j=4'''        





n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(i,end=" ")
    print()

time.sleep(2)
#-------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(j,end=" ")
    print()

#-------------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(chr(64+i),end=" ")
    print()

#----------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        print(chr(64+j),end=" ")
    print()

#--------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(i,end="")
    print()
#--------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(j,end="")
    print()

#-----------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(chr(64+i),end="")
    print()

#--------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1, n+2-i):
        print(chr(64+j),end="")
    print()

#------------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i):
        print(i-j,end=" ")
    for k in range(0,i):
        print(k,end=" ")
    print()
#---------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print() 
#--------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

#------------------------------------------------


for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print("*", end=" ")
    print()
#-----------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(i ,end=" ")
    print()

#---------------------------------------------------

for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(k, end=" ")
    print()
#--------------------------------------------------


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+i) ,end=" ")
    print()
#-------------------------------------------------

for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(chr(64+k), end=" ")
    print()
#------------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#-----------------------------------------------

for k in range(1,n+1):
    for l in range(1,n+2-k):
        print("*",end=" ")
    print()
#----------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#---------------------------------------------
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print(k,end=" ")
    print()

#--------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()

#-------------------------------------------
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print(chr(64+k),end=" ")
    print()

#------------------------------------------

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print()
#-----------------------------------------
for k in range(1,n+1):
    print(" "*(n-k),end=" ")
    for l in range(1,k+1):
        print("*",end=" ")
    print()
#--------------------------------------------

import time
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    time.sleep(1)
    for j in range(i,n+2-i):
        print(j,end=" ")
    print()
#------------------------------------------

for k in range(1,n+1):
    print(" "*(n-k),end=" ")
    time.sleep(1)
    for l in range(1,k+1):
        print(k,end=" ")
    print()
#-----------------------------------------