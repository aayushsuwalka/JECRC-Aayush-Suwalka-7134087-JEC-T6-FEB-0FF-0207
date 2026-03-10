
'''
raise -->> It is a keyword, which helps us to throw an error in between a program.

Exception Creation,
1. Custom Exception(raise)
    We use pre-built Exception classes according to our requirment.
    raise ValueError('message')
    ValueError : message
2. User-defined Exception(raise)
    It is type of exception in which we can create our own exception classes based upon our own requirement. We can also provide names to those classes according to the use cases.
3. Assertion Exception(assert)
    Assertion exception can be created byu using one keyword called 'assert'
    syntax :-
    assert <condition>, print(ERROR)
    print(output)

'''


# Custom Exception
# num = 16
# if num >= 18:
#     print('You are eligible for voting and driving')
# else:
#     raise NameError('Age should be greater than or equals to 18')

# User-Defined Exception
# class MyException(Exception):
#     pass
# raise MyException("This is my exception class")
# n1, n2 = 10, 5
# if n2 == 0:
#     raise MyException("Second num can not be Zero!")
# else:
#     print(n1 / n2)

# Assert Exception
s = input('Enter a string : ')
assert s == s[::-1], print('It is not a palindromic String!')
print("It is a palindromic String")