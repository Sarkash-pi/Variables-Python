'''
Variable Assignment 
'''

# # add a value to the variable 'name'
# name = 'Sarkash'
# print(name)

#==================><=================
# a = b = c = 'dog'
# print(a)
# print(b)
# print(c)

#==================><=================

# #reuse variable names, so the last assingment will be printed

# colour = 'Red'
# colour = 'Blue'
# print(colour)

#==================><=================

# #legal variable names 
# firstname   = "John"
# first_name  = "John"
# _firs_tname = "John"
# firstName   = "John"
# firstname2  = "John"
# FIRSTNAME   = "John"

# #illigal variable names

# 2firstname = "John" #no number at the beginning 
# first-name = "John" #no hyphen in between 
# first name = "John" #no space in between

#==================><=================

''' 
Reserved Keywords 
'''

# help('keywords') # to print the reserved keywrods in python.
# from = 'London'
# print(from)  # It won't be printed and will get back invalid syntax as 'from' is a reserved keyword

#==================><=================

# variable types

# val = 'Hello world!'
# print(type(val))

# val = 25 
# print(type(val))

''' 
Object Identity
'''
# score = 400
# pb = score 
# print(id(score))
# print(id(pb))

'''
Object Reference 
'''

# both score and pb point to the samee into object
# score --------> int 100 <--------- pb
# score = 100
# pb = score

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

#==================><=================

# garbage collection

# pb     ----------> int 20
# score  ----------> str 'Completed'
#        ----------> int 100

# pb = 20
# score = 100
# score = 'Completed'

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)