'''STACK PROGRAM IN PYTHON USING DIFFERENT METHOD (NON- CLASS BASE) USING TIME FUNCTION'''

# import time

# mystack = []
# size = int(input("Enter the size of strack: "))

# for i in range(size):
#     a = int (input("push element in stack: "))
#     mystack.append(a)
# else:
#     print("stack is full")
#     print(mystack)
    
# print("pop operation start: ")
# for i in range(size):
#     time.sleep(3)
#     print(mystack.pop(),"pop element from stack")
# else:
#     print("stack is empty")
#     print(mystack)
    

'''tower of hanoi'''

# Rules of the game :
# 1. we can move only oe disk at a time
# 2. we have to pick upper disk from any one pipe 
# 3. we have to place on top of any dsk
# 4. we can not place any large disk on top of smaller disk

#self code :
# hanoistack = []
# stackB = []
# stackC = []
# n = int(input("enter of the number element is needed in the hanoi stack: "))

# for i in range(n):
#     a = int (input(" the elements of hanoi stacks: "))
#     hanoistack.append(a)
    
# print(" Stack A = ",hanoistack)
# print("Stack B = ",stackB)
# print("Stack C = ",stackC)

#program - code
# import time
# class tower:
#     def __init__(self):
#         print("Welcome to tower of hanoi game: ")
#         print()
#         print("Given Problem A=[3,2,1]    B=[]   C=[]")
#         print()
#         print("Expected output A=[]    B=[]    C=[3,2,1]")  
#         self.A = []
#         self.B = []
#         self.C = []
        
#     def tower(self,item):
#         self.A.append(item)
#         time.sleep(3)
#         print("A= ",self.A)
#         print("Items in tower A\n") 
        
#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A =",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS ONE COMPLETE===============================\n")
        
#     def pass2(self):
#         self.temp = self.A.pop(1)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS TWO COMPLETE===============================\n")
        
#     def pass3(self):
#         self.temp = self.A.pop(0)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS THREE COMPLETE===============================\n")
        
#     def pass4(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS FOUR COMPLETE===============================\n")
        
#     def pass5(self):
#         self.temp = self.B.pop(1)
#         self.A.append(self.temp)
#         time.sleep(3)
#         print("A",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS FIVE COMPLETE===============================\n")
        
#     def pass6(self):
#         self.temp = self.B.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS SIX COMPLETE===============================\n")
        
#     def pass7(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A",self.A   ,"     ",   "B = ",self.B   , "   ",  "C= ",self.C)
#         print("PASS SEVEN COMPLETE===============================\n")
        
# obj = tower()
# obj.tower(3)
# obj.tower(2)
# obj.tower(1)
# obj.pass1
# obj.pass2
# obj.pass3
# obj.pass4
# obj.pass5
# obj.pass6
# obj.pass7


'''SELECTION SORTING'''

# def find_smallest(list,i):
#     small = list[i]
#     small_i = i
    
#     for i in range(i+1,len(list)):
#         if list[i]<small:
#             small = list[i]
#             small_i = i
#     return small_i 

# def selection_sort(list):
#     for i in range (0,len(list) ):
#         index = find_smallest(list, i)
#         list[i] , list[index] = list[index] , list[i]
#     return list

# print(selection_sort([5,4,2,6,7,1]))


'''write a functin extsort to sort a list of files based on extension'''
# check the exsort.py file in the folder


###############################################################

# import time
# myqueue=[]
# print("QUEUE IMPLEMENTATION")
# print()
# size = int(input("Enter the size of queue: "))


# for i in range(size):
#     a = int(input("ADD ITEM IN QUEUE: "))
#     myqueue.append(a)
# else:
#     print("Queue is full")
#     print("queue elment are = :",myqueue)

# for i in range(size):
#     time.sleep(3)
#     j=0
#     print(myqueue.pop(j),":Remove element from queue")
# else:
#     print("queue is empty")
#     print("queue element are=",myqueue)

###############################################################

'''DOUBLE ENDED QUEUE'''

# import collections

# # initializing deque
# de = collections.deque([1,2,3])
# print("deque: ", de)

# # using append() to insert element at right end
# # insert 4 at th end of deque
# de.append(4)

# # printing modified deque
# print("\n the deque after appending at right is : ")
# print(de)

# # using appendleft() to insert element at left end
# # insert 6 at the beginning of deque
# de.appendleft(6)

# # printing modified deque
# print("\n the deque after appending at left is : ")
# print(de)


# # poping item efficiently 
# import collections

# # initializing deque
# de = collections.deque([6,1,2,3,4])
# print("deque: ",de)

# # using pop() to delete element from right end 
# # deletes 4 from the right end of deque
# de.pop()

# # printing modified deque
# print("\n the deque after deleting from right is : ")
# print(de)

# # using popleft() to delete element from left end
# # delete 6 from the left end og deque
# de.popleft()

# import collections
# de = collections.deque([1,2,3])

# de.extend([4,5,6])

# print("the deque after extending deque at end is : ")
# print(de)

# de.extend([7,8,9])

# print("the deque aftyer extending deque at begining is : ")
# print(de)

# de.rotate(-3)

# print("the deque after rotating deque is : ")
# print(de)

# de.reverse()

# print("the deque after reversing deque is :")
# print(de)