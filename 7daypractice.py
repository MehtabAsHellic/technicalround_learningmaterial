'''find i value of the smallest number value in the arr / list'''

# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1,len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i  
#     return smallest_index

###############################################################

'''RECURSION'''

# def f(n):
#     return 1+f(n-1)    # ERROR -  RecursionError: maximum recursion depth exceeded

# print(f(6))

###############################################################

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n+f(n-1)

# print(f(6))


###############################################################

# def sum_list(lst):
#     if len(list) !=1:
#         return lst[0] + sum_list(lst[1:])
#     else:
#         return lst[0]

###############################################################

'''REVERSE A STRING USING RECURSION'''

# f("python") =
# "n" + f("python") =
# "n" + "o"
# + f("pyth")

# def substring(string):
#     if len(string) == 1:
#         return string[0]
#     else:
#         return string[-1] + substring(string[0:-1])

# print(substring('python'))


###############################################################

'''WHAT IS DS'''
# Data structure are differently ways to organizing data in your computer, that can be used effectively
# catagoty is LINEAR DS AND NON-LINEAR DS
# SEARCHING, SORTING, QUEUE, LINKLIST - Linear DS
# TREE AND GRAPH - non-linear DS
#  example - organizing event and want to sell ticket and how the organzing team will do that

'''what is algorithm'''
# It is a set of instruction or step by step instruction to finish the task 

'''why dsa is important'''
# as we knpw that for normal processing we have to provide i/p and it processs and then we will 
# get ouput. Simlarly in google ma[ we provide starting location and ending destination points as 
# a input and for processing it used graph algorithm to find shortest path and that is our provessing 
# and finally we will get back our shortest path or root as output