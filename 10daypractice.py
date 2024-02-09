'''SQL COMMAND'''

'''DDL'''
# create
# alter
# truncate
# drop

'''DML'''
# insert
# update
# delete

'''DCL'''
# grant
# revoke

'''TCL'''
# save point 
# roll back
# commit

'''DQL'''
# select

##############################################################

# solution_set = {5,2,1}
# sum = 0
# while sum == 15:
#     for i in range (0,len(solution_set)):
#         print(i)

##############################################################

# solution_set = []
# coins = [5,2,1]
# sum = 0
# val = 18
# k=0
# j=0
# while sum<18:
#     a = coins[k]
#     j = val//a
#     val = val%a
#     for i in range(j):
#         solution_set.append(a)
#         sum = sum+a
#     k = k+1
# print(solution_set)    

##############################################################

'''TREE CONCEPTS '''

# First, visit all the nodes in the left subtree
# Then the root node
# Visit all the nodes in the right subtree

# class node:
#     def __init__(self, item):
#         self.right = None
#         self.left = None
#         self.val = item
        
# root = node(1)
# # print(root.val)
# root.left = node(2)
# root.right = node(1) 



