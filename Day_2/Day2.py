# LIST
# appen and extend
list1 = [1, 2, 3, 4, 5]
# print(list1)
list1.extend([0, 0, 0, 0])
# print(list1)
list1.append(-1)
# print(list1)
list1.extend(['GM'])
# print(list1)

# Remove Method
list1.remove(5)
# print(list1)
# print(help(list.remove))
list2 = [1, 1, 2, 2, 3, 4, 5, 4 , 5, 5]
list2.remove(5)
# print(list2)
myList = [100, 200.02, 'HELLO', [1, 2, 3]]
# print(myList[len(myList) - 1][len(myList[len(myList)-1])-1])
# print(myList[-2])
# print(myList[-2][-2])

# TUPLE
tpl1 = (1, 2, 3)
# It is a homogenous tuple collection
tp12 = (10, 20, 1.1)
# It is a heterogeneous Collection
# It is a type of collection in which we ca store both same or different data items which will be enclosed between parenthesis.
# It is an immutable collection
tpl3 = 1, 1.1, 1+9j, False, [1, 2], (3, 4), {10, 20}, {1:1, 2:2}
# print(tpl3)

# SET Collection or Multi-Value Data Type
set1 = {1, 2, 3, 'Hello'} # Homogenous
# print(type(set1))
set2 = {1, 1.1, 90+8j}# Heterogenous
# print(set2)
# Set is an unordered collection. No indexing concept will be applied on it.
# print({1, 2, 3, 4 ,3, 2, 1})
# No duplicate values are allowed
# It is a type of collection in which we can store unique homogenoue and heterogenous data items and all the data items will be enclosed between braces and the order will not be followed.
# print(dir(set))
# print(dir(list))
# print([1]+[1])
# print(set1)
# set2 = {1, 3, {1, 2, 3, 4}} # I can't store one inside another set
# print(set2)
# set3 = {1, 2, 3, (1, 2, 3), 30 + 8j}
# print(set3)

# DICTIONARY
# {k1:v1, k2:v2, ......, kn:vn}
# It is a type of collection in which we can store the data in the form of key value pairs which will be wnclosed between braces where key-value pairs will be seperated by comma & key, value will be seperated by colon.
user_info = {
    'userid'   : 8765432147,
    'password' : '*******',
    'location' : 'INDIA'
}
# print(user_info)
# print(type(user_info))
# print(user_info['userid'])
# Adding is_logged_in = True
user_info['is_logged_in'] = True
# print(user_info)
# Update the value
user_info['is_logged_in'] = False
# print(user_info)
d1 = {
    1:'I am int num',
    3.142 : 'Value of Pi',
    0j : 'Default Value',
    'name' : 'Aayush Suwalka'
}

# Mutable Data Type 
mlist = [1, 2, 3]
# print(id(mlist))
mlist[0] = 10
# print(mlist)
# print(id(mlist))
# Firstly I have stored some value inside a memory block. After performing modifiction, the memory address is remaining as it is.
# After storing a value inside a memory block if it is possible to perform some modification 

# Slicing
# Fetching or extracting a part of a collection
# It is supported by those data types who supports indexing concept
# Syntax --->>> var_name/coll[si : ei+-1 : updation/step_value]
# si(starting Index) --->>> from where we have to start.(Default value is 0)
# ei(ending Index) --->>> WHere should I stop ? (exclusive)
# updation/step_value --->>> How to go to the next one ? (+1)
# +1 --> Positive Index --> Left -> Right
# -1 --> Negative Index --> Left <- Right

s = 'HELLO PYTHON'
# print(s[:5:]) # HELLO
# print(s[4::-1]) # OLLEH
# print(s[::-1]) # NOHTYP OLLEH
# print(s[:1:]) # H
# print(s[0:1:1]) # H
# print(s[:1:1]) # H
l = [1, 2, 3, 4, 5]
# print(l[-5:-3:1])

# TYPE CASTING :-
# It is a process of converting one datatype into another datatype
# We can perform typcasting in two different ways 
# 1. Implicit :- Automatically
# print(10 + 5.5)
# 5.5 --> 5 (data Loss)
# 10 --> 10.0
# print(5.5)
# 2. Explicit :- Manually

# int 
# print(complex(10))
# print(bool(10))
# print(str('10'))
# print(tuple(10))
# We can convert "int" into all the SVDs and in case of MVDs, we can only convert it into str

# float
# print(int(10.94))
# print(bool(4.56))
# print(complex(12.453))

# complex
# print(int(5j+1)) #we cannot convert
# print(float(5j+1)) #we cannot convert
# print(bool(5j+1))
# print(str('5j+1'))
# We can convert "complex" only complex & bool in case of SVDs .Only into str, we can convert it.
# str
print(dict(True))


