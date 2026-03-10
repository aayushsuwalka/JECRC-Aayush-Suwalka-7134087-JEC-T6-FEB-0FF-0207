import time
'''
Exception Handling

What is Exception ?
# Unauthorized Event
# Flow of execution of the program will be stopped
# After that it will never execute the further code.

'''
# Keywords-
# try: We will put the problem statement(Block of code due to which we might get an error).
# except: We put actual solutin for the reason(resolution for error prome code)
        # due to this block we can prevent the unauthorized events(errors)
        # Purple/Pink -> Exception
        # Red -> Error(classes)
        # Purple -> warning (object) 
# finally: After getting error or after resolution , forcefully if we want to execute block of code, we use it.
# else: It is an alternative of try block. If we find out any error inside try block, interpreter will move forward towards else block.
        # if code is correct(output)
        # if code is incorrect

'''
Exception handling Approaches :--
--> Specific Exception Handling 
    If we are awareof the error or, exception then we can go with 'specific'
--> Generic Exception Handling
    It is a type of exception handling Approach in which there is no need to pass any particular exception class name. Instead of we can use parent "exception" class called "Exception".
    Using "generic exception handling , We vcants 
--> Default Exception Handling
    It is a type of exception Handling in which we can handle all types of errors or exception except 'SyntaxError'

'''
# n1, n2 = 21, 0
# try:
    # problem statement
#     result = n1/n2
#     print(result)
# except ZeroDivisionError:
    # solution code
#     print('Please do not use 0 as a denominator')
# print('code after try except - 01')
# print('code after try except - 02')
# print('code after try except - 03')

# try:
#     a, b, c = 1, 2
# except Exception:
#     print('for performing MVC, no. of should be equals to no of values!')
# # print(a, b, c)


# try:
#     print(a, b, c)
# except Exception:
#     print('Identifiers are not there in the menory')

# try:
#     while True:
#         print(time.time())
# except Exception:
#     print("Loop got Stopped")
    
