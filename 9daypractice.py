# class stack:
#     def __init__(self):
#         self.list = []
        
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)

#     def isempty(self):
#         if self.list == []:
#             return True
#         else:
#             return False

#     def  push(self,value):
#         self.list.append(value)
#         return "THE ELEMENT IS BEING PUSHED"
    
#     def pop(self):
#         if self.isEmpty():
#             return "this isn no element in the stack"
#         else:
#             return self.list.pop()
        
#     def peek(self):
#         if self.isempty():
#              return "this isn no element in the stack"
#         else:
#             return self.list[len(self.list)-1]
        
#     def delete(self):
#         self.list = None

# ##############################################################

# import sys

# class Stack:
#   def __init__(self):
#     self.list = []
#     print("Stack created successfully")

#   def __str__(self):
#     #values = self.list.reverse()
#     values = [str(x) for x in self.list]
#     return '\n'.join(values)

#   def isEmpty(self):
#     if self.list == []:
#       return True
#     else:
#       return False

#   def push(self, value):
#     self.list.append(value)
#     return "Element inserted successfully"

#   # Removes top element from stack
#   def pop(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     else:
#       return self.list.pop()

#   # Returns top element from stack but doesn't remove it
#   def peek(self):
#     if self.isEmpty():
#       return "There is not any element in the stack"
#     else:
#       return self.list[len(self.list)-1]

#   def delete(self):1
#     self.list = None
#     return "Stack deleted"
# m = True
# while m==True:
#   print("===================================")
#   print("1. Create stack")
#   print("2. IsEmpty")
#   print("3. Push")
#   print("4. Pop")
#   print("5. Peek")
#   print("6. Delete")
#   print("7. Exit")
#   ch = int(input("Enter your choice: "))
#   match ch:
#     case 1:
#       customstk = Stack()
#     case 2:
#       print(customstk.isEmpty())
#     case 3:
#       a = int(input("Enter the value to be inserted: "))
#       print(customstk.push(a))
#     case 4:
#       print(customstk.pop())
#     case 5:
#       print(customstk.peek())
#     case 6:
#       customstk.delete()
#     case 7:
#       m = False

################################################################

# from multiprocessing import Value
# from optparse import Values


# class Stack:
#     def __init__(self, maxsize):
#         self.maxsize = maxsize
#         self.list = []
        
#     def __str__(self) -> str:
#         value = self.list.reverse()
#         value = [str(x) for x in self.list]
#         return '\n'.join(value)

#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
            
#     def isfull(self):
#         if len(self.list) == self.maxsize:
#             return True
#         else:
#             return False
        
#     def push(self):
#         if self.isfull():
#             return "THIS STACK IS FULL"
#         else:
#             self.list.append(Value)
#             return "Element inserted successfully"
    
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.list.pop()

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             return self.list[len(self.list)-1]

#     def delete(self):
#         self.list = None
#         return "Stack deleted"
       
# m = True
# while m==True:
#   print("===================================")
#   print("1. Create stack")
#   print("2. IsEmpty")
#   print("3. Push")
#   print("4. Pop")
#   print("5. Peek")
#   print("6. Delete")
#   print("7. Exit")
  
#   ch = int(input("Enter your choice: "))
#   match ch:
#     case 1:
#       customstk = Stack()
#     case 2:
#       print(customstk.isEmpty())
#     case 3:
#       a = int(input("Enter the value to be inserted: "))
#       print(customstk.push(a))
#     case 4:
#       print(customstk.pop())
#     case 5:
#       print(customstk.peek())
#     case 6:
#       customstk.delete()
#     case 7:
#       m = False

# def deque(self):
#     if self.isempty():
#         return "tyhis is no element in the que"
#     else:
#         return self.items.pop(0)

##############################################################

'''linear search pseudocode question'''
# 1. create functions with two parameter which are an array and a value
# 2. loop through the array and check if the current array element is equal to the value
# 3. if it return the index at which the element is found
# 4. if the value is never found the return -1

# def linearsearch(array,value):
#     for i in range(len(array)):
#         if array[i] == value:
#             return i
#     return -1

# print(linearsearch([20,40,30,50,90],90))

##############################################################

'''Binary search pseudocode'''
# 1. create a function with two parameter which are a sprted array and a value 
# 2. create two pointers: a left pointer is in start of the array and the right 
# pointer is in the end of the array
# 3. while middle is not equal to the value and start<=end loop:
#     if the miidle is greater than the value move the right
# pointer down:
#     if the middle is less than the vlaue move the left
# pointer up
# 4. if the value never found than return -1

##############################################################

# class node:
#     def __init__(self, value):
#         self.value = value 
#         self.next = None
        
# new_node = node(10)
# print(new_node.value)

# class linkedlist:
#     def __init__(self , value):
#         new_node = node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 0
        
# new_linked_list = linkedlist(10)
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)

# class node:
#     def __init__(self, value):
#         self.value = value 
#         self.next = None
        
#     def __str__(self):
#         temp_mode = self.head
#         result = ' '
#         while temp_mode is not None:
#             result += str(temp_mode.value)
#             if temp_mode.next is not None:
#                 result += ' -> '
#             temp_mode = temp_mode.next
#         return result
    
#     def append(self, value):
#         new_node = node(value)
#         if self.head is new_node:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.lengh += 1
        
    
# linked_list = linkedlist()
# linked_list.append(10)
# print(linked_list)