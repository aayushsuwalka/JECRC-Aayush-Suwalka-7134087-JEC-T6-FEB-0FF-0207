# Problem 1:
# Calculate electricity bill based on units consumed
# 0-100     5/unit
# 101-300   7/unit
# Above 300 10/unit
# if Bill > 5000  5% discount
# unit = int(input('Enter Unit : '))
# bill_amt = None
# if unit > 0 :
#     if unit <= 100 :
#         bill_amt = unit * 5
#     elif 101 <= unit <= 300 :
#         bill_amt = unit * 7
#     else:
#         bill_amt = unit * 10
#     if bill_amt > 5000:
#         bill_amt = bill_amt * 0.95
#     print(f'Printing the Total Bill : {bill_amt}') # It's F String
# else :
#     print("Enter Valid Units")

# Problem 2:
# Loan approval System
# if 
# salary > 25000
# CIBIL > 700
# salary = int(input('Enter your Salary : ')) 
# cibil = int(input('Enter your CIBIL Score : '))
# if salary >= 25000 and cibil > 700:
#     if salary > 5000 and cibil > 750:
#         print("Will get Instant Approval!!!")
#     else:
#         print("Loan will be approved after background verification")
# else:
#     print('Not Eligible')

# Problem 3:
# WAP to find a year is a Leap year or not
# year = int(input())
# if year%4 == 0 :
#     if year%100 != 0 :
#         print("It is a Leap Year")
#     else:
#         print("It is not a Leap Year")
# elif year%400 == 0 :
#     print("It is a Leap Year")
# else:
#     print("It is not a Leap Year")

# Problem 4:
# To find the ASCII values of the different characters we use ord() function
# print(ord('A'))
# print(ord('a'))
# print(ord('g'))
# If we wnat to  convert one uppercase alphabet to lowercase alphabet then we have to add +32
# If we wnat to  convert one lowercase alphabet to uppercase alphabet then we have to add -32
# print(chr(70))
# print(chr(106))

# Problem 5:
# WAP tp take a character from the user and convert it into lowercase if it is in uppercase or vise-versa
# char = str(input())
# ans = None
# if ord(char) >=65 and ord(char) <=90 :
#     ans = ord(char) + 32
#     print(chr(ans))
# elif ord(char) >=97 and ord(char) <=122 :
#     ans = ord(char) - 32
#     print(chr(ans))
# else :
#     print(char)


# LOOPING STATEMENTS
# ForLoop 
# Syntax : for()
# i = 1
# while i<=5:
#     print(i)
#     i = i+1

# if no of iterations is not mentioned then we can go with the while loop. 
# We have to write everything manually(intialization, condition, updation)
# we can perform iterations on set & dictionary

# for var_name in coll/ref_coll:
    # Statement
    # Block

# Problem 5:
# input_string = str(input())
# ans = None
# res = ''
# i = 1
# for i in input_string : 
#     if ord(i) >=65 and ord(i) <=90 :
#         ans = ord(i) + 32
#         res += chr(ans)
#     elif ord(i) >=97 and ord(i) <=122 :
#         ans = ord(i) - 32
#         res += chr(ans)
#     else :
#         res += i
# print(res)


# Problem 7: 
# WAP to find the max element which int or float of datatype
# list1 = [10, 2.2, 5, 'Hello', [100,200], 99.9]
# max = list1[0]
# for i in list1 :
#     if type(i) in [int, float] : 
#         if i > max :
#             max = i
# print(max)


# Problem 8:
# input : {'a':1, 'b':2}
# output : {1: 'a', 2: 'b'}
# coll = {'a':1, 'b':2}
# new_coll = {}
# for i in coll:
#     new_coll[coll[i]] = i
# print(new_coll)

# Problem 9:
# input : ['Hello', 'Hi', 20, 40.2, 9.6j, [1, 2], 'PYTHON', 'JECRC', (1, 2, 3)]
# output : {'Hello': 'l', 'Hi': 'Hi', 'PYTHON': 'PN', 'JECRC': 'C', (1, 2, 3): 2}
# col = {'Hello', 'Hi', 20, 40.2, 9.6j, [1, 2], 'PYTHON', 'JECRC', (1, 2, 3)}
# new_col = {}
# for i in col :
#     if type(i) in [str, tuple] :
#         if len(i)%2 == 0:
#             new_col[i] = i[0] + i[-1]
#         else:
#             new_col[i] = i[len(i)//2]
# print(new_col)

# Whenever python interpreter will encounter 'break' keyword it will simply stop its execution on this particular line and mke the interpreter to go out of the loop. In future, control will never go inside the same loop
col = [1, 1.2, 3, 4, 5]
i, flag = col[0], True

for j in col: 
    if type(i) == type(j):
        flag = True
    else :
        flag = False
if flag:
    print('Homogenous Collection')
else :
    print('Heterogenous Collection')

