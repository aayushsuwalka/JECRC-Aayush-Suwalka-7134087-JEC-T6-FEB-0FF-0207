import copy
# Shallow Copy
# org = [[1, 2], [3, 4]]
# sha = copy.copy(org)
# sha[0][0] = 100
# print("Org : ", org)
# print("Sha : ", sha)


# Deep copy
org = [[1, 2], [3, 4]]
sha = copy.deepcopy(org)
sha[0][0] = 100
# print("Org : ", org)
# print("Sha : ", sha)

# Operators
# 1.Arthematic Operators
    # Addition
    # Substraction
    # Multiplication
    # Division
        # True Division(/)
        # Floor Division(//)
        # Modulus(%)
    # Exponential 

# 2.Relational Operator
    # Equal to 
    # Not Equal tom
    # Less Than 
    # Greater Than
    # Less Than or Equal to 
    # More Than or Equal to 

# 3. Logical Operator
    # Logical and(and) -->> If all the conditions are true, then only "and" will return output as true, Otherwise False
    # Logical or(or) -->> If ant one of the 
    # Logical not(not)

# 4. Assignment Operator
    # Assignment(=)
    # Argumented Assignment Operator : +=, -=, *=, /=, //=, %=, etc

# 5. Bitwise Operator
    # Bitwise AND(&)
    # Bitwise OR(|)
    # Bitwise NOT(!)
    # Bitwise XOR(^)
    # Bitwise AND
    # Bitwise AND

# Membership Operator
    # in     -->> It will give output as True if the value belongs to the collecvtion, Otherwise False.
    # not in -->> It will give output as True if the value is not there in the collection , Otherwise True.

# Identity Operator
    # is     -->> It will give output as True if both the values are belongs to the same memory location. Otherwise, False.
    # is not -->> It will give output as True if the values are not pointing towards the same memory location. Otherwise, False.


# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# It is a type of statement which controls the flow of the execution of a program.
## Conditional Statement : Based upon one condition, the flow of the exwcution of a program will be decided.
    # if statement (Simple if)
        # Syntax :
            #  if <condition> :     (if condition is true)
            #      statement Block
    # if else statement,
    # elif statement,
    # nested if statement

# IF Statement --->
# WAP to check whether the username & password is correct or not. if correct print login successfully completed. If not, do nothing.
user = {
    'username' : 'user123',
    'password' : '*****'
}
# un = input("Enter Username : ")
# ps = input("Enter Your Password : ")
# if un == user['username'] and ps == user['password']:
# print("Login Successfully")
# else :
# print("Login Unsuccessfull")

# ELIF Statement --->
# When you have multiple conditions; multiple statement blocks; 
# Atleast one if condition should be there
# WAP in pyhton to take a character from the user and check wheather it is a vowel, or consonent or digit or special character
chr = input('Enter a chr: ')
if chr in 'aeiouAEIOU':
    print('Vowel')
elif chr in '0123456789':
    print('Digit')
elif chr in '!@#$%^&*()`~':
    print('Special Character')
else:
    print("Consonent")
