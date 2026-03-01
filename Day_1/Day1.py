# class AddTwoNum:
#     @staticmethod
#     def result(n1, n2):
#         return n1+n2
# print(AddTwoNum(10,20))~
# Variable is  a name given to a memory block where theb actual value is stored
# a = 30
# b = a # It will provide a new memry block with the memory address of a.
# a = a + b  
# print(a,b)
# print(id(30))
# print(id(60))



# Multiple Variable Creation:-
# It is a process of creating n numbers of variable in a single.
# In case of MVC, no. of variables should be equal to no. of values.
# a, b, c, d = 1, 2, 3, 4, 5
# print(a, b, c, d, e)

# Identifier:-
# it is name given to identify something.
# It is a name given to a variable/class/function/module to identify it.
# We can't put any numeric value at the starting of an identifier name
# We can't put any spaces at the begining or middle or at the ending in the idnetifier name 
# is_logged_in = True
# we can't use keyword name and any specical character in and as an identifier name 
# Identifiers names are Case Sensitive Values
# _ character shows the prvious executed value


# Library Functions :-
# These are the type of function which is already predefined by the devs.
# If we want, 
#           1. We can access them 
#           2. We can also use them
#           3. We can't modify its functionality
# print(help('keywords'))

# Keywors :-
# import keyword
# var_name == kwlist
# print(len(keyword.kwlist))
# 1. Special Keyword :- False, True, None (We can treat them as a value and can store there reference in some variable, also we can use them as a resultant of a condition)
# a = True
# b = False
# c = None
# p
# p = None
# 2. Soft Keyword :- We  can treat them as a variable name
# type = 'HELLO'
# print(type)
# case = 200
# print(case)
# match = 30 
# print(match)
# False = 0 (Not allowed , will give error )


# Q. Why "keywords" are known as "Universal Standard Words" ?
# Most of the keywords are same for multiple programming languages

# DataTypes :-
# Data- -
# DataType :- It is used to specify what type of data is stored in the memory
# print(type(10))
# print(type('Hello'))
# print(type(None))
# print(type([1, 2, 3]))
# 1. Single Vale
    #   Numeric:
    #       int     
    #       float   
    #       complex 
    #   Bool:
    #       False
    #       True
    #   NoneType:
    #       None
# 2. Multi Value
    #   string
    #   list
    #   tuple
    #   set
    #   dict

# Integer <class='int'>
# int is nothing but a number which dosen't have any decimal point & fractional part.
# Range :- -ve Infinite,....., -2, -1, 0, 1, 2,....., +ve Infinite
# Memory Allocation :- 
# num = 100
# print(num)
# print(n) it shows NameError

# Floating Point Number, float: <class 'float'>
# It is a type of number which consists of both  decimal and fractional part
# Range :- -ve Infinity,.....,-1.3, -0.45, 0, 0.45, 1.3, +ve Infinity
# print(type(3.22))
# print(type(-8.45))

# Complex Number, complex: <class 'complex'>
# a+-bi
# print(type(20 + 9j))
# print(type(1.34320 + 9j))
# print(type(20 + 9.67564j))
# Rules :- 
# 1. It is possible to represent a +-bj <---> +-bj + a  
# 2. We can't switch the position of b & j
# 3. For defining a complex number we can't loose the value for bj
# print(type(1)) It is integer
# 4. Only "bj" is enough to represent a complex number
# print(type(4j))
# 5. in case of complex number, we can only use "j" or "J" to represent the imaginary number

# Bool, Boolean: <class 'bool'>
# It is a type of single value or individual data type which have exactly two values , One is "True" and another is "False".
# <class 'bool'> is a sub class of <class 'int'>
# True  --> 1
# False --> 0
# print(True + True + False) # 2
# print(20 * False) # 0

# String, str: <class 'str'>
# Whatever values are there inside quotes (single/double/triple) is known as string.
# Characters
    # - Alphabets [Uppercase / Lowercase]
    # - Digits [0123456789]
    # - Special Characters [!@#$%^&*()]
# print('Hello World')
# msg = "Pyhton Practice"
# print(msg)
# print(type(msg))
# myName = "Aayush"
# print(len(myName))

# Q. When should I use single quote('' or "") ?
#   we can use both of them anywhere but when there a multiple quates in a line we use double quotes 
# msg = 'Python'
# print(msg)
# msg1 = "Rahul's Batch"
# print(msg1)
# para = '''Hello 
# Heyyy
# Hieeee
# Hi
# Hlw'''
# print(para)

# Indexing 
#  1. Positive Indexing
        # si -> 0
        # ei -> len(coll) - 1
        # index will traverse from left to right side 
# () - Parenthesis
# {} - Braces/Curly Braces/ Flower Braces
# [] - Only Braces/ Square Braces
#  2. Negative Indexing
#  


# Default & Non-Default Values 
#          0 1 2 3 
# -3 -2 -1 0 
# Default values are the initial values for any datatype.
# data_type ## default value for a particular data type.
# Apart from default value all other values will be considered as non-default values.
# print(int())
# print(float())
# print(complex())
# print(bool())
# print(str())
# print(len(str()))
print(bool(0))
print(bool(1))